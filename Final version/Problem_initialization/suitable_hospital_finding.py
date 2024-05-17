from Problem_initialization import isWhere
import pandas as pd
from tkinter import *
import pandas as pd
from Problem_initialization import Harvensine
import os


# import From another directory 
import sys

# Add the directory to sys.path
sys.path.insert(
    1,
    "\Problem_initialization",
) 

#import all data files that we need using their path

East_hospitals = os.path.join(os.path.dirname(__file__),'..', 'data', 'hospitals_clinics_east.csv')

Center_hospitals = os.path.join(os.path.dirname(__file__),'..', 'data', 'hospitals_clinics_center.csv')

West_hospitals = os.path.join(os.path.dirname(__file__),'..', 'data', 'hospitals_clinics_west.csv')


def finding_hopital(file, selected_service,user_coordinates):

    Min_distance = float("inf")
    Nearest_Hospital = None
    df = file
    nearest_coord = None
    x, y = user_coordinates
    for index, row in df.iterrows():
        services = row["services"].strip('""').split(",")
        if selected_service in services and row["Capacity"] > 0:
            lat, lon = row["coordinates"].split(",")
            lat = float(lat)
            lon = float(lon)
            # x and y are global variables
            distance = Harvensine.Distance_Haversine((float(x),float(y)), (lat, lon))
            if distance < Min_distance:
                Min_distance = distance
                Nearest_Hospital = row['facility']
                nearest_coord = (lat, lon)

    return Nearest_Hospital, Min_distance, nearest_coord


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
    Algiers_region = isWhere.is_Where(coordinates)
    # Initialize variables
    Min_distance = float("inf")
    Nearest_Hospital = None
    nearest_coord = None

    # Find the nearest hospital based on the Algiers region
    if Algiers_region == "East":
        file = pd.read_csv(East_hospitals)
        Nearest_Hospital, Min_distance, nearest_coord = finding_hopital(file, service,coordinates)

        # If no hospital is found in the East region, search in the Center region
        if Nearest_Hospital == None:
            file = pd.read_csv(Center_hospitals)
            Nearest_Hospital, Min_distance, nearest_coord = finding_hopital(
                file, service,coordinates
            )

            # If no hospital is found in the Center region, search in the West region
            if Nearest_Hospital == None:
                file = pd.read_csv(West_hospitals)
                Nearest_Hospital, Min_distance, nearest_coord = finding_hopital(
                    file, service,coordinates
                )

    elif Algiers_region == "West":
        file = pd.read_csv(West_hospitals)
        Nearest_Hospital, Min_distance, nearest_coord = finding_hopital(
                    file, service,coordinates
                )

        # If no hospital is found in the West region, search in the Center region
        if Nearest_Hospital == None:
            file = pd.read_csv(Center_hospitals)
            Nearest_Hospital, Min_distance, nearest_coord = finding_hopital(
                file, service,coordinates
            )

            # If no hospital is found in the Center region, search in the East region
            if Nearest_Hospital == None:
                file = pd.read_csv(East_hospitals)
                Nearest_Hospital, Min_distance, nearest_coord = finding_hopital(
                    file, service,coordinates
                )

    elif Algiers_region == "Center":
        file = pd.read_csv(Center_hospitals)
        Nearest_Hospital, Min_distance, nearest_coord = finding_hopital(file, service,coordinates)

        # If no hospital is found in the Center region, search in the East region
        if Nearest_Hospital == None:
            file = pd.read_csv(East_hospitals)
            Nearest_Hospital, Min_distance, nearest_coord = finding_hopital(file, service,coordinates)

            # If no hospital is found in the East region, search in the West region
            if Nearest_Hospital == None:
                file = pd.read_csv(West_hospitals)
                Nearest_Hospital, Min_distance, nearest_coord = finding_hopital(
                    file, service, coordinates
                )

    else:
        print("Please enter a valid location in Algiers")

    if Nearest_Hospital == None:
        return "Sorry! There is no hospital with this service"

    return Nearest_Hospital, Min_distance, nearest_coord

