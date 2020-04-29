import matplotlib.pyplot
import agentframework
import csv
import random

num_of_agents = 10 #define the number of agents
num_of_iterations = 100 #defines the number of iterations
neighbourhood= 20# defines the number of neighbourhoods


environment = [] # creates list for the environment
agents = [] #creates a list for the agents
agentlist = [] #list of agents for other agents to know about

# uses the csv module for the txt file to add environment data
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
#adding data to the environment list  
    for row in reader:
        environment.append(row)

#creating the agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

    
    random.shuffle(agents) # shuffles the agents' order
    
#defines behaviour of agents: eat, move, share
for j in range(num_of_iterations):    
    for i in range(num_of_agents):
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)# the new function allows the agents to also interact with the other agents
        agents[i].move()
        
        

#Visualisation of agents
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)#Defines the plot area
matplotlib.pyplot.imshow(environment)#puts the environment on the plot
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)# puts the agents on the plot
matplotlib.pyplot.show()


