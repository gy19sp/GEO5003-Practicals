import random
"""slight alterations gave been made to the agent frmework, with the inclusion of an eat function.
The environment data has been linked to an "in" text file containing the environmental data. 
This allows the agents (sheep) to eat from the environment and store the food"""

class Agent():
    
#puts and defines new agent's location within the environment and make agents change it
    def __init__(self, environment):
        self._y = (random.randint(0,99))
        self._x = (random.randint(0,99))
        self.environment = environment
        self.store = 0 

#makes the agents move from the original location
    def move(self):
        
        if random.random() < 0.5:
            self._y = self._y + 1 % 100
        else:
            self._y = self._y - 1 % 100

        if random.random() < 0.5:
            self._x = self._x + 1 % 100
        else:
            self._x = self._x - 1 % 100

# makes agent eat the environment (grass)
    def eat(self): 
        if self.environment[self._y][self._x] > 10 and self.store >= 100:
           self.environment[self._y][self._x] -= 10
           self.store += 10 

        