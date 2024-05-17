from Problem_initialization import userLocation
import json
import time
from Problem_initialization import suitable_hospital_finding
from Problem import Problem
import folium
import os

# import From another directory 
import sys

# Add the directory to sys.path
sys.path.insert(
    1,
    "\Problem_initialization",
) 

from General_Search import General_Search

# Construct the file path
file_path = os.path.join(os.path.dirname(__file__), 'data', 'road_graph.json')

start = time.time()

# Create The graph
with open(file_path, "r") as json_file:
    graph = json.load(json_file)


# change here get the user input from the user
x = float(36.70344692041837)
y = float(3.094759595910879)
use_location = (x, y)
# find closest interesction from the user
initial_node_id = userLocation.find_closest_node(use_location, graph)


end = time.time()


# get its coordinates
initial_coord = (
    graph[str(initial_node_id)]["coordinates"]["lat"],
    graph[str(initial_node_id)]["coordinates"]["lon"],
)



# find the relevant hospital
Nearest_hospital, distance_hosp, hosp_coord = suitable_hospital_finding.Relevant_Hospital(
    initial_coord, "Pediatric Emergency"
)
# find the closest inter to the Hospital
goal_node_id = userLocation.find_closest_node(hosp_coord, graph)


end = time.time()


Our_prob = Problem(graph, initial_node_id, goal_node_id)

# let's test the UCS:
path_coord = []
path = General_Search(Our_prob,"Bidirectional")
for node in path:
    coord = (
        graph[str(node)]["coordinates"]["lat"],
        graph[str(node)]["coordinates"]["lon"],
    )
    path_coord.append(coord)
    print(f"this is node : {node}")
    print("-----------------------------")

# Create map with an initial location
mymap = folium.Map(location=[36.7538, 3.0588], zoom_start=12)

for i, coord in enumerate(path_coord):
    folium.CircleMarker(coord, radius=5, fill_opacity=0).add_to(mymap)

folium.PolyLine(path_coord, weight=2.5, opacity=1).add_to(mymap)
mymap.get_root().html.add_child(
    folium.Element(
        """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    """
    )
)

# Save map to HTML file
mymap.save("hospitals_map_BID.html")
