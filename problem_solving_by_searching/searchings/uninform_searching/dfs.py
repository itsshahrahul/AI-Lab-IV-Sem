class Graph:
    def __init__(self):
        self.graph = {}
    
    # Add an edge from vertex u to vertex v
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
    
    # Perform DFS starting from a given vertex
    def dfs(self, start):
        visited = set()  # Set to keep track of visited nodes
        stack = [start]  # Initialize a stack with the starting node
        
        while stack:
            node = stack.pop()  # Pop the top node from the stack
            
            if node not in visited:
                print(node, end=" ")  # Process the node (e.g., print it)
                visited.add(node)  # Mark the node as visited
                
                # Add all unvisited neighbors to the stack
                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited:
                        stack.append(neighbor)

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    print("DFS traversal starting from vertex 2:")
    g.dfs(2)
