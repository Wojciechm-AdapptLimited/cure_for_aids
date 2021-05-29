from collections import defaultdict
import random


class Graph:
    def __init__(self, number_of_vertices, saturation_value):
        self.number_of_vertices = number_of_vertices
        self.saturation = saturation_value * 0.5 * self.number_of_vertices * (self.number_of_vertices - 1)
        self.vertices_list = random.sample(list(range(self.number_of_vertices)), self.number_of_vertices)
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def remove_edge(self, u, v):
        for index, key in enumerate(self.graph[u]):
            if key == v:
                self.graph[u].pop(index)
        for index, key in enumerate(self.graph[v]):
            if key == u:
                self.graph[v].pop(index)

    def gen_hamiltonian(self):
        edges = self.number_of_vertices
        self.add_edge(self.vertices_list[0], self.vertices_list[-1])
        for i in range(self.number_of_vertices - 1):
            self.add_edge(self.vertices_list[i], self.vertices_list[i + 1])
        while edges < self.saturation:
            while True:
                first = random.randint(0, self.number_of_vertices - 1)
                second = random.randint(0, self.number_of_vertices - 1)
                third = random.randint(0, self.number_of_vertices - 1)
                if first != second and first != third and second != third and first not in self.graph[second]\
                        and first not in self.graph[third] and second not in self.graph[third]:
                    break
            self.add_edge(first, second)
            self.add_edge(first, third)
            self.add_edge(second, third)
            edges += 3

    def gen_not_hamiltonian(self):
        rand_vertex = random.randint(0, self.number_of_vertices - 1)
        while len(self.graph[rand_vertex]) > 0:
            self.remove_edge(rand_vertex, self.graph[rand_vertex][0])

    def input_graph(self, edges):
        for i in range(edges):
            edge = None
            while True:
                try:
                    edge = list(map(int, input("Enter edge: ".split())))
                except ValueError:
                    continue
                else:
                    if len(edge) != 2:
                        continue
                    else:
                        break
            if edge:
                self.add_edge(edge[0], edge[1])

    def print_graph(self):
        print("Adjacency list of the graph: ")
        for key in self.graph:
            print(key, end=' -> | ')
            for item in self.graph[key]:
                print("{} | ".format(item), end="")
            print()

    def dfs_count(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                count += self.dfs_count(i, visited)
        return count

    def is_valid_next_edge(self, u, v):
        if len(self.graph[u]) == 1:
            return True
        visited = [False] * self.number_of_vertices
        count_1 = self.dfs_count(u, visited)
        self.remove_edge(u, v)
        visited = [False] * self.number_of_vertices
        count_2 = self.dfs_count(u, visited)
        self.add_edge(u, v)
        return False if count_1 > count_2 else True

    def print_euler_util(self, u):
        for v in self.graph[u]:
            if self.is_valid_next_edge(u, v):
                print("{} - {}".format(u, v), end='\t'),
                self.remove_edge(u, v)
                self.print_euler_util(v)

    def print_euler_tour(self):
        u = 0
        for i in range(self.number_of_vertices):
            if len(self.graph[i]) % 2 != 0:
                u = i
                break
        print("\nEuler path:")
        self.print_euler_util(u)
        print("\n")

    def print_hamiltonian_cycle(self):
        if len(self.graph[0])<1:
            path = [self.graph[1][0]]
        else:
            path = [self.graph[0][0]]
        node = len(path)
        depth = {key: 0 for key in range(self.number_of_vertices)}

        while node:
            vertex = path[-1]
            next_node = None

            if depth[vertex] < len(self.graph[vertex]):
                next_node = self.graph[list(depth.keys()).index(vertex)][depth[vertex]]

            if next_node is not None and next_node not in path:
                print("Path (0):\t", path)
                path.append(next_node)
                depth[vertex] = depth[vertex] + 1
                node = node + 1
                continue

            elif next_node in path:
                depth[vertex] = depth[vertex] + 1
                continue

            else:
                if len(path) == self.number_of_vertices:
                    print("Path (1):\t", path, "(max length)")
                    if path[0] in self.graph[path[-1]]:
                        path.append(path[0])
                        print("This is Hamilton Cycle:\t", path)
                        break
                else:
                    print("Path (2):\t", path)
                path.pop(-1)
                depth[vertex] = 0
                node = node - 1
