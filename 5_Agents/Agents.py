#import random 
#import operator
import matplotlib.pyplot
import agentframework# calls for the newly created file which separates the model per se from the workings of the agents

#revised version of pythagoras theorwm, as per notes. This version appears to be much simplet
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a._x - agents_row_b._x)**2) +
    ((agents_row_a._y - agents_row_b._y)**2))**0.5

num_of_agents = 10# number of agents
num_of_iterations = 100 # number of iterations by agents
agents = []# agent list

"""the workings of the initial position of the agents has been moved to a different file (namely: agent framework), this 
file is being dedicated to the model per se"""

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent())

# Move the agents. the formula of movements has been transfered to the agentframework file
for j in range(num_of_iterations):# this displays the number of movements the agent will be doing
    for i in range(num_of_agents):
        agents[i].move()# new functions that moves the agent within the environment also tied to the agent framework

#sets the size of the plot        
matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.ylim(0, 100)
#puts the ganets on the plot
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        
# Connected to the agentframework file
a = agentframework.Agent()

print(a._y, a._x)# prints y and x co-ordinate of agents