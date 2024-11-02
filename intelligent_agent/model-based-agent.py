internal_state = {}

def model_based_agent(percept):
    location = percept['location']
    status = percept['status']

    internal_state['location'] = status

def rule_based_action():

    for location, status in internal_state.items():
        if status == 'dirty':
            return f"Clean {location}"
        
        return f"Move to {location}"
    

def act(percept):
    model_based_agent(percept)
    return rule_based_action()

if __name__ == "__main__":
    percepts = [
        {'location': 'A', 'status': 'dirty'},
        {'location': 'B', 'status': 'clean'},
        {'location': 'C', 'status': 'dirty'},
    ]

    for percept in percepts:
        action = act(percept)
        print(f"Percept: {percept}, Action: {action}")