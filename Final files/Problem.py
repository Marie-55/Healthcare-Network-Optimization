
class Problem:
    def __init__(self, graph, initial_state, goal_state):
        self.graph = graph   #takes a dictionary as a transitional model (representing a graph)
        self.initial_state = int(initial_state)
        self.goal_state = int(goal_state)

    def goal_test(self, state): 
        return state == self.goal_state
    
    def expand_node(self,node):
        return self.get_neighbours(node)
    
    
    #manipulation of the transitional model (the graph)
    def get_neighbours(self,node1):
        node= self.graph[str(node1)]
        return node['neighbors']  #returns the neighbors of the node in the graph (with all its iformation : id, length , speed and type)
    
    def get_best_neighbor(self, node): #function that returns the best neighbor ( considering the cost)
        neighbors = self.get_neighbours(node)
        best_neighbor = min(neighbors, key=lambda x: x['length']) #iterate over the list of neighbors and get the min cost 
        return best_neighbor
    
    def get_node(self,node):      #returns a function with all its information ( coordinates, neighbors)
        print ("inside find")
        return self.graph[str(node)]
        

    def get_cost(self,node1,node2):   #returns the cost between 2 nodes
        
        if node1== node2:
            return 0
        
        neighbors=self.get_neighbours(node1)
        for neighbor in neighbors:
            if neighbor['target']==node2:
                return float(neighbor['length'])
            
        neighbors=self.get_neighbours(node2)
        for neighbor in neighbors:
            if neighbor['target']==node1:
                return float(neighbor['length'])
            
    
    def get_id(self,node):
        return self.graph[str(node)]['id']
    
    def get_total_cost(self,path):     #count a total path 
        total=0
        for i in range(0,len(path)-2):
            total=total+self.get_cost(path[i],path[i+1])
            
        return total
    
    
    def Get_coord(self,node):
        N=self.graph[str(node)]
        coordinates=N['coordinates']
        return coordinates['lon'],coordinates['lat']
            
        
        
        
        
    def printGraph(self):
        
        
        count = 0
        for node in self.edges.keys():
            print(f"Node: {node.id}")
            for neighbor, cost in self.edges[node]:
                print(f"  Edge to {neighbor.id} with cost {cost}")
            count += 1
            if count == 5:
                break  
                
           
    
        