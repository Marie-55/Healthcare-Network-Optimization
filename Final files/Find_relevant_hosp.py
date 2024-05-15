from isWhere import is_Where
import pandas as pd
from Harvensine import Distance_Haversine
from tkinter import *
from PIL import Image, ImageTk
from Harvensine import Distance_Haversine
import pandas as pd
import csv

_OPTIONS = [
    "Burn Center",
    "Cardiac Emergency",
    "Dental Emergency",
    "Diabetology Emergency",
    "General Emergency",
    "Gastrointestinal Emergency",
    "Gynecology Emergency",
    "Infectious Disease Emergency",
    "Medical-Surgical Emergency",
    "Medical-Surgical Emergency",
    "Neurological Emergency",
    "Ophtalmology Emergency",
    "ORL",
    "Orthopedic Emergencies",
    "Pediatric Emergency",
    "Psyciatric Emergency",
    "Renadial Hemodialysis",
    "respiratory emergencies",
    "Trauma center"
]

_options = [
    "5",
    "10",
    "15",
    "20",
    "25",
    "30"]

master = Tk()
master.geometry("500x700") 
master.title("Service Menu")  

img = Image.open("doctor.jpg")
photo = ImageTk.PhotoImage(img)

canvas = Canvas(master, width=master.winfo_width(), height=master.winfo_height())
canvas.pack(fill="both", expand=True)

img_x = (master.winfo_width() - img.width)/ 2 + 80
img_y = (master.winfo_height() - img.height) / 2 + 180

canvas.create_image(img_x, img_y, image=photo, anchor="nw")

label1 = Label(master, text="Please select the needed information:")
label1.pack(pady=10)  
label1.config(font=("Arial", 16))
label2 = Label(master, text="enter your coordinates:")
label2.pack(pady=20)  
label2.config(font=("Arial", 16))


def store_selected_information():
    global selected_service
    selected_service = str(variable.get())
    entered_coordinates = coordinates.get()
    global x
    global y
    x, y = entered_coordinates.split(',')
    master.destroy()
    

variable = StringVar(master)
variable.set("Medical service") # ask user for the needed service 


coordinates = StringVar(master)

c = Entry(master, textvariable=coordinates)
c.config(font=("Arial", 14), bg="#B9D9EB", fg="black", width=25)
c.pack(pady=25)
# Create the OptionMenu widget
w = OptionMenu(master, variable, *_OPTIONS)
w.config(font=("Arial", 14), bg="#B9D9EB", fg="black", width=20)  # Configure visual properties


w.pack(pady=20)

button = Button( master, text = "select" , command = store_selected_information,bg="#ffffff", fg="#72A0C1", font=("Arial", 14), padx=10, pady=5, borderwidth=-1,relief="raised").pack()

label = Label(master, text=" ")
service = label.pack()
mainloop()

#find the hospital that satisfy the patient's emergency service with shortest path 


def finding_hopital(file, selected_service):
    client_service = selected_service
    Min_distance = float("inf")
    Nearest_Hospital = None
    df = file
    for index, row in df.iterrows():
        services = row['services'].strip('""').split(',')
        if selected_service in services and row["Capacity"] > 0:
            lat, lon = row["coordinates"].split(",")
            lat = float(lat)
            lon = float(lon)
            distance = Distance_Haversine((float(x), float(y)),(lat, lon))
            if distance < Min_distance:
                Min_distance = distance
                Nearest_Hospital = row["facility"]

    return Nearest_Hospital, Min_distance



def Relevant_Hospital(coordinates, service):
    """
    Finds the nearest hospital based on the given coordinates and service.

    Args:
        coordinates (tuple): The latitude and longitude of the client's location.
        service (str): The required service.

    Returns:
        tuple: A tuple containing the nearest hospital and the minimum distance to it.
            If no hospital is found, returns a string indicating that there is no hospital with the given service.
    """
    # Determine the region of Algiers based on the coordinates
    Algiers_region = is_Where(coordinates)

    # Initialize variables
    Min_distance = float("inf")
    Nearest_Hospital = None

    # Find the nearest hospital based on the Algiers region
    if Algiers_region == "East":
        file = pd.read_csv("hospitals_clinics_east.csv")
        Nearest_Hospital, Min_distance = finding_hopital(file, service)
        
        # If no hospital is found in the East region, search in the Center region
        if Nearest_Hospital == None:
            file = pd.read_csv("hospitals_clinics_center.csv")
            Nearest_Hospital, Min_distance = finding_hopital(file, service)
            
            # If no hospital is found in the Center region, search in the West region
            if Nearest_Hospital == None:
                file = pd.read_csv("hospitals_clinics_west.csv")
                Nearest_Hospital, Min_distance = finding_hopital(file, service)
    
    elif Algiers_region == "West":
        file = pd.read_csv("hospitals_clinics_west.csv")
        Nearest_Hospital, Min_distance = finding_hopital(file, service)
        
        # If no hospital is found in the West region, search in the Center region
        if Nearest_Hospital == None:
            file = pd.read_csv("hospitals_clinics_center.csv")
            Nearest_Hospital, Min_distance = finding_hopital(file, service)
            
            # If no hospital is found in the Center region, search in the East region
            if Nearest_Hospital == None:
                file = pd.read_csv("hospitals_clinics_east.csv")
                Nearest_Hospital, Min_distance = finding_hopital(file, service)
    
    elif Algiers_region == "Center":
        file = pd.read_csv("hospitals_clinics_center.csv")
        Nearest_Hospital, Min_distance = finding_hopital(file, service)
        
        # If no hospital is found in the Center region, search in the East region
        if Nearest_Hospital == None:
            file = pd.read_csv("hospitals_clinics_east.csv")
            Nearest_Hospital, Min_distance = finding_hopital(file, service)
            
            # If no hospital is found in the East region, search in the West region
            if Nearest_Hospital == None:
                file = pd.read_csv("hospitals_clinics_west.csv")
                Nearest_Hospital, Min_distance = finding_hopital(file, service)
    
    else:
        print("Please enter a valid location in Algiers")
    
    if Nearest_Hospital == None:
        return "Sorry! There is no hospital with this service"
    
    return Nearest_Hospital, Min_distance


near, distance = Relevant_Hospital((x,y),selected_service)
print(f"near hospital is : {near}")
print(f"distance is : {distance}")