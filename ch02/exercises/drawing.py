import turtle

num_sides = int(input("Enter the number of sides"))
length = int(input("Enter length of each side"))
T1 = turtle.Turtle()
turtle.color("blue")
for i in range(num_sides):
    T1.forward(length)
    T1.right(360/num_sides)

turtle.exitonclick()
