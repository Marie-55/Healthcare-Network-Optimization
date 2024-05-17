import sys
from Strategy import UCS
from Strategy import Bidirectional_BFS
from Strategy import HillClimbing
from Strategy import Astar



sys.path.insert(1,"\Strategy")


def General_Search(Problem, Strategy):
    if Strategy == "Astar":
        return Astar.Astar(Problem)
      
    elif Strategy == "UCS":
        return UCS.ucs(Problem)
      
    elif Strategy == "Bidirectional":
        return Bidirectional_BFS.Bidirectional_BFS(Problem)
      
    elif Strategy == "Hill Climbing":
        return HillClimbing.Hill_Climbing(Problem,10)
    else:
      return "Strategy not Found"
