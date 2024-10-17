import os
import networkx as nx
import heapq
import timeit


def read_pajek(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    in_vertices_section = False
    in_arcs_section = False

    vertices_data = []
    arcs_data = []

    for line in lines:
        if line.startswith('*vertices'):
            in_vertices_section = True
            continue
        elif line.startswith('*arcs'):
            in_vertices_section = False
            in_arcs_section = True
            continue

        if in_vertices_section:
            vertices_data.append(line.strip().split())
        elif in_arcs_section:
            arcs_data.append(line.strip().split())

    graph = nx.DiGraph()

    for parts in vertices_data:
        node_id = int(parts[0])
        node_label = parts[1]
        x = float(parts[2])
        y = float(parts[3])
        graph.add_node(node_id, label=node_label, x=x, y=y)

    for parts in arcs_data:
        source = int(parts[0])
        target = int(parts[1])
        weight = float(parts[2])
        graph.add_edge(source, target, weight=weight)

    return graph


def greedy_bfs(graph, start_node, goal_node):
    path = []
    visited = set()
    current_node = start_node

    while current_node != goal_node:
        neighbors = graph.neighbors(current_node)
        next_node = min(neighbors, key=lambda node: graph[current_node][node]['weight'])

        path.append((current_node, next_node))
        visited.add(current_node)
        current_node = next_node

        if current_node in visited:
            break

    return path

def astar_algorithm(graph, start_node, goal_node):
    def heuristic(node):
        return nx.shortest_path_length(graph, node, goal_node)

    priority_queue = [(0, start_node, [])]
    visited = set()

    while priority_queue:
        _, current_node, path = heapq.heappop(priority_queue)

        if current_node == goal_node:
            return path + [current_node]

        if current_node not in visited:
            visited.add(current_node)

            for neighbor in graph.neighbors(current_node):
                weight = graph[current_node][neighbor]['weight']
                heapq.heappush(priority_queue, (heuristic(neighbor) + weight, neighbor, path + [current_node]))

    return None


def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, "graph-airports-koord.net")
    graph = read_pajek(file_path)

    start_node = int(input("Unesite početni grad (indeks): "))
    goal_node = int(input("Unesite ciljni grad (indeks): "))

    start_time = timeit.default_timer()
    greedy_bfs_path = greedy_bfs(graph, start_node, goal_node)
    end_time = timeit.default_timer()
    print(f"Greedy BFS putanja: {greedy_bfs_path}")
    print(f"Greedy BFS vreme izvršavanja: {end_time - start_time} sekundi")

    start_time = timeit.default_timer()
    astar_path = astar_algorithm(graph, start_node, goal_node)
    end_time = timeit.default_timer()
    print(f"A* algoritam putanja: {astar_path}")
    print(f"A* algoritam vreme izvršavanja: {end_time - start_time} sekundi")

if __name__ == '__main__':
    main()
