from queue import PriorityQueue
from collections import deque
from math import radians, sin, cos, sqrt, atan2
from Problem_initialization import Harvensine


# import From another directory 
import sys

# Add the directory to sys.path
sys.path.insert(
    1,
    "\Problem_initialization",
) 




def Astar(Problem):
    Initial_state = Problem.initial_state      #ID of the initial state
    goal_state = Problem.goal_state            #ID of the goal state
    
    heuristic_init = Harvensine.Distance_Haversine(Problem.Get_coord(Initial_state), Problem.Get_coord(goal_state))
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
                priority = child['length'] + Harvensine.Distance_Haversine(Problem.Get_coord(child_id), Problem.Get_coord(goal_state)) + chosen_priority - Harvensine.Distance_Haversine(Problem.Get_coord(Chosen_node), Problem.Get_coord(goal_state))
                if child_id not in explored and child_id not in frontier.queue:
                    frontier.put((priority, child_id))
                    parent[child_id]=Chosen_node
