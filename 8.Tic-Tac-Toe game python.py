from collections import deque
def bfs(graph, start):
    queue = deque([start])
    visited = set()
    visited.add(start)
    traversal_order = []
    while queue:
        node = queue.popleft()
        traversal_order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return traversal_order
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    start_node = 'A'
    print("BFS Traversal Order:", bfs(graph, start_node))
