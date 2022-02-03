from collections import defaultdict, deque
import random


class Graph:
    def __init__(self, num):
        self.adj_matrix = [[0] * num for _ in range(num)]
        self.adj_list = defaultdict(list)
        self.edge_list = []
        self.number_of_vertices = num

    def gen_adj_matrix(self):
        saturation = 0.25 * self.number_of_vertices * (self.number_of_vertices - 1)
        edges = 0
        for y in range(self.number_of_vertices - 2):
            x = random.randint(y + 1, self.number_of_vertices - 1)
            self.adj_matrix[y][x] = 1
            edges += 1
        while edges < saturation:
            y = random.randint(0, self.number_of_vertices - 2)
            x = random.randint(y + 1, self.number_of_vertices - 1)
            if self.adj_matrix[y][x] == 1:
                continue
            else:
                self.adj_matrix[y][x] = 1
                edges += 1

    def gen_adj_list(self):
        for y in range(self.number_of_vertices):
            for x in range(self.number_of_vertices):
                if self.adj_matrix[y][x] == 1:
                    self.adj_list[y].append(x)

    def gen_edge_list(self):
        for y in range(self.number_of_vertices):
            for x in range(self.number_of_vertices):
                if self.adj_matrix[y][x] == 1:
                    self.edge_list.append([y, x])

    def input_adj_matrix(self):
        for i in range(self.number_of_vertices):
            adjacency = [0] * self.number_of_vertices
            while True:
                try:
                    adjacency = list(map(int, input("Enter adjacency values of vertex {}: ".format(i)).split()))
                except ValueError:
                    continue
                else:
                    if len(adjacency) != self.number_of_vertices:
                        continue
                    else:
                        break
            self.adj_matrix[i] = adjacency

    def print_adj_matrix(self):
        print("Adjacency matrix of the graph: ")
        for i in range(self.number_of_vertices):
            print(self.adj_matrix[i])

    def print_adj_list(self):
        print("Adjacency list of the graph: ")
        for key in self.adj_list:
            print(key, end='')
            for item in self.adj_list[key]:
                print(" -> {}".format(item), end="")
            print()

    def print_edge_list(self):
        print("Edge list of the graph: ")
        for item in self.edge_list:
            print(item)

    def dfs_utility(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        for consequent in self.adj_list[vertex]:
            if consequent not in visited:
                self.dfs_utility(consequent, visited)

    def dfs(self):
        visited = set()
        print("Deep First Search: ")
        for vertex in list(self.adj_list):
            if vertex not in visited:
                self.dfs_utility(vertex, visited)

    def bfs(self):
        visited = [False] * (max(self.adj_list) + 1)
        queue = deque()
        print("Breadth First Search: ")
        for vertex in list(self.adj_list):
            if not visited[vertex]:
                visited[vertex] = True
                queue.append(vertex)
                while queue:
                    vertex = queue.popleft()
                    print(vertex, end=' ')
                    for consequent in self.adj_list[vertex]:
                        if not visited[consequent]:
                            queue.append(consequent)
                            visited[consequent] = True

    def topological_dfs_utility(self, vertex, visited, stack, rep_type):
        visited[vertex] = True
        if rep_type == '1':
            for i in range(self.number_of_vertices):
                if not visited[i] and self.adj_matrix[vertex][i] == 1:
                    self.topological_dfs_utility(i, visited, stack, rep_type)
        elif rep_type == '2':
            for i in self.adj_list[vertex]:
                if not visited[i]:
                    self.topological_dfs_utility(i, visited, stack, rep_type)
        elif rep_type == '3':
            for i in self.edge_list:
                if i[0] == vertex and not visited[i[1]]:
                    self.topological_dfs_utility(i[1], visited, stack, rep_type)
        stack.append(vertex)

    def topological_dfs(self, rep_type):
        visited = [False] * self.number_of_vertices
        stack = []
        for i in range(self.number_of_vertices):
            if not visited[i]:
                self.topological_dfs_utility(i, visited, stack, rep_type)
        print("Graph topologically sorted via DFS: ")
        print(stack[::-1])

    def topological_bfs(self, rep_type):
        in_degree = [0] * self.number_of_vertices
        if rep_type == '1':
            for y in range(self.number_of_vertices):
                for x in range(self.number_of_vertices):
                    if self.adj_matrix[y][x] == 1:
                        in_degree[x] += 1
        elif rep_type == '2':
            for i in self.adj_list:
                for j in self.adj_list[i]:
                    in_degree[j] += 1
        elif rep_type == '3':
            for i in self.edge_list:
                in_degree[i[1]] += 1
        queue = deque()
        for i in range(self.number_of_vertices):
            if in_degree[i] == 0:
                queue.append(i)
        top_order = []
        while queue:
            first = queue.popleft()
            top_order.append(first)
            if rep_type == '1':
                for i in range(self.number_of_vertices):
                    if self.adj_matrix[first][i] == 1:
                        in_degree[i] -= 1
                        if in_degree[i] == 0:
                            queue.append(i)
            elif rep_type == '2':
                for i in self.adj_list[first]:
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        queue.append(i)
            elif rep_type == '3':
                for i in self.edge_list:
                    if i[0] == first:
                        in_degree[i[1]] -= 1
                        if in_degree[i[1]] == 0:
                            queue.append(i[1])
        print("Graph topologically sorted via BFS: ")
        print(top_order)
