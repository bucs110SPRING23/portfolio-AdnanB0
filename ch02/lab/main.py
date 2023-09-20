import turtle  # 1. import modules
import random

# Part A
window = turtle.Screen()  # 2.  Create a screen
window.bgcolor("lightblue")

michelangelo = turtle.Turtle()  # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color("orange")
leonardo.color("blue")
michelangelo.shape("turtle")
leonardo.shape("turtle")

michelangelo.up()  # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)
x = random.randrange(1,100)
michelangelo.forward(random.randrange(1,100))
leonardo.forward(random.randrange(1,100))
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

#################################################

## Race 2
x1 = random.randrange(1,101)
x2 = random.randrange(1,101)
michelangelo.up() 
leonardo.up()
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)
for _ in range(x1):
    michelangelo.forward(x1)
    leonardo.forward(x2)
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

window.exitonclick()

##################################################

##PART B
import pygame
import math
pygame.init()
window = pygame.display.set_mode()


