class Graph:
    def __init__(self):
        self.vertices = set()
        self.vertex_names = {}
        self.graph = []
    
    def add_edge(self, src, dest, weight):
        self.vertices.add(src)
        self.vertices.add(dest)
        self.graph.append((src, dest, weight))

    def prim_mst(self):
        parent = [-1] * len(self.vertices)
        key = [float('inf')] * len(self.vertices)
        mst_set = [False] * len(self.vertices)

        key[0] = 0

        for _ in range(len(self.vertices)):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v, w in self.get_neighbors(u):
                if not mst_set[v] and w < key[v]:
                    key[v] = w
                    parent[v] = u

        self.print_mst(parent)

    def min_key(self, key, mst_set):
        min_val = float('inf')
        min_index = -1

        for v in range(len(self.vertices)):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v

        return min_index

    def print_mst(self, parent):
        print("\nPrimov algoritam - Minimalno razapinjuce stablo:")
        total_weight = 0
        for i in range(1, len(self.vertices)):
            weight = self.get_weight(parent[i], i)
            print(f"Grana {self.get_vertex_name(parent[i])} - {self.get_vertex_name(i)}, Tezina: {weight}")
            total_weight += weight
        print(f"Ukupna tezina: {total_weight}")

    def get_weight(self, src, dest):
        for edge in self.graph:
            if edge[0] == src and edge[1] == dest:
                return edge[2]
            elif edge[1] == src and edge[0] == dest:
                return edge[2]
        return 0

    def kruskal_mst(self):
        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(len(self.vertices)):
            parent.append(node)
            rank.append(0)

        while e < len(self.vertices) - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        self.print_kruskal_mst(result)

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def print_kruskal_mst(self, result):
        print("\nKruskalov algoritam - Minimalno razapinjuce stablo:")
        total_weight = 0
        for u, v, weight in result:
            print(f"Grana {self.get_vertex_name(u)} - {self.get_vertex_name(v)}, Tezina: {weight}")
            total_weight += weight
        print(f"Ukupna tezina: {total_weight}")

    def get_neighbors(self, u):
        return [(v, w) for (x, v, w) in self.graph if x == u] + [(u, v, w) for (u, v, w) in self.graph if v == u]

    def get_vertex_name(self, vertex):
        return self.vertex_names.get(vertex, str(vertex))


def read_pajek_file(file_path):
    graph = Graph()
    with open(file_path, 'r') as file:
        lines = file.readlines()

        is_vertices = False
        for line in lines:
            if line.startswith('*vertices'):
                is_vertices = True
                continue

            if is_vertices and line.strip():
                parts = line.split()
                if len(parts) >= 2:
                    vertex_index = int(parts[0])
                    vertex_name = parts[1]
                    graph.vertices.add(vertex_index)
                    graph.vertex_names[vertex_index] = vertex_name
                else:
                    break

    with open(file_path, 'r') as file:
        lines = file.readlines()

        is_arcs = False
        for line in lines:
            if line.startswith('*arcs'):
                is_arcs = True
                continue

            if is_arcs and line.strip():
                parts = line.split()
                if len(parts) == 3:
                    src = int(parts[0])
                    dest = int(parts[1])
                    weight = int(parts[2])
                    graph.add_edge(src, dest, weight)

    return graph

def main():
    file_path = 'airports-split.net'
    graph = read_pajek_file(file_path)

    graph.prim_mst()
    graph.kruskal_mst()

if __name__ == '__main__' :
    main ()