import turtle  # 1. import modules
import random
import pygame
import math

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
michelangelo.up() 
leonardo.up()
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)
for _ in range(10):
    x1 = random.randrange(1,10)
    x2 = random.randrange(1,10)
    michelangelo.forward(x1)
    leonardo.forward(x2)
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

window.exitonclick()

##################################################

##PART B
pygame.init()
while True:
    for event in pygame.event.get():
        pass
    window = pygame.display.set_mode()
    points = []
    num_sides = [3,4,6,20,100,360]
    side_length = 100
    xpos = 300
    ypos = 400

    for sides in num_sides:
        for i in range(sides):
            angle = 360/sides
            radians = math.radians(angle * i)
            x = xpos + side_length * math.cos(radians)
            y = ypos + side_length  * math.sin(radians)
            points.append([x,y])
        window.fill('white')
        pygame.draw.polygon(window, 'Blue', points)
        pygame.display.flip()
        pygame.time.wait(1000)
        points = []
    break



  




