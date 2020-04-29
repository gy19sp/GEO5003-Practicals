import random




class Agent():
    
#puts and defines new agent's location within the environment and make agents change it
    def __init__(self, environment, all_agents):
        self._y = (random.randint(0,199))
        self._x = (random.randint(0,199))
        self.environment = environment
        self.all_agents= all_agents
        self.store = 0 
        

#makes the agents move from the original location
    def move(self):

        if random.random( ) <0.5:
            self._y = (self._y + 1) % 199
        else:
            self._y = (self._y - 1) % 199
         
        if random.random( ) <0.5:
            self._x = (self._x + 1) % 199
        else:
            self._x = (self._x - 1) % 199

# makes agent eat the environment (grass)
    def eat(self): 
        if self.environment[self._y][self._x] > 10:
           self.environment[self._y][self._x] -= 10
           self.store += 10 
        else:
           self.store += self.environment[self._y][self._x]
           self.environment[self._y][self._x] = 0
        if self.store >= 100:
           # agents with a high storage eat parts of the grass , rather than just storing it
           self.store -= 5
           
    def distance_between(self, agents): #transferred from model
        dist= (((self._x - agents._x)**2) + ((self._y - agents._y)**2))**0.5 
        #print (dist)    #test to ,easure distances between agents
        return dist 
        
        
    def share_with_neighbours(self, neighbourhood):# definition
        for i in self.all_agents:# Loop through the agents in self.agents .
            distance = self.distance_between(i) # Calculate the distance between self and the current other agent:
            if distance <= neighbourhood:# If distance is less than or equal to the neighbourhood
                sum = self.store + i.store #combined storage
                ave = sum /2 #divide between agents
                self.store = ave #agents share
                i.store = ave

