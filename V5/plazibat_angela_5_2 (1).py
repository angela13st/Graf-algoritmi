class Graph:
    def __init__(self):
        self.vertices = set()
        self.graph = []

    def add_edge(self, src, dest):
        self.vertices.add(src)
        self.vertices.add(dest)
        self.graph.append((src, dest))

    def degree_of_nodes(self):
        degrees = {}

        for edge in self.graph:
            src, dest = edge

            if src in degrees:
                degrees[src] += 1
            else:
                degrees[src] = 1

            if dest in degrees:
                degrees[dest] += 1
            else:
                degrees[dest] = 1

        return degrees

    def get_neighbors(self, node):
        return [v for u, v in self.graph if u == node] + [u for u, v in self.graph if v == node]

    def calculate_components(self):
        visited = set()
        components = []
        max_component_size = 0

        def dfs(node, component):
            nonlocal max_component_size
            visited.add(node)
            component.append(node)

            for neighbor in self.get_neighbors(node):
                if neighbor not in visited:
                    dfs(neighbor, component)

            max_component_size = max(max_component_size, len(component))

        for vertex in self.vertices:
            if vertex not in visited:
                component = []
                dfs(vertex, component)
                components.append(component)

        return len(components), max_component_size

    def print_components_info(self):
        num_components, max_component_size = self.calculate_components()
        print(f"Broj komponenti u grafu: {num_components}")
        print(f"Veličina najveće komponente: {max_component_size}")

    def read_pajek_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

            is_arcs = False
            for line in lines:
                if line.startswith('*arcs'):
                    is_arcs = True
                    continue

                if is_arcs:
                    parts = line.split()
                    if len(parts) == 2:
                        src = int(parts[0])
                        dest = int(parts[1])
                        self.add_edge(src, dest)

    def get_vertex_name(self, vertex):
        return list(self.vertices)[vertex]

    def print_top_companies(self, num_companies):
        degrees = self.degree_of_nodes()
        sorted_degrees = sorted(degrees.items(), key=lambda x: x[1], reverse=True)

        print(f"Prvih {num_companies} kompanija i broj kompanija koje posjeduju:")
        for i in range(min(num_companies, len(sorted_degrees))):
            company, degree = sorted_degrees[i]
            print(f"Kompanija: {self.get_vertex_name(company)}, Broj kompanija koje posjeduju: {degree}")

def main():
    file_path_eva = 'eva.net' 
    graph_eva = Graph()
    graph_eva.read_pajek_file(file_path_eva)

    graph_eva.print_components_info()

    graph_eva.print_top_companies(10)

if __name__ == '__main__' :
    main ()