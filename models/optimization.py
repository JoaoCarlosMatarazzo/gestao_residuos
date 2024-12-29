import itertools
import numpy as np

def calculate_distance_matrix(bins, city_map):
    # Simula uma matriz de distâncias entre lixeiras
    num_bins = len(bins)
    distance_matrix = np.random.randint(1, 20, size=(num_bins, num_bins))
    return distance_matrix

def optimize_route(bins, city_map):
    distance_matrix = calculate_distance_matrix(bins, city_map)
    permutations = list(itertools.permutations(range(len(bins))))
    min_distance = float('inf')
    best_route = None
    for perm in permutations:
        distance = sum(distance_matrix[perm[i-1]][perm[i]] for i in range(len(perm)))
        if distance < min_distance:
            min_distance = distance
            best_route = perm
    return best_route, min_distance

if __name__ == "__main__":
    bins = [{"bin_id": 1}, {"bin_id": 2}, {"bin_id": 3}]
    city_map = "data/city_map.json"
    route, distance = optimize_route(bins, city_map)
    print(f"Melhor rota: {route}, Distância mínima: {distance}")
