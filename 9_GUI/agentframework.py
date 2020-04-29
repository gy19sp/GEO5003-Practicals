import random
import requests
import bs4


"""requests the website"""
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
"""extracts the data from the page"""
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
"""print(td_ys)
print(td_xs) """

#values assigned to x and y co-ordinates to be used in agent class
y= td_ys
x= td_ys

class Agent():
    
#puts and defines new agent's location within the environment and make agents change it
    def __init__(self, environment, all_agents):
        self._y = (random.randint(0,200))
        self._x = (random.randint(0,200))
        self.environment = environment
        self.agents= all_agents
        self.store = 0 
        

#makes the agents move from the original location
    def move(self):

        if (y == None):
            self._y = random.randint(0,200)
        else:
            self._y = y

        if (x == None):
            self._x = random.randint(0,200)
        else:
            self._x = x 

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
           
    #def distance_between(self, agents): #transferred from model
    #    return (((self._x - agents._x)**2) + ((self._y - agents._y)**2))**0.5 
        
        
    def share_with_neighbours(self, neighbourhood):# definition
        for i in self.all_agents:# Loop through the agents in self.agents .
            distance = self.distance_between(i) # Calculate the distance between self and the current other agent:
            if distance <= neighbourhood:# If distance is less than or equal to the neighbourhood
                sum = self.store + i.store #combined storage
                ave = sum /2 #divide between agents
                self.store = ave #agents share
                i.store = ave

