import pickle
import csv
import pandas as pd
from Node import Node
from graph import Graph
from Problem import Problem

import time


start_time = time.time()
G = Graph()

# Read the nodes from the CSV file using pandas
nodes_df = pd.read_csv("finalnode.csv")

# Create a dictionary mapping node IDs to Node objects
node_dict = {row["ID"]: Node(row["ID"], (row["lat"], row["lon"])) for _, row in nodes_df.iterrows()}

# Read the edges from the CSV file using pandas
edges_df = pd.read_csv("finaledge.csv")

# Iterate over the edges and create edges in the graph
for _, row in edges_df.iterrows():
    source_id = row["source"]
    target_id = row["target"]
    cost = row["length"]
    bi = row["bidirectional"]

    source_node = node_dict[source_id]
    target_node = node_dict[target_id]  

    G.add_edge(source_node, target_node, cost, bi)
end_time = time.time()

# Rest of your code...
print("finished")

execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")
print("=============================")

# Serialize the graph object to a file
with open('graph.pkl', 'wb') as f:
    pickle.dump(G, f)

# Load the pickle file
with open('graph.pkl', 'rb') as f:
    reconstructed_graph = pickle.load(f)
    
reconstructed_graph.printGraph()

