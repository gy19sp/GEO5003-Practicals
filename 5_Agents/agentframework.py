import random
""" A new file. Very basic at this stage the first part establishes the initial position
the move part established how the agents move after words. later the agents will perform 
a set amount of iterations"""

#creates the Agent class
class Agent():
    
#make and define new agent's location
    def __init__(self):
        self._x = random.randint(0,99)        
        self._y = random.randint(0,99)


#movement has been transferred to this file
    def move(self):
        
        if random.random() < 0.5:
            self._y = self._y + 1 % 100
        else:
            self._y = self._y - 1 % 100

        if random.random() < 0.5:
            self._x = self._x + 1 % 100
        else:
            self._x = self._x - 1 % 100
        
        
    