from Harvensine import Distance_Haversine


def Goal_test(current_node, goal_node):
    if Distance_Haversine(current_node.Get_coord(), goal_node.Get_coord()) <= 100:
        return True
    return False


def Hill_Climbing(Problem, max_sideways):

    closed = set()
    Initial_node = Problem.initial_state
    Goal_node = Problem.goal_state
    Initial_heuristic = Distance_Haversine(Initial_node.Get_coord, Goal_node.Get_coord)

    if Goal_test(Initial_node, Goal_node):
        return "Success"

    closed.add(Initial_node)

    Current_Node = Initial_node
    Current_heuristic = Initial_heuristic

    # Not ensure that we are at better or same quality state
    Not_Worst = True

    sideways_moves = 0

    while Not_Worst and sideways_moves <= max_sideways:
        Not_Worst = False
        prev_heuristic = Current_heuristic
        for successor_node, successor_cost in Problem.expand_node(Current_Node):
            if successor_node in closed:
                continue
            successor_heuristic = Distance_Haversine(
                successor_node.Get_coord, Goal_node.Get_coord
            )

            if successor_heuristic <= Current_heuristic:
                Current_Node = successor_node
                Current_heuristic = successor_heuristic
                Not_Worst = True

                if Goal_test(Current_Node, Goal_node):
                    return "Success"
        if Current_heuristic == prev_heuristic:
            sideways_moves += 1
        else:
            sideways_moves = 0
    return "False"
