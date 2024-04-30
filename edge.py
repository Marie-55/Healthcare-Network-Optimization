#edge class definition
class Edge:
    def __init__(self,source,dest,cost):
        self.source=source # source node 
        self.destination=dest # destination node
        self.cost=cost #cost of the edge
        
    def Get_cost(self):
        return self.cost
    
    def Get_source(self):
        return self.source
    
    def Get_dest(self):
        return self.destination 
    
    def __eq__(self, other): #check if the edge is the same as another
        if ((self.source == other.source) and (self.destination==other.destination)  ):
            return True
        return False
    
    def __lt__(self,other):
        return self.cost < other.cost
    
    def __gt__(self,other):
        return self.cost > other.cost
    
    