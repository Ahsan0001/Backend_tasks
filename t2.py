#T2 Task 1 -> degree
import matplotlib.pyplot as plt
import networkx as nx

def degree(graph, vertex):
    degree = 0
    #print(graph)
    rows = len(graph) # getting rows of graph
    columns = len(graph[0] ) # getting columns of graph
    #print(rows)
    #print(columns)
    for x in range (columns):
        if graph[vertex][x] == 1:
            degree= degree+1
    print("degree is: ")
    print (degree)
    print("HELLO WORLD")


empty_graph = [[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]]

simple_graph = [[0,1,1,1],
               [1,0,1,0],
               [1,1,0,0],
               [1,0,0,0]]


grid_3_3 = [[0, 1, 0, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 1, 0, 1, 0]]


degree(empty_graph, 0)
degree(simple_graph, 1)
degree(grid_3_3, 0)
degree(grid_3_3, 1)
print("adasdadasda")
