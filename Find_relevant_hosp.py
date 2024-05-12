#find the hospital that satisfy the patient's emergency service with shortest path 
from isWhere import is_Where
import pandas as pd
from Harvensine import Distance_Haversine

def finding_hopital(file, coordinates, service):
    client_lat, client_lon = coordinates
    client_service = service
    Min_distance = float("inf")
    Nearest_Hospital = None
    df = file
    for index, row in df.iterrows():
        services = row['services'].strip('""').split(',')
        if client_service in services and row["Capacity"] > 0:
            lat, lon = row["coordinates"].split(",")
            lat = float(lat)
            lon = float(lon)
            distance = Distance_Haversine((client_lat, client_lon), (lat, lon))
            if distance < Min_distance:
                Min_distance = distance
                Nearest_Hospital = row["facility"]

    return Nearest_Hospital, Min_distance

import pandas as pd

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
        Nearest_Hospital, Min_distance = finding_hopital(file, coordinates, service)
        
        # If no hospital is found in the East region, search in the Center region
        if Nearest_Hospital == None:
            file = pd.read_csv("hospitals_clinics_center.csv")
            Nearest_Hospital, Min_distance = finding_hopital(file, coordinates, service)
            
            # If no hospital is found in the Center region, search in the West region
            if Nearest_Hospital == None:
                file = pd.read_csv("hospitals_clinics_west.csv")
                Nearest_Hospital, Min_distance = finding_hopital(file, coordinates, service)
    
    elif Algiers_region == "West":
        file = pd.read_csv("hospitals_clinics_west.csv")
        Nearest_Hospital, Min_distance = finding_hopital(file, coordinates, service)
        
        # If no hospital is found in the West region, search in the Center region
        if Nearest_Hospital == None:
            file = pd.read_csv("hospitals_clinics_center.csv")
            Nearest_Hospital, Min_distance = finding_hopital(file, coordinates, service)
            
            # If no hospital is found in the Center region, search in the East region
            if Nearest_Hospital == None:
                file = pd.read_csv("hospitals_clinics_east.csv")
                Nearest_Hospital, Min_distance = finding_hopital(file, coordinates, service)
    
    elif Algiers_region == "Center":
        file = pd.read_csv("hospitals_clinics_center.csv")
        Nearest_Hospital, Min_distance = finding_hopital(file, coordinates, service)
        
        # If no hospital is found in the Center region, search in the East region
        if Nearest_Hospital == None:
            file = pd.read_csv("hospitals_clinics_east.csv")
            Nearest_Hospital, Min_distance = finding_hopital(file, coordinates, service)
            
            # If no hospital is found in the East region, search in the West region
            if Nearest_Hospital == None:
                file = pd.read_csv("hospitals_clinics_west.csv")
                Nearest_Hospital, Min_distance = finding_hopital(file, coordinates, service)
    
    else:
        print("Please enter a valid location in Algiers")
    
    if Nearest_Hospital == None:
        return "Sorry! There is no hospital with this service"
    
    return Nearest_Hospital, Min_distance

print("Dear client enter your coordinates :")

near, distance = Relevant_Hospital((36.7483, 3.2459), "Gynecology Emergency")
print(f"near hospital is : {near}")
print(f"distance is : {distance}")
