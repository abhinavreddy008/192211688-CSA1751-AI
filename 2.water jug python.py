from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    queue, visited = deque([(0, 0)]), set((0, 0))

    while queue:
        jug1, jug2 = queue.popleft()

        if jug1 == target or jug2 == target:
            return f"Solution found: ({jug1}, {jug2})"

        moves = [
            (jug1_capacity, jug2), (jug1, jug2_capacity),(0, jug2), (jug1, 0),  
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),  
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1))   
        ]

        for state in moves:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    return "No solution found."
print(water_jug_bfs(4, 3, 2))
