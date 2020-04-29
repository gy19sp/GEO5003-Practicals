
import random # imports the random function


""" ransomised position of y coordinate of agent in a 99*99 grid, this function varies
from the random.random function, as the randint functions offers the possibility to create 
a range of numbers whereas random.random offers a range from 0-1"""
y0= random.randint (0,99) 
x0= random.randint (0,99)

#Make Random movement by 1 step in the y coordinate
if random.random() < 0.5:# generates a random number with a value of 0-0.99
    y0 += 1 #increases a step in the y direction
else:
    y0 -= 1 #deccreases a step in the y direction
    
#This is the same movement for the x coordinate
if random.random() < 0.5:
    x0 += 1 #increases a step in the x direction
else:
    x0 -= 1 #decreases a step in the x direction

""" same action for a second agent"""

y1= random.randint (0,99) #generates a number within the specified parameters in this case 0-99
x1= random.randint (0,99)

#same method as for previous agent
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
    

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1
    
"""
#y0 = 0
#x0 = 0
#y1 = 4
#x1 = 3 values used to test pythagoras theorem that gives an answer of 5
the randomised sequence gives varying answers"""
    
    
answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5 
"""a suared+ b squared= c squared, **0.5 being the square root of c, which is 
the distance between 1 and 2"""


print (answer)# prints the result from the triangulation



