import csv
from Node import Node
from graph import Graph


G = Graph()

all_nodes=[]
with open('n.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    
    
    for line in csv_reader:
        ID, x, y,name=line #retrieve the data in this order
        if(name ==""):
            node=Node(ID,(x,y))
            all_nodes.append(node)
        else:
            node=Node(ID,(x,y),name)
            all_nodes.append(node)
            
with open('docs.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    
    for line in csv_reader:
        source=line[0]
        target=line[1]
        cost=line[2]
        bi=line[5]
        
        for s in all_nodes:
            if(i.id==source):
                for t in all_nodes:
                    if(t.id==target):
                        add_edge(i,t,cost,bi)
                        
                        
                        
G.printGraph()