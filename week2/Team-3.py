class Graph:

    def __init__(self, Matrix):
        # create a graph from  passed 2d matrix
        # creating an n*m matrix
        self.Matrix = Matrix
        self.n = len(Matrix)
        self.m = len(Matrix[0])

    def printGraph(self):
        # print the graph
        for i in range(self.n):
            for j in range(self.m):
                print(self.Matrix[i][j], end=" ")
            print("\n")

    def Degree(self, vertex):
        degree = 0
        for j in range(self.n):
            if self.Matrix[vertex][j] == 1:
                degree += 1
        return degree


empty_graph = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]

simple_graph = [[0, 1, 1, 1],
                [1, 0, 1, 0],
                [1, 1, 0, 0],
                [1, 0, 0, 0]]

grid_3_3 = [[0, 1, 0, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 1, 0, 1, 0]]

if __name__ == "__main__":
    graph = Graph(grid_3_3)
    print(graph.Degree(0))
