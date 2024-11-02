from queue import PriorityQueue

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    queue = PriorityQueue()
    queue.put((heuristic[start], start))
    parent = {start: None}

    while not queue.empty():
        _, current_node = queue.get()
        
        if current_node == goal:
            return reconstruct_path(parent, goal)

        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.put((heuristic[neighbor], neighbor))
                parent[neighbor] = current_node

    return None

def reconstruct_path(parent, goal):
    path = []
    while goal:
        path.append(goal)
        goal = parent[goal]
    return path[::-1]

# Example usage:
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_node = 'A'
    goal_node = 'F'

    # Example heuristic function (Euclidean distance to the goal)
    heuristic = {'A': 5, 'B': 3, 'C': 2, 'D': 4, 'E': 1, 'F': 0}

    shortest_path = best_first_search(graph, start_node, goal_node, heuristic)

    if shortest_path:
        print(f"Shortest path from {start_node} to {goal_node}: {shortest_path}")
    else:
        print(f"No path found from {start_node} to {goal_node}.")
