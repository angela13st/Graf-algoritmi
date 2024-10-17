import time
import timeit
import networkx as nx
import heapq
import os

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


def dijkstra_algorithm(graph, start_node):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start_node] = 0

    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = min(priority_queue)
        priority_queue.remove((current_distance, current_node))
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = distances[current_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                priority_queue.append((distance, neighbor))
    return distances


def bellman_ford_algorithm(graph, start_node):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start_node] = 0

    for _ in range(len(graph) - 1):
        for u, v, weight in graph.edges.data('weight', default=1):
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    return distances

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, "graph-airports-koord.net")

    graph = read_pajek(file_path)

    start_node = int(input("Unesite početni grad (indeks): "))

    start_time = timeit.default_timer()
    dijkstra_distances = dijkstra_algorithm(graph, start_node)
    end_time = timeit.default_timer()
    print(f"Dijkstra najkraći putevi: {dijkstra_distances}")
    print(f"Dijkstra vreme izvršavanja: {end_time - start_time} sekundi")

    start_time = timeit.default_timer()
    bellman_ford_distances = bellman_ford_algorithm(graph, start_node)
    end_time = timeit.default_timer()
    print(f"Bellman-Ford najkraći putevi: {bellman_ford_distances}")
    print(f"Bellman-Ford vreme izvršavanja: {end_time - start_time} sekundi")

if __name__ == '__main__':
    main()
