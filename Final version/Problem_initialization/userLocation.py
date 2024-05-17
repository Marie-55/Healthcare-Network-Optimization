from math import radians, sin, cos, sqrt, atan2
from Problem_initialization import Harvensine


# import From another directory 
import sys

# Add the directory to sys.path
sys.path.insert(
    1,
    "\Problem_initialization",
) 




def find_closest_node(user_location, graph):

    closest_node_id = None
    min_dist = float("inf")


    for key, node in graph.items():

        coord = node["coordinates"]
        x = coord["lat"]
        y = coord["lon"]
        node_coords = (x, y)

        dist = float(Harvensine.Distance_Haversine(user_location, node_coords))


        if dist < min_dist:

            min_dist = dist
            closest_node_id = node["id"]

        """ else:
                # Skip empty lines
                continue """

    
    return closest_node_id

