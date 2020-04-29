import random
import operator
import matplotlib.pyplot
import time
import math # as suggested by link below this module involves mathematical operations such as sum pow etc

start = time.clock()

def distance_between(agents_row_a, agents_row_b):
    points= zip(agents_row_a, agents_row_b)
    diffs_squared_distance = [pow(a - b, 2) for (a, b) in points]
    return math.sqrt(sum(diffs_squared_distance))#pythagoras theorem to triangulate distance
# adapted from https://www.kdnuggets.com/2016/01/implementing-your-own-knn-using-python.html/2
# attempted this version for the sake of trying something different, In the end the version presented in the practicals, seems to be neater
    
num_of_agents = 10# number of agents
num_of_iterations = 100# number of movements by agents
agents = [] # list for the agents to populate

    
# Makes the agents in a ransom position
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Moves the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 99
        else:
            agents[i][0] = (agents[i][0] - 1) % 99

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 99
        else:
            agents[i][1] = (agents[i][1] - 1) % 99



"""
distance = distance_between(agents[0], agents[1])#tests arbitrary agents once
# random distance between random agents, therefore the answer varies
"""

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
""" The answer I am getting is always 0.0, I am assuming that since all agents are being 
measured against eacj other the values are cancelling out"""
        
print(distance) #The result here is contingent with which formula is being used
       
       
#the answer for the test is 0.0 because all distances are being tested twice?






end = time.clock() # end of timing

# sets the dimensions of the plot
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
for i in range(num_of_agents):# present the agents
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show() #show the graph

print("time = " + str(end - start))# prints the timing


""" time with 10 agents 0.004385, 100: 0.03920, 1000: 0.40870, 10000: 3.92710
timings have a wide range. After multiple tests setting the test 
after the matplot gives higher times"""