import csv
from Node import Node
from graph import Graph
from UCS import ucs

from queue import PriorityQueue
from Problem import Problem

from Bidirectional_BFS import Bidirectional_BFS

from Astar import Astar



G = Graph()

all_nodes=[]
with open('nodes.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    
    
    for line in csv_reader:
        ID, x, y=line #retrieve the data in this order
        node=Node(int(ID),(float(x),float(y)))
        all_nodes.append(node)
            
with open('doc.csv', 'r') as csv_file:   #open the edges file
    csv_reader = csv.reader(csv_file)    
    next(csv_reader)
    
    for line in csv_reader:
        source=int(line[0])
        target=int(line[1])
        cost=float(line[2])
        bi=int(line[5])
        
        for s in all_nodes:           #go through all nodes in the list 
            if(s.id==source):         #find source node in the list 
                for t in all_nodes:
                    if(t.id==target):   #when source is found , find target
                        G.add_edge(s,t,cost,bi)   #the objects are directly added
                        

#problem
ini=G.get_node(940)
print (f"this is initial state:  {ini.id}")


goal=G.get_node(944)
print (f"this is goal state:  {goal.id}")

ourprob=Problem(G,ini,goal)

""" 
path=ucs(ourprob)

#printing the path
for node in path:
    print(f"this is node : {node.id}")
    print("-----------------------------")

     """
""" 
path=Bidirectional_BFS(ourprob)

#printing the path
for node in path:
    print(f"this is node : {node.id}")
    print("-----------------------------")
 """
 

path=Astar(ourprob)

#printing the path
for node in path:
    print(f"this is node : {node.id}")
    print("-----------------------------")

                        
                        
#G.printGraph()