
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv
import random

""" In this exercise the model comes to life with an animation. another function from the matplotlib is being used to illustrate the
movement and action of the agents on the established environment"""


num_of_agents = 40 #define the number of agents (sheep), increased deliberitely
num_of_iterations = 100 #number of movements, also increased
neighbourhood= 20 #establishes the size of the neighbourhood


environment = [] # creates list for the environment
agents = [] #creates a list for the agents


# uses the csv module for the txt file to add environment data
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
#adding data to the environment list  
    for row in reader:
        environment.append(row)
            
#definition of animation
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#creating the agents to put into the model
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents)) 


carry_on = True	

#Visualisation of agents
def update(frame_number):#new addition
    random.shuffle(agents) # shuffles the agents' order
    
    fig.clear()   #new addition
    global carry_on
    
#sets the size of the plot, increased to match the starting positions of the sheep  
    matplotlib.pyplot.xlim(0, 200)
    matplotlib.pyplot.ylim(0, 200)#Defines the plot area
    matplotlib.pyplot.imshow(environment)#puts the environment on the plot
#defines behaviour of agents: eat, move, share in the model
    for i in range(num_of_agents):
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        agents[i].move()
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x, agents [i]._y,color='white', s=7)
        # puts the agents on the plot, gave them white colour to resemble sheep
        
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

"""defines the parameters for the animation including base figure, time(number of iterations/
set time/ generated), and whether or not the animation should be repeated"""
        
animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False)
""" define the animation which includes the figure, the update section which includes the various items from the agentframework, and the number of iterations which could have been
set to a random generator, but was instead fixed to the number of iterations, basically now all actions are being made within the environment
of the animation: The model"""

matplotlib.pyplot.show()
