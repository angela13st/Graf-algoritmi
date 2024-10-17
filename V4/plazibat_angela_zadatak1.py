def read_pajek_file(file_path):
    adjacency_list = {}
    
    with open(file_path, 'r') as file:
        lines = file.readlines()

        reading_edges = False
        for line in lines:
            if line.startswith('*'):
                if "*Edges" in line or "*Arcs" in line:
                    reading_edges = True
                continue

            if not reading_edges:
                continue

            parts = line.split()
            if len(parts) == 2:
                start_vertex = int(parts[0])
                end_vertex = int(parts[1])

                if start_vertex not in adjacency_list:
                    adjacency_list[start_vertex] = []
                if end_vertex not in adjacency_list:
                    adjacency_list[end_vertex] = []

                adjacency_list[start_vertex].append(end_vertex)
                adjacency_list[end_vertex].append(start_vertex)

    return adjacency_list

def adjacency_list_to_adjacency_matrix(adjacency_list):
    num_vertices = max(adjacency_list.keys())
    adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    for vertex, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            adjacency_matrix[vertex - 1][neighbor - 1] = 1
            adjacency_matrix[neighbor - 1][vertex - 1] = 1  

    return adjacency_matrix


def adjacency_list_to_incidence_matrix(adjacency_list):
    num_vertices = max(adjacency_list.keys())
    num_edges = sum(len(neighbors) for neighbors in adjacency_list.values()) // 2
    incidence_matrix = [[0] * num_edges for _ in range(num_vertices)]

    edge_index = 0
    for vertex, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            if vertex < neighbor:  
                incidence_matrix[vertex - 1][edge_index] = 1
                incidence_matrix[neighbor - 1][edge_index] = 1
                edge_index += 1

    return incidence_matrix

def adjacency_matrix_to_adjacency_list(adjacency_matrix):
    num_vertices = len(adjacency_matrix)
    adjacency_list = {}

    for i in range(num_vertices):
        neighbors = [j + 1 for j in range(num_vertices) if adjacency_matrix[i][j] == 1]
        adjacency_list[i + 1] = neighbors

    return adjacency_list

def adjacency_matrix_to_incidence_matrix(adjacency_matrix):
    num_vertices = len(adjacency_matrix)
    num_edges = sum(sum(row) for row in adjacency_matrix) // 2
    incidence_matrix = [[0] * num_edges for _ in range(num_vertices)]

    edge_index = 0
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if adjacency_matrix[i][j] == 1:
                incidence_matrix[i][edge_index] = 1
                incidence_matrix[j][edge_index] = 1
                edge_index += 1

    return incidence_matrix

def incidence_matrix_to_adjacency_list(incidence_matrix):
    num_vertices = len(incidence_matrix)
    adjacency_list = {}

    for i in range(num_vertices):
        neighbors = [j + 1 for j in range(len(incidence_matrix[i])) if incidence_matrix[i][j] == 1]
        adjacency_list[i + 1] = neighbors

    return adjacency_list

def incidence_matrix_to_adjacency_matrix(incidence_matrix):
    num_vertices = len(incidence_matrix)
    num_edges = len(incidence_matrix[0])
    adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    for j in range(num_edges):
        connected_vertices = [i for i in range(num_vertices) if incidence_matrix[i][j] == 1]
        if len(connected_vertices) == 2:  
            adjacency_matrix[connected_vertices[0]][connected_vertices[1]] = 1
            adjacency_matrix[connected_vertices[1]][connected_vertices[0]] = 1

    return adjacency_matrix


if __name__ == "__main__":
    file_path = 'euler.net'
    adjacency_list = read_pajek_file(file_path)
    
    
    print("Pocetna lista susjedstava:")
    for vertex, neighbors in adjacency_list.items():
        print(f"{vertex}: {neighbors}")
    
    
    adjacency_matrix = adjacency_list_to_adjacency_matrix(adjacency_list)
    print("\nLista susjedstva u matricu susjedstva:")
    for row in adjacency_matrix:
        print(row)
    
    
    incidence_matrix = adjacency_list_to_incidence_matrix(adjacency_list)
    print("\nLista susjedstva u matricu incidencije:")
    for row in incidence_matrix:
        print(row)
    
    adjacency_list1 = adjacency_matrix_to_adjacency_list(adjacency_matrix)
    print("\nMatrica susjedstva u listu susjedstva:")
    for vertex, neighbors in adjacency_list1.items():
        print(f"{vertex}: {neighbors}")
    
    incidence_matrix_from_adjacency = adjacency_matrix_to_incidence_matrix(adjacency_matrix)
    print("\nMatrica susjedstva u matricu incidencije:")
    for row in incidence_matrix_from_adjacency:
        print(row)
    
    
    adjacency_list_back = incidence_matrix_to_adjacency_list(incidence_matrix)
    print("\nMatrica incidencije u listu susjedstva:")
    for vertex, neighbors in adjacency_list_back.items():
        print(f"{vertex}: {neighbors}")
    
    adjacency_matrix1 = incidence_matrix_to_adjacency_matrix(incidence_matrix)
    print("\nMatrica incidencije u matricu susjedstva:")
    for row in adjacency_matrix1:
        print(row)
    
