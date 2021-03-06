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

    def is_path(self, path):  # path is a list of vertices
        for i in range(len(path) - 1):
            if self.Matrix[path[i]][path[i + 1]] == 0:
                return False
        return True

    def print_as_grid(graph, n):  # print Graph as grid n = row size and column size
        for i in range(n):
            for j in range(n):
                print(graph.Matrix[i][j], end=" ")
            print("\n")

    def BFS_traversal(self, start):
        # BFS traversal of the graph
        visited = [False] * self.n
        queue = []
        queue.append(start)
        visited[start] = True
        while queue:
            start = queue.pop(0)
            print(start, end=" ")
            for i in range(self.n):
                if self.Matrix[start][i] == 1 and visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def DFS_traversal(self, start):
        # DFS traversal of the graph
        visited = [False] * self.n
        stack = []
        stack.append(start)
        visited[start] = True
        while stack:
            start = stack.pop()
            print(start, end=" ")
            for i in range(self.n):
                if self.Matrix[start][i] == 1 and visited[i] == False:
                    stack.append(i)
                    visited[i] = True

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



#
# if __name__ == "__main__":
#     # graph = Graph(grid_3_3)
#     # print(graph.Degree(0))
#     # graph.BFS_traversal(0)
