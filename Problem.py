class Problem:
    def __init__(self, graph, initial_state, goal_state):
        self.graph = graph
        self.initial_state = initial_state
        self.goal_state = goal_state

    def is_goal_state(self, state): 
        return state == self.goal_state