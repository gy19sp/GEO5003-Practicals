import random
""" Another dimension is being added to the model, that is: interaction with other agents to avoid overlapping. This mimics normal 
behaviour of sheep that would normally not encroach on each other. The previou distance calculation is being used for this reason
while a new function on how agents interact with each other has been created"""

class Agent():
    
#puts and defines new agent's location within the environment and gives access to the agent
    def __init__(self, environment, agentlist):
        self._y = (random.randint(0,99))
        self._x = (random.randint(0,99))
        self.environment = environment
        self.agentlist= agentlist
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
           
#calculate the distance between agents so that agents do not overlap
    def distance_between(self, agents): #transferred from model
        dist= (((self._x - agents._x)**2) + ((self._y - agents._y)**2))**0.5 
        #print (dist)    #test to ,easure distances between agents
        return dist 
        
#avoids overlapping     
    def share_with_neighbours(self, neighbourhood):# definition
        for i in self.agentlist:# Loop through the agents in self.agents .
            distance = self.distance_between(i) # Calculate the distance between self and the current other agent:
            if distance <= neighbourhood:# If distance is less than or equal to the neighbourhood
                sum = self.store + i.store #combined storage
                ave = sum /2 #divide between agents
                self.store = ave #agents share
                i.store = ave

