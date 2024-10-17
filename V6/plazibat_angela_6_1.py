from itertools import permutations
import timeit
import time

def read_city_names(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        city_names = lines[0].strip().split(',')[1:]
    return city_names

def read_distance_matrix(file_path):
    distances = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        data_start = lines.index('*data\n') + 1 if '*data\n' in lines else 1

        for line in lines[data_start:]:
            row = line.strip().split(',')[1:]  
            distances.append([int(cell) if cell != '-' else float('inf') for cell in row])

    return distances


def calculate_tour_length(tour, distance_matrix):
    length = 0
    for i in range(len(tour) - 1):
        length += distance_matrix[tour[i]][tour[i + 1]]
    length += distance_matrix[tour[-1]][tour[0]]  
    return length

def brute_force(distance_matrix, num_cities):
    cities = list(range(num_cities))

    min_tour = None
    min_length = float('inf')

    start_time = timeit.default_timer()
    for tour_indices in permutations(cities):
        tour = list(tour_indices)
        length = calculate_tour_length(tour, distance_matrix)
        if length < min_length:
            min_length = length
            min_tour = tour

    end_time = timeit.default_timer()
    execution_time = end_time - start_time 

    return min_tour, min_length, execution_time



def nearest_neighbor(distance_matrix, num_cities):
    unvisited_cities = list(range(1, num_cities)) 
    current_city = 0
    tour = [current_city]
    length = 0

    def evaluate_tour():
        nonlocal current_city, tour, length
        while unvisited_cities:
            distances_to_visited = [0 if city in tour else distance_matrix[current_city][city] for city in range(num_cities)]
            nearest_city = min((city for city in unvisited_cities), key=lambda city: distances_to_visited[city])
            length += distance_matrix[current_city][nearest_city]
            current_city = nearest_city
            tour.append(current_city)
            unvisited_cities.remove(current_city)

        length += distance_matrix[current_city][tour[0]]  

    start_time = timeit.default_timer()
    timeit.timeit(evaluate_tour, number=1)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time

    return tour, length, execution_time

def sorted_neighbors(distance_matrix, num_cities):
    unvisited_cities = list(range(1, num_cities))
    current_city = 0
    tour = [current_city]
    length = 0

    def evaluate_tour():
        nonlocal current_city, tour, length
        while len(tour) < num_cities:
            sorted_edges = [(current_city, city, distance_matrix[current_city][city]) for city in unvisited_cities]
            sorted_edges.sort(key=lambda x: x[2])

            nearest_edge = sorted_edges[0]
            nearest_city = nearest_edge[1]
            length += nearest_edge[2]
            current_city = nearest_city
            tour.append(current_city)
            unvisited_cities.remove(current_city)

        length += distance_matrix[current_city][tour[0]]

    start_time = timeit.default_timer()
    timeit.timeit(evaluate_tour, number=1)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time

    return tour, length, execution_time

def main():
    file_path = 'distance.csv'
    num_cities = 10

    city_names = read_city_names(file_path)
    distance_matrix = read_distance_matrix(file_path)

    brute_force_result, min_length, execution_time_bf = brute_force(distance_matrix, num_cities)
    city_names_result = [city_names[i] for i in brute_force_result]
    print(f"Brute Force Result - Tour: {', '.join(city_names_result)}, Length: {min_length}")
    print(f"Brute Force Time: {execution_time_bf} seconds")

    nearest_neighbor_result, nn_length, execution_time_nn = nearest_neighbor(distance_matrix, num_cities)
    city_names_result = [city_names[i] for i in nearest_neighbor_result]
    print(f"Nearest Neighbor Result - Tour: {', '.join(city_names_result)}, Length: {nn_length}")
    print(f"Nearest Neighbor Time: {execution_time_nn} seconds")

    sorted_neighbors_result, sn_length, execution_time_sn = sorted_neighbors(distance_matrix, num_cities)
    city_names_result = [city_names[i] for i in sorted_neighbors_result]
    print(f"Sorted Neighbors Result - Tour: {', '.join(city_names_result)}, Length: {sn_length}")
    print(f"Sorted Neighbors Time: {execution_time_sn} seconds")

if __name__ == '__main__':
    main()
