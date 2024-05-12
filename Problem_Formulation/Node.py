from collections import deque


class Node:
    def __init__(self,id, coordinates,name= "intersection"):
        self.id = id
        self.coordinates = coordinates
        self.name = name

        # getters for the coordinates 
    @property 
    def long(self):
        return self.coordinates[0]
        
    @property 
    def lat(self):
        return self.coordinates[1]
        

    def __hash__(self):
        if isinstance(self.id, list):
            return hash(tuple(map(tuple, self.id)))
        else:
            return hash(self.name)

    def __eq__(self, other):
        if isinstance(other, Node):
            return other.coordinates == self.coordinates 
        else:
            return False

    def Get_coord(self):
        return self.coordinates
    
    def get_id(self):
        return self.id
""" 
Might be used somewhere else 
    def __gt__(self, other):
        return (self.cost + self.heuristic) > (other.cost + other.heuristic)

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
 """
