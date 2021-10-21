import turtle
turtle.goto(-60,50)
turtle.bgcolor("black")
size = int(input("Choose the size:"))
sides = int(input("Choose the number of sides:"))
angle = 360/sides
clr = "red"

def draw_polygon():
    turtle.color(clr)
    turtle.begin_fill()
    for i in range (sides):
        turtle.forward(size)
        turtle.left(angle)
    turtle.end_fill()
    turtle.hideturtle()
draw_polygon()