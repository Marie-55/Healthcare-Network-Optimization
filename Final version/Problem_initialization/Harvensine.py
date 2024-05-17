from math import radians, sin, cos, sqrt, atan2


def Distance_Haversine(
    initial_coordinates, goal_coordinates
):  # calculate the distance between coordinates
    lat1, lon1 = initial_coordinates
    lat2, lon2 = goal_coordinates
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    h = 6371e3 * c
    return round(h, 3)


""" print(
    f"harvey is bithcing : {Distance_Haversine((36.70344692041837, 3.094759595910879),(36.7050725,3.0946176))}"
) """

# Chatttty shit
""" def Distance_Haversine(initial_coordinates, goal_coordinates):
    # Calculate the distance between coordinates
    lat1, lon1 = initial_coordinates
    lat2, lon2 = goal_coordinates
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    radius_earth_km = 6371
    distance = radius_earth_km * c
    return round(distance, 3) """
