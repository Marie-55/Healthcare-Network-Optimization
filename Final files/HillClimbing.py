from Harvensine import Distance_Haversine


def Goal_test(current_coord, goal_coord):
    if Distance_Haversine(current_coord, goal_coord) <= 100:
        return True
    return False


def Hill_Climbing(Problem, max_sideways):

    closed = set()
    Initial_node = Problem.initial_state
    Goal_node = Problem.goal_state
    Initial_heuristic = Distance_Haversine(Problem.Get_coord(int(Initial_node)), Problem.Get_coord(int(Goal_node)))
    parent={Initial_node:None}
   
    closed.add(Initial_node) #closed set keeps the IDS of the visited nodes

    Current_Node = Initial_node
    Current_heuristic = Initial_heuristic

    if Goal_test(Problem.Get_coord(Initial_node),Problem.Get_coord( Goal_node)):
        return "PATH IS EMPTY"


    closed.add(Initial_node) #closed set keeps the IDS of the visited nodes

    Current_Node = Initial_node
    Current_heuristic = Initial_heuristic

    # Not ensure that we are at better or same quality state
    Not_Worst = True

    sideways_moves = 0
    print(Not_Worst)
    print(sideways_moves)
    while Not_Worst and sideways_moves <= max_sideways:
        Not_Worst = False
        prev_heuristic = Current_heuristic
        for successor_node in Problem.expand_node(Current_Node): #takes the node and expands it (returns its neighbors)
            target=successor_node['target']
            if target in closed:  #check if the node is already visited
                continue
            successor_heuristic = Distance_Haversine(
                Problem.Get_coord(target), Problem.Get_coord(Goal_node)
            )

            if successor_heuristic <= Current_heuristic:
                parent[target]=Current_Node
                Current_Node = target
                Current_heuristic = successor_heuristic
                Not_Worst = True

                if Goal_test(Problem.Get_coord(Current_Node),Problem.Get_coord( Goal_node)):
                    
                    path=[]
                    while Current_Node is not None:
                        print(type(Current_Node))
                        path.append(Current_Node)
                        Current_Node=parent[Current_Node]

                    path.reverse()
                    return path
                
        if Current_heuristic == prev_heuristic:
            sideways_moves += 1
        else:
            sideways_moves = 0
        
    return "False"
