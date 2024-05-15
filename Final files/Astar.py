
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
    Initial_state = Problem.initial_state      #ID of the initial state
    goal_state = Problem.goal_state            #ID of the goal state
    
    heuristic_init = Distance_Hversine(Problem.Get_coord(Initial_state), Problem.Get_coord(goal_state))
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
            for child in Children:
                child_id=child['target']
                child_node=Problem.get_node(child_id)
                priority = child['length'] + Distance_Hversine(Problem.Get_coord(child_id), Problem.Get_coord(goal_state)) + chosen_priority - Distance_Hversine(Problem.Get_coord(Chosen_node), Problem.Get_coord(goal_state))
                if child_id not in explored and child_id not in frontier.queue:
                    frontier.put((priority, child_id))
                    parent[child_id]=Chosen_node
