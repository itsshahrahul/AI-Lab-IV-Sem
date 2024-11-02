from collections import deque

def bfs(graph, start):
    # Initialize a queue with the start node
    queue = deque([start])
    
    # Keep track of visited nodes
    visited = set([start])
    
    while queue:
        # Pop the first node from the queue
        node = queue.popleft()
        print(node, end=" ")

        # Visit all the neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Perform BFS starting from node 'A'
bfs(graph, 'C')
