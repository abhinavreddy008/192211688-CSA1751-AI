from itertools import permutations

def calculate_route_cost(graph, route):
    return sum(graph[route[i]][route[i+1]] for i in range(len(route)-1)) + graph[route[-1]][route[0]]

def tsp(graph):
    nodes = list(graph.keys())
    all_routes = permutations(nodes)
    
    min_cost = float('inf')
    best_route = None
    
    for route in all_routes:
        cost = calculate_route_cost(graph, route)
        if cost < min_cost:
            min_cost = cost
            best_route = route
    
    return best_route, min_cost
if __name__ == "__main__":
    graph = {
        'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
        'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
        'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
        'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
    }
    
    best_route, min_cost = tsp(graph)
    print(f"Best route: {best_route}, Minimum cost: {min_cost}")
