from collections import deque

def Bidirectional_BFS(problem):
    #if dir == 0 then search starts from start state else it staterts from goal

    initial= int(problem.initial_state)
    goal= int(problem.goal_state) 

        
    frontier_front= deque()   #keeps nodes to be expanded from intial state
    explored_front= set() #keeps explored nodes from front
    frontier_front.append(initial)
    parent_front={initial:None}
    
    frontier_back= deque()     #frontiere from backward bfs
    explored_back= set() #keeps explored  nodes from back
    frontier_back.append(goal)   #takes it as a node with all its attributes
    parent_back={goal:None}  #dictionary parent: child -----> to get the final path

    
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
                
                
                for neighbor in problem.expand_node(chosen_front):
                    neighbor_id=neighbor['target']
                    neighbor_node= problem.get_node(neighbor_id)

                    if neighbor_id not in explored_front and neighbor_node not in frontier_front:
                        frontier_front.append(neighbor_id)
                        parent_front[neighbor_id]=chosen_front
                        
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
                
                for neighbor in problem.expand_node(chosen_back):
                    neighbor_id=neighbor['target']
                    neighbor_node= problem.get_node(neighbor_id)
                    if neighbor_id not in explored_back and neighbor_node not in frontier_back:
                        frontier_back.append(neighbor_id)
                        parent_back[neighbor_id]=chosen_back
                        
                        
    return False