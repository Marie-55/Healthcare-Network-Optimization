from Node import Node
from queue import PriorityQueue
from collections import deque
from math import radians, sin, cos, sqrt, atan2


def Distance_Hversine(initial_coordinates, goal_coordinates): #calculate the distance between coordinates 
  lat1, lon1 = initial_coordinates
  lat2, lon2 = goal_coordinates
  lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
  dlat = lat2 - lat1
  dlon = lon2 - lon1
  a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
  c = 2 * atan2(sqrt(a), sqrt(1 - a))
  h = 6371e3 * c 
  return round(h, 3)

def Astar(Problem):
    Initial_state = Problem.initial_state    
    goal_state = Problem.goal_state
    heuristic_init = Distance_Hversine(Initial_state.Get_coord(), goal_state.Get_coord())
    frontier = PriorityQueue()
    frontier.put((heuristic_init, Initial_state))
    
    parent={Initial_state:None}

    explored= set()
    while frontier:
        chosen_priority, Chosen_node = frontier.get()
        if Problem.goal_test(Chosen_node):
            path=[]
            #retrieve the path by climbing up the graph
            while Chosen_node is not None:
                path.append(Chosen_node)
                Chosen_node=parent[Chosen_node]
            #reverse so we get from the initial state to goal state not the opposite
            path.reverse()
            #we return the path 
            return path
            
        else:
            explored.add(Chosen_node)
            Children  = Problem.expand_node(Chosen_node)
            for child, cost in Children:
                priority = cost + Distance_Hversine(child.Get_coord(), goal_state.Get_coord()) + chosen_priority - Distance_Hversine(Chosen_node.Get_coord(), goal_state.Get_coord())
                if child not in explored and child not in frontier.queue:
                    frontier.put((priority, child))
                    parent[child]=Chosen_node
