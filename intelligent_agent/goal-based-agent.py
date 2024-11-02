goal_position = (6,5)

internal_state = {
    'location': (0,0)
}

def update_state ( action ):
    x, y = internal_state['location']
    if action == 'Move Right':
        x += 1
    elif action == 'Move Left':
        x -= 1
    elif action == 'Move Up':
        y += 1
    elif action == 'Move Down':
        y -= 1

    internal_state['location'] = (x, y)

def goal_achieved():
    return internal_state['location'] == goal_position

def decide_action():

    if goal_achieved():
        return 'Goal Achieved'
    
    x, y = internal_state['location']
    goal_x, goal_y = goal_position

    if x < goal_x:
        return 'Move Right'
    elif x > goal_x:
        return 'Move Left'
    elif y < goal_y:
        return 'Move Up'
    elif y > goal_y:
        return 'Move Down'
    
def act():
    action = decide_action()

    if action != 'Goal Achieved':
        update_state(action)

    return action

if __name__ == "__main__":
    print(f"Starting location: {internal_state['location']}")
    while True:
        action = act()
        print(f"Action: {action}, New Location: {internal_state['location']}")
        if action == 'Goal Achieved':
            break
