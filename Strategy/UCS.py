from queue import PriorityQueue
from Problem import Problem


def ucs(Problem):
    initial_state = Problem.initial_state
    frontier = PriorityQueue()   #The frontier is a priority queue so we can get the node with the lowest cost
    frontier.put((0, initial_state))  #the cost of the initial state is zero
    explored = set()
    
    # the parent dictionary is used to retrieve the path after the goal is found
    # where the key is the node and the value is its parent
    parent={initial_state:None}
    
    while not frontier.empty():
        #get the node with the lowest cost from the priority queue
        cost, current_node=frontier.get()
        
        if Problem.goal_test(current_node):
            path=[]
            #retrieve the path by climbing up the graph
            while current_node is not None:
                path.append(current_node)
                current_node=parent[current_node]
            #reverse so we get from the initial state to goal state not the opposite
            path.reverse()
            #we return the path 
            return path
        
        if current_node not in explored:
            explored.add(current_node)
            
            for neighbor, neighbor_cost in Problem.expand_node(current_node):
                #we calculate the total cost by adding the cost of neighbor node and the cost of its parent
                neighbor_Total_cost = cost + neighbor_cost
                #add the neighbor to the frontier only if it is not in the explored set
                
                if neighbor not in explored:
                    frontier.put((neighbor_Total_cost,neighbor))
                    parent[neighbor]=current_node
        
    return []
        
