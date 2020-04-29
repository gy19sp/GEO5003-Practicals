import matplotlib
matplotlib.use('TkAgg') 
import tkinter
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv
import random

""" to test if the model is working without the GUI setup, all options related to the GUI were 
commented out, and the new sata from the text file was used. the animation worked fine"""

num_of_agents = 50 #define the number of agents (sheep), increased deliberitely
num_of_iterations = 100 #number of movements, also increased
neighbourhood= 20


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

    
    random.shuffle(agents) # shuffles the agents' order

carry_on = True	

#Visualisation of agents


def update (frame_number):#new addition
    
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
     
 
def run(i):

    model_menu.entryconfig("Run model", state="disable")



"""model could not be associated with menus"""
root = tkinter.Tk()
root.wm_title("Model")
menu = tkinter.Menu(root)
root.config(menu=menu)
#sets the Menu
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)# creates the model menu with pulldown
model_menu.add_command(label="Run model", command=run)# creates the run model option


canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

ani = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False)
# describes the snimation

tkinter.mainloop() 







   

  


