
# Healthcare Network Optimisation

In order to enhance the efficiency of ambulance services and emergency medical responses in Algiers, Algeria, our objective is to optimize ambulance routes, patient transfers, and overall emergency response times. Specifically, our focus is on determining the most optimal route for patients requiring hospital or clinic visits within Algiers.



## Strategies 
The Strategies used are :
A*,
UCS,
Bidiractional BFS,
Hill Climbing.

These strategies were used to find shortest path from initial coordinates of intersection to goal coordinates of an intersection.

The goal is  to evaluate and compare the effectiveness of these strategies in optimizing emergency medical responses within Algiers.

## Data Generated
We gathered the data about hospitals and clinics (coordinates, emergency services, capacity) from google maps and different resouces. Then we divided the data hospital in 3 seperate files (west, center, east)

We gathered the data about intersections of roads and edges between them from turbo overpass website as OSM file  then from it we generated 2 csv files one for the nodes(coordinates, direction ) and other for the edges between them.

## Problem Formulation 
the graph is our  transitional model such
the nodes  are the intersections of roads, and the edges are the roads between the intersections. Then, we save the graph in the format pkl , then we copied the object of graph and apply the search strategies on it.

## Credit:
HADJ MESSAOUD Maria
BAZOULA Nouha
ABDELI zahra
BENBOUABDELLAH Nadia
