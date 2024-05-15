import csv
import json

from UCS import ucs

from queue import PriorityQueue
from Problem import Problem

from Bidirectional_BFS import Bidirectional_BFS

from Astar import Astar


from HillClimbing import Hill_Climbing
import pickle
import time

start_read=time.time()



with open('output2.json', 'r') as json_file:
    graph = json.load(json_file)
    
    #to test that the dict is working
    '''
    for node,node_info in json_read.items():
        print (f"Node:{node} ")
        print(f'coordinates:')
        coordinates=node_info['coordinates']
        x=coordinates['lon']
        y=coordinates['lat']
        print(f'x= {x}, y={y}')
        print(f'neighbors:')
        
        for neighbor in node_info['neighbors']:
            target= neighbor['target']
            length= neighbor['length']
            print(f'neighbor id: {target}, cost={length}')
        '''
        
#testig the problem functions:
ourprob=Problem(graph,1,1236)
print('the nrighbors of node 940:')
print(ourprob.get_neighbours(940)) #works
print ("===============================")
print('our best neighbor: ')
print(ourprob.get_best_neighbor(940)) #works just fine
print("=======================================")
print(ourprob.get_node(940))  #works
print("====================================")
print(ourprob.get_cost(940,6383))
print("======================================")
#_________________print(ourprob.Get_coord(940))
#let's test the HC:
#__________________print(Hill_Climbing(ourprob,10)) #wooooorkksss
#let's test bidirectional
'''
path=Bidirectional_BFS(ourprob)
for node in path:
    print(f"this is node : {node}")
    print("-----------------------------")

#BFS WORKINGGG
     '''

#let's test the ASTAR

'''
path=Astar(ourprob)
for node in path:
    print(f"this is node : {node}")
    print("-----------------------------")
''' #worksss
#let's test the UCS:
path=Hill_Climbing(ourprob,20)
for node in path:
    print(f"this is node : {node}")
    print("-----------------------------")
     
""" #workssss
            
with open('doc.csv', 'r') as json_file:   #open the edges file
    csv_reader = csv.reader(csv_file)    
    next(csv_reader)
    
    for line in csv_reader:
        source=int(line[0])
        target=int(line[1])
        cost=float(line[2])
        speed=int(line[4])
        bi=int(line[5])
        
        for s in all_nodes:           #go through all nodes in the list 
            if(s.id==source):         #find source node in the list 
                for t in all_nodes:
                    if(t.id==target):   #when source is found , find target
                        G.add_edge(s,t,cost,bi)   #the objects are directly added
                        
                        
                        
end_read= time.time()
elapsed_time= end_read-start_read
print(f"finished reading the files in__ {elapsed_time}")
print("=============================")



print(f"finished search in__ {elapsed_time}")
print("=============================")



# Serialize the graph object to a file
with open('graph.pkl', 'wb') as f:
    pickle.dump(G, f)

# Load the pickle file
with open('graph.pkl', 'rb') as f:
    reconstructed_graph = pickle.load(f)
    
reconstructed_graph.printGraph()



start_strategy=time.time()
#problem
ini=G.get_node(940)
print (f"this is initial state:  {ini.id}")


goal=G.get_node(944)
print (f"this is goal state:  {goal.id}")



ourprob=Problem(G,ini,goal)

print(f"{Hill_Climbing(ourprob,10)}")
end_strategy=time.time()

elapsed_time= end_strategy-start_strategy
miaw=Bidirectional_BFS(ourprob)

print("==================")

my_path=path(miaw,G)

p=steepest_ascent_search(my_path,G, 500)
#printing the path
for node in miaw:
    print(f"this is node : {node.id}")
    print("-----------------------------")
"""

""" 

print("==================")

my_path=path(miaw,G)

p=steepest_ascent_search(my_path,G, 500)

#printing the path
for node in p:
    print(f"this is node : {node.id}")
    print("-----------------------------")

 """""" 
path=Bidirectional_BFS(ourprob)

#printing the path
for node in path:
    print(f"this is node : {node.id}")
    print("-----------------------------")
"""
 
""" 
path=Astar(ourprob)

#printing the path
for node in path:
    print(f"this is node : {node.id}")
    print("-----------------------------")

"""                       
                        
#G.printGraph()