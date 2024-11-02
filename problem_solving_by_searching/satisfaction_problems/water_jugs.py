from collections import deque

class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __lt__(self, other):
        return (self.jug1, self.jug2) < (other.jug1, other.jug2)

    def __eq__(self, other):
        return (self.jug1, self.jug2) == (other.jug1, other.jug2)

    def __hash__(self):
        return hash((self.jug1, self.jug2))

def water_jug_bfs(capacity1, capacity2, goal):
    q = deque()
    visited = set()

    # Initial state with both jugs empty
    q.append(State(0, 0))
    visited.add(State(0, 0))

    while q:
        current = q.popleft()
        jug1 = current.jug1
        jug2 = current.jug2

        # Print the current state of the jugs
        print(f"Jug 1: {jug1}, Jug 2: {jug2}")

        # Check if we've reached the goal
        if jug1 == goal or jug2 == goal:
            print("Found solution!")
            return

        # Generate all possible next states
        next_states = [
            State(capacity1, jug2),  # Fill jug1
            State(jug1, capacity2),  # Fill jug2
            State(0, jug2),          # Empty jug1
            State(jug1, 0),          # Empty jug2
            State(min(jug1 + jug2, capacity1), max(0, jug1 + jug2 - capacity1)),  # Pour jug2 -> jug1
            State(max(0, jug1 + jug2 - capacity2), min(jug1 + jug2, capacity2))   # Pour jug1 -> jug2
        ]

        for next_state in next_states:
            if next_state not in visited:
                visited.add(next_state)
                q.append(next_state)

    print("No solution found.")

# Driver code
jug1_capacity = 4
jug2_capacity = 3
goal = 2

water_jug_bfs(jug1_capacity, jug2_capacity, goal)
