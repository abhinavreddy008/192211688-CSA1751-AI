def is_valid(graph, colors, node, color):
    return all(colors.get(nei) != color for nei in graph[node])
def map_coloring(graph, colors, nodes, index, color_list):
    if index == len(nodes):
        return True
    node = nodes[index]
    for color in color_list:
        if is_valid(graph, colors, node, color):
            colors[node] = color
            if map_coloring(graph, colors, nodes, index + 1, color_list):
                return True
            colors[node] = None
    return False
def solve_map_coloring(graph, color_list):
    colors = {node: None for node in graph}
    nodes = list(graph.keys())
    if map_coloring(graph, colors, nodes, 0, color_list):
        return colors
    return None
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'C', 'E'],
        'C': ['A', 'B', 'F'],
        'D': ['A', 'E'],
        'E': ['B', 'D', 'F'],
        'F': ['C', 'E']
    }
    color_list = ['Red', 'Green', 'Blue']
    solution = solve_map_coloring(graph, color_list)
    print("Map Coloring Solution:", solution)
