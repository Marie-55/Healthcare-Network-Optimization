from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()  # to avoid redundancy 
        self.edges = defaultdict(set) # dictionnary
        

    def add_node(self,node):
        self.nodes.append(node) # adding a node to the set of nodes

    def add_edge(self, node1, node2, cost, b):  # b is a temporary parameter meant to check if the edge is bidirectional or not ;)
        self.edges[node1].add((node2,cost))
        self.nodes.add(node1)
        self.nodes.add(node2)
        if b == 1:
            self.edges[node2].add((node1,cost))

    def get_neighbors(self,node1): #get the list of neighbors in the form of tuple
        return self.edges[node1]
    
    def get_best_neighbor(self, node): #might be modified later for the search algo
        neighbors = self.get_neighbors(node)
        best_neighbor = min(neighbors, key=lambda x: x[1]) #iterate over the list of neighbors and get the min cost 
        return best_neighbor


      def printGraph(self):
        count = 0
        for node in self.edges.keys():
          print(f"Node: {node}")
          for neighbor, cost in self.edges[node].items():
            print(f"  Edge to {neighbor} with cost {cost}")
          count += 1
          if count == 5:
            break  
