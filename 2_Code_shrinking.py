import matplotlib.pyplot # imports the plotting package
import random # imports the random function
import operator # imports operator package

""" ransomised position of y coordinate of agent in a 99*99 grid, this function varies
from the random.random function, as the randint functions offers the possibility to create 
a range of numbers whereas random.random offers a range from 0-1"""

agents = []#creates list for agents to use
agents.append([random.randint(0,99),random.randint(0,99)]) #appends agent to the list
""" With this seturp an indication of y,x has been lost"""

#Make Random movement by 1 step in the y coordinate
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1
    
#This is the same movement for the x coordinate
if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1

""" same action for a second agent"""

agents.append([random.randint(0,99),random.randint(0,99)]) #agent 1
#Make Random movement by 1 step in the y coordinate
if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1
    
#This is the same movement for the x coordinate
if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1
    


#print (list(agents))is another function which can be used to list the position of agents
print(max(agents)) #answer here depends only on the y taking the x into account if the y's are equal
print(max(agents, key=operator.itemgetter(1)))# this allows to have the reult also from the x directions
#Item getter is indexed at (1) representing the y 

#deliniates the area of the plot graph
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
#presentes the agents
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
m = max(agents, key=operator.itemgetter(1)) #the true max in the x direction
matplotlib.pyplot.scatter(m[1],m[0], color='red') #the eastermost point is coloured in red
matplotlib.pyplot.show()# shows the plot

