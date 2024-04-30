from collections import deque


class Node:
    def __init__(self, state, coordinates, heuristic,parent=None, destination=None, cost=0):
        self.coordinates = coordinates
        self.heuristic = heuristic
        self.state = state
        self.parent = parent  # node
        self.destination = destination
        self.cost = cost  # (incremented with each newly expanded node)
        if parent is None:  # root node
            self.depth = 0  # level in the graph 0 for the root node
        else:
            self.depth = parent.depth + 1  # parent level + 1

    def __hash__(self):
        if isinstance(self.state, list):
            return hash(tuple(map(tuple, self.state)))
        else:
            return hash(self.state)

    def __eq__(self, other):
        if isinstance(other, Node):
            return other.state == self.state 
        else:
            return False

    

    def __gt__(self, other):
        return (self.cost + self.heuristic) > (other.cost + other.heuristic)

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
