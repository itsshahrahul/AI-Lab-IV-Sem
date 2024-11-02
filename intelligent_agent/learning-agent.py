import random

# Define the grid size and goal
grid_size = 10
goal_position = (6, 5)
obstacles = [(2, 2), (3, 3)]

# Learning parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate

# Initialize the Q-value table
q_table = {}

actions = ['Move Right', 'Move Left', 'Move Up', 'Move Down']

def get_possible_actions(position):
    x, y = position
    possible_actions = []

    if x < grid_size - 1:
        possible_actions.append(('Move Right', (x + 1, y)))
    if x > 0:
        possible_actions.append(('Move Left', (x - 1, y)))
    if y < grid_size - 1:
        possible_actions.append(('Move Up', (x, y + 1)))
    if y > 0:
        possible_actions.append(('Move Down', (x, y - 1)))

    return possible_actions

def get_reward(position):
    if position == goal_position:
        return 100  
    elif position in obstacles:
        return -100  
    else:
        return -1  

def choose_action(position):
    if random.uniform(0, 1) < epsilon:
        action, _ = random.choice(get_possible_actions(position))
    else:
        q_values = q_table.get(position, {})
        if q_values:
            action = max(q_values, key=q_values.get)
        else:
            action, _ = random.choice(get_possible_actions(position))
    return action

def update_q_table(state, action, reward, next_state):
    q_values = q_table.get(state, {})
    current_q_value = q_values.get(action, 0)

    next_q_values = q_table.get(next_state, {})
    max_future_q = max(next_q_values.values(), default=0)

    new_q_value = current_q_value + alpha * (reward + gamma * max_future_q - current_q_value)
    q_values[action] = new_q_value

    q_table[state] = q_values

def get_new_position(action, position):
    x, y = position

    if action == 'Move Right':
        return (x + 1, y)
    elif action == 'Move Left':
        return (x - 1, y)
    elif action == 'Move Up':
        return (x, y + 1)
    elif action == 'Move Down':
        return (x, y - 1)
    
    return position

# Training the agent
for episode in range(1000):
    current_position = (0, 0)
    while current_position != goal_position:
        # Choose an action using epsilon-greedy policy
        action = choose_action(current_position)
        
        # Determine the next position based on the chosen action
        next_position = get_new_position(action, current_position)
        
        # Get the reward for the new position
        reward = get_reward(next_position)
        
        # Update the Q-table with the new experience
        update_q_table(current_position, action, reward, next_position)
        
        # Move to the next position
        current_position = next_position

# Testing the agent after training
current_position = (0, 0)
print(f"Starting location: {current_position}")

while current_position != goal_position:
    action = choose_action(current_position)
    print(f"Action: {action}, Current Position: {current_position}")

    current_position = get_new_position(action, current_position)
    if current_position == goal_position:
        print(f"Goal reached at {current_position}")
        break
