from graph import Graph
class Problem:
    def __init__(self, graph, initial_state, goal_state):
        self.graph = graph
        self.initial_state = initial_state
        self.goal_state = goal_state

    def goal_test(self, state): 
        return state == self.goal_state
    
    def expand_node(self,node):
        return self.graph.get_neighbors(node)
    
        
