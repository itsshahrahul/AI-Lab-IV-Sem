class simple_reflex_agent:
    def __init__(self):
        self.action = None

    def perceive(self,percept):
        if percept == 'obstacle':
            self.action = 'turn'
        else:
            self.action = 'move'

    def act(self):
        return self.action
    

agent = simple_reflex_agent()
percept = ['obstacle','clear','obstacle','clear','clear','clear','clear','clear','clear','clear']

for p in percept:
    agent.perceive(p)
    action = agent.act()
    print('Percept:',p,'Action:',action)    