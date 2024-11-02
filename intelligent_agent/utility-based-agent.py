goal_position = (4, 4)
obstacles = [(2,0 ), (3, 3)]

current_position = (0, 0)

def calculate_utility(position):
    x, y = position
    goal_x, goal_y = goal_position
    distance_to_goal = abs(x - goal_x) + abs(y - goal_y)


    if position in obstacles:
        return -float('inf')
    
    
    return -distance_to_goal

def get_possible_actions():
    """
    Generates possible actions and resulting positions from the current position.
    :return: A list of (action, resulting_position) tuples.
    """
    x, y = current_position
    possible_actions = []


    if x < 4:  
        possible_actions.append(('Move Right', (x + 1, y)))
    if x > 0: 
        possible_actions.append(('Move Left', (x - 1, y)))
    if y < 4: 
        possible_actions.append(('Move Up', (x, y + 1)))
    if y > 0:  
        possible_actions.append(('Move Down', (x, y - 1)))

    return possible_actions

def decide_action():
    possible_actions = get_possible_actions()
    best_action = None
    best_utility = -float('inf')

    for action, new_position in possible_actions:
        utility = calculate_utility(new_position)
        
        if utility > best_utility:
            best_utility = utility
            best_action = action

    return best_action

def update_position(action):
    """
    Updates the current position based on the given action.
    :param action: The action taken by the agent.
    :return: New updated position.
    """
    x, y = current_position

    if action == 'Move Right':
        x += 1
    elif action == 'Move Left':
        x -= 1
    elif action == 'Move Up':
        y += 1
    elif action == 'Move Down':
        y -= 1

    return (x, y)

if __name__ == "__main__":
    print(f"Starting location: {current_position}")
    while True:
        action = decide_action()
        print(f"Action: {action}, Current Position: {current_position}")
        
        current_position = update_position(action)
        
        if current_position == goal_position:
            print(f"Goal reached at {current_position}")
            break
