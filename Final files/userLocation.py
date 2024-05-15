import csv
from math import radians, sin, cos, sqrt, atan2


# get the cowl flew distance from the current node to the goal node
def get_cowl_flew_distance(coordinates, goal_coordinates):
# Get latitude and longitude coordinates for each city
    lat1, lon1 = coordinates
    lat2, lon2 = goal_coordinates
# Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
# Calculate the straight-line distance using Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    h = 6371 * c # Radius of the Earth in kilometers
    return h

def find_closest_node(user_location):
    
    closest_node_id = None
    with open('nodes.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        min_dist = float('inf')
        for line in csv_reader:
            print("now reading")
            ID, x, y=line #retrieve the data in this order
            node_coords = (float(x),float(y))
            print("node cords: ",node_coords)
            dist = float(get_cowl_flew_distance(user_location, node_coords))
            print("distance is: ", dist)
            print("min dist : ",min_dist)
            print("node id : ", ID)
            if dist < min_dist:
                print("val before ", min_dist)
                min_dist = dist
                closest_node_id = ID
                print("val after : ",min_dist)
                print("node id : ",closest_node_id)
            """ else:
                    # Skip empty lines
                    continue """

    return closest_node_id


# Ask the user to enter their location
user_input = input("Enter your coordinates (latitude, longitude) separated by a comma: ")
user_location = tuple(map(float, user_input.split(",")))

# Find the closest node
closest_node = find_closest_node(user_location)
print(f"The closest node to your location is node with ID: {closest_node}")
                        
