import turtle as t 

#Examples of functions we have been using
print("This is the print function.")

#The following example uses the range function
for i in range(4):
  #forward and left are functions from the turtle library
  t.forward(100)
  t.left(90)

#Define a function to draw a square
def drawsquare():
  for i in range(4):
    t.forward(100)
    t.left(90)

#Using a function
t.clear()
drawsquare()

#Define a function to draw an n-sided shape
def draw_ngon(num_sides):
  for i in range(num_sides):
    t.forward(50)
    t.left(360.0/num_sides)

t.clear()
t.speed(10)

#draw a square
draw_ngon(4)

#draw an octogon
draw_ngon(8)

#draw a 13-sided shape
draw_ngon(13)

#Define a function that takes multiple parameters
def draw_colored_ngon(num_sides, color):
  t.color(color)
  draw_ngon(num_sides)

draw_colored_ngon(5, 'blue')
draw_colored_ngon(6, 'purple')

#The following line will give an error because num_sides is defined inside a function
#print(num_sides)

#Variables defined outside of a function can be used inside the function
color = 'red'
draw_colored_ngon(7, color)

#Getting a value back from a function
def create_greeting(name):
  return "Hello. My names is " + name

greet = create_greeting("Liz")
print(greet)

#Using the system module to get user input
import sys 

#Get user input for a function
print("Enter a number")
#User input is always a string so be sure to convert it to another type if necessary
num_sides = int(sys.stdin.readline())

print("Enter a color")
color = sys.stdin.readline()

draw_colored_ngon(num_sides, color)
