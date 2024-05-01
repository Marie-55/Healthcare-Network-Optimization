from graph import Graph
from collections import deque

def Bidirectional_BFS(problem):
    #if dir == 0 then search starts from start state else it staterts from goal

    initial= problem.initial_state
    goal= problem.goal_state 

        
    frontier_front= deque()   #keeps nodes to be expanded from intial state
    explored_front= set() #keeps explored nodes from front
    frontier_front.append(initial)
    parent_front={initial:None}
    
    frontier_back= deque()     #frontiere from backward bfs
    explored_back= set() #keeps explored  nodes from back
    frontier_back.append(goal)
    parent_back={goal:None}

    
    #path={initial:None}    #list to keep the track
    
    while frontier_front and frontier_back:
        
        if frontier_front:
            chosen_front= frontier_front.popleft()
            if chosen_front == goal or chosen_front in frontier_back:
                path=[]
                temp=chosen_front
                while temp is not None:
                    path.append(temp)
                    temp=parent_front[temp]
                path.reverse()
                temp=parent_back[chosen_front]
                while temp is not None:
                    path.append(temp)
                    temp=parent_back[temp]
                    
                return path
            
            else:
                explored_front.add(chosen_front)
                
                for neighbor,_ in problem.expand_node(chosen_front):
                    if neighbor not in explored_front and neighbor not in frontier_front:
                        frontier_front.append(neighbor)
                        parent_front[neighbor]=chosen_front
                        
        if frontier_back:
            chosen_back= frontier_back.popleft()
            if chosen_back == initial or chosen_back in frontier_front:
                path=[]
                temp=chosen_back
                while temp is not None:
                    path.append(temp)
                    temp=parent_front[temp]
                path.reverse()
                temp=parent_back[chosen_back]
                while temp is not None:
                    path.append(temp)
                    temp=parent_back[temp]
                    
                return path
            
            else:
                explored_back.add(chosen_back)
                
                for neighbor,_ in problem.expand_node(chosen_back):
                    if neighbor not in explored_back and neighbor not in frontier_back:
                        frontier_back.append(neighbor)
                        parent_back[neighbor]=chosen_back
                        
                        
    return false