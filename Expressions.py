from turtle import Turtle, Screen

def tuckCentered(turtle, center, side1, side2):

    xPt, yPt = center

    xPt -= side1 / 2
    yPt += side2 / 2

    turtle.up()
    turtle.goto(xPt, yPt)
    turtle.down()

    for _ in range(1):
        turtle.forward(side1)
        turtle.right(90)
        turtle.forward(side2)
        turtle.right(90)
        turtle.forward(side1)
        turtle.right(90)
        turtle.forward(side2)

tuck = Turtle()

tuckCentered(tuck, (0, 0), 100, 200)

screen = Screen()


