# -*- coding: utf-8 -*-
import operator
import random # imports the random function
import matplotlib.pyplot



"""Pythagoras Theorem for the new agents to trinagulate distance
def distance_between(agents_row_a, agents_row_b): 
    answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
    distance = answer"""
    
    
agents= []

    
number_of_agents = 10 #number of agents in list
number_of_iterations= 100 #number of movements (instead of 2 as previously)

#creates agents in a loop
for i in range(number_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

#moves agents
for j in range(number_of_iterations):
    for i in range (number_of_agents):#movements of the agent (iterations)
        
# further move agents
#y
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 99
        else:
            agents[i][0] = (agents[i][0] - 1) % 99
  
#x
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 99
        else:
            agents[i][1] = (agents[i][1] - 1) % 99
""" note how the code has here been modified to use the agents from the list creating a list
of 10 agents instead of having to presnt the same agent for all agents, like before (code shrinking)"""


#print(max(agents))
#print(max(agents, key=operator.itemgetter(1))) 
print(list(agents))# shows coordinates of all agents even without the plot
#size of plot
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
for i in range (number_of_agents): #This puts the agents in the list on the graph
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
#presents plot
matplotlib.pyplot.show()

#print(answer)
""" as per the title a much leaner code has drastically increased the amount of work done. With the previous method
pages of code would be required to illustrate 10 agents, in reality an infinite number of agents could be presented here using the 
same amount of code"""
