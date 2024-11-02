import heapq

# Node structure
class Node:
    def __init__(self, x, y, g, h):
        self.x = x
        self.y = y
        self.g = g  # Cost from start node
        self.h = h  # Heuristic (Manhattan distance to goal)

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

# Heuristic function: Manhattan distance
def heuristic(current, goal):
    return abs(current.x - goal.x) + abs(current.y - goal.y)

# A* search algorithm
def a_star_search(start, goal, grid):
    pq = []
    heapq.heappush(pq, start)

    while pq:
        current = heapq.heappop(pq)

        print(f"Visiting node at ({current.x}, {current.y})")

        if current.x == goal.x and current.y == goal.y:
            print("Goal reached!")
            return

        # Explore neighbors
        neighbors = [
            Node(current.x - 1, current.y, current.g + 1, 0),
            Node(current.x + 1, current.y, current.g + 1, 0),
            Node(current.x, current.y - 1, current.g + 1, 0),
            Node(current.x, current.y + 1, current.g + 1, 0)
        ]

        for neighbor in neighbors:
            if 0 <= neighbor.x < len(grid) and 0 <= neighbor.y < len(grid[0]) and grid[neighbor.x][neighbor.y] == 0:
                neighbor.h = heuristic(neighbor, goal)
                heapq.heappush(pq, neighbor)

# Example usage
if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    start = Node(0, 0, 0, 0)  # Start point (x, y)
    goal = Node(4, 4, 0, 0)   # Goal point (x, y)

    # Initialize heuristic for the start node
    start.h = heuristic(start, goal)

    a_star_search(start, goal, grid)
