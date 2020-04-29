import matplotlib.pyplot
import agentframework
import csv# new module being used to convert the data within a txt file to be used in python


num_of_agents = 10 #define the number of agents
num_of_iterations = 100

environment = [] # new list that incorporates environmental data
agents = [] #creates a list for the agents

# uses the csv module for the txt file
with open('in.txt', newline='') as f: # sets the CSV as a txt file reader
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)# uses the reader 

#use in data in file as environment   
    for row in reader:
        environment.append(row)

# Call the agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))

# Move the agents and make them eat within the environment
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        
#calculate the distance
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a._x - agents_row_b._x)**2) +
    ((agents_row_a._y - agents_row_b._y)**2))**0.5

#sets the plt size
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
#shows the environment in the plot
matplotlib.pyplot.imshow(environment)
#puts agents in the plot
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
#shows the plot/ model
matplotlib.pyplot.show()




