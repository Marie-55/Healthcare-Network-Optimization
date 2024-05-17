from tkinter import *
from PIL import Image, ImageTk
import webbrowser
import folium
import pandas as pd
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable

import json
import time

#import local files 
from Problem import Problem
from General_Search import General_Search
from Problem_initialization import suitable_hospital_finding
from Problem_initialization import userLocation

# import From another directory 
import sys
import os

# Add the directory to sys.path
sys.path.insert(
    1,
    "\Problem_initialization",
) 

# Construct the file path for the graph
file_path = os.path.join(os.path.dirname(__file__), 'data', 'road_graph.json')


# Construct the file path for the image
image = os.path.join(os.path.dirname(__file__),'VisualizationResources', 'doctors.jpg')


# List of service options
_OPTIONS = [
    "Gynecology Emergency", "Infectious Disease Emergency", "Renadial Hemodialysis",
    "Orthopedic Emergencies", "Trauma center", "Psyciatric Emergency",
    "Ophtalmology Emergency", "Cardiac Emergency", "Medical-Surgical Emergency",
    "Neurological Emergency", "respiratory emergencies", "General Emergency",
    "ORL", "Pediatric Emergency", "Dental Emergency", "Gastrointestinal Emergency",
    "Burn Center", "Medical-Surgical Emergency", "Diabetology Emergency"
]
#choose strategy
strategy_options = ["Bidirectional", "UCS", "Astar","Hill Climbing"]


master = Tk()
master.state('zoomed')  
master.title("Service Menu") 
img = Image.open(image)
img = img.resize((int(master.winfo_screenwidth()), int(master.winfo_screenheight()*0.995)))
photo = ImageTk.PhotoImage(img) 
canvas = Canvas(master, width=master.winfo_width()+600, height=master.winfo_height()+300)
canvas.pack(fill="both", expand=True)

# Center the image on the canvas
img_x = (master.winfo_width()) 
img_y = (master.winfo_height()-200) 
canvas.create_image(img_x, img_y, image=photo, anchor="nw")

#create dropdown for strategies
label_s = Label(master, text="Select an option from the dropdown menu:")
label_s.pack(pady=10) 
label_s.config(font=("Arial", 16)) 
variable_strategy = StringVar(master)
variable_strategy.set("Choose a strategy")
w = OptionMenu(master, variable_strategy, *strategy_options)
w.config(font=("Arial", 14), bg="#B9D9EB", fg="black", width=20)  # Configure visual properties
w.pack(pady=20)

#drop down for services
variable = StringVar(master)
variable.set("Choose a service")

# Create the OptionMenu widget
w = OptionMenu(master, variable, *_OPTIONS)
w.config(font=("Arial", 14), bg="#B9D9EB", fg="black", width=20)  # Configure visual properties
w.pack(pady=20)

# Create an input box for the address
address_label = Label(master, text="Enter your coordinates")
address_label.config(font=("Arial", 14), fg="black", width=20)
address_label.pack(pady=5)
coordinates = Entry(master, font=("Arial", 12), fg="black", width=30, borderwidth=2, justify="center")
coordinates.pack(pady=5)

## Store the selected service and user coordinates
def store_selected_input(): 
    global selected_service, user_coordinates # Make the variables global so they can be accessed outside the function
    global strategy
    strategy = str(variable_strategy.get())
    selected_service = str(variable.get())
    user_coordinates = tuple(map(float, coordinates.get().split(','))) 
    master.destroy()

# button to submit the selected service and strategy and coordinates
button = Button(
    master, text="Submit", command=store_selected_input, bg="#B9D9EB", fg="black",
    font=("Arial", 14), padx=10, pady=5, borderwidth=0, relief="raised", width=10, border= 2
).pack(pady=20)
label = Label(master, text=" ")
service = label.pack()
mainloop()

# Create map with an initial location
mymap = folium.Map(location=[36.7538, 3.0588], zoom_start=12)

try:
    # Function to handle click event on map
    geolocator = Nominatim(user_agent="MyPythonScript")
    patient_location = user_coordinates

    # Create The graph
    with open(file_path, "r") as json_file:
        graph = json.load(json_file)

    #find the nearesr intersection from the user location
    initial_node_id = userLocation.find_closest_node(patient_location, graph)

    # get its coordinates
    initial_coord = (
        graph[str(initial_node_id)]["coordinates"]["lat"],
        graph[str(initial_node_id)]["coordinates"]["lon"],
    )

    # Find nearest hospital
    #Nearest_Hospital, Min_distance, nearest_coord
    nearest_hospital,distance,hospital_coordinates = suitable_hospital_finding.Relevant_Hospital(initial_coord, selected_service)
    
    # find the closest inter to the Hospital
    goal_node_id = userLocation.find_closest_node(hospital_coordinates, graph)

    #apply search algorithm
    Our_prob = Problem(graph, initial_node_id, goal_node_id)
    # let's test the UCS:
    path_coord = []
    path = General_Search(Our_prob, strategy)
    for node in path:
        coord = (
            graph[str(node)]["coordinates"]["lat"],
            graph[str(node)]["coordinates"]["lon"],
        )
        path_coord.append(coord)

    # Add marker for patient location
    popup_text = f"Patient Location"
    popup = folium.Popup(popup_text, max_width=250)
    folium.Marker(location=patient_location, popup=popup, icon=folium.Icon(color="blue", prefix='fa', icon='user')).add_to(mymap)

    # Add marker for nearest hospital
    x,y = hospital_coordinates
    hospital_location = tuple(map(float,(x,y)))
    folium.Marker(location=hospital_location, popup=nearest_hospital, icon=folium.Icon( color="red", prefix='fa', icon='hospital')).add_to(mymap)

    # list of intersections to be marked
    for i, coord in enumerate(path_coord):
            folium.CircleMarker(coord, radius=5, fill_opacity=0).add_to(mymap)

    # Add the patient's location as the first point and the hospital's location as the last point in the path_coord list
    path_coord.insert(0, patient_location)
    path_coord.append(hospital_location)

    # Draw line between all points in the path_coord list
    folium.PolyLine(path_coord, weight=2.5, opacity=1).add_to(mymap)
    #icons takne from fontawesome website 
    mymap.get_root().html.add_child(folium.Element("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    """))

    # Save map to HTML file
    mymap.save("final_test.html")
    webbrowser.open("final_test.html")

except GeocoderUnavailable:
    print("Error: Could not find location!! Please check your input and try again.")
