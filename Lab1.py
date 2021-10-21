import turtle
import math
turtle.bgcolor("black")
turtle.pencolor('red')
turtle.speed(0)

#Square
for i in range(4):
    turtle.forward(50)
    turtle.left(90)

turtle.clear()
#Rectangle
for i in range(2):
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    
turtle.clear()

#Triangle
turtle.forward(100) 
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.clear()

#Star
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.penup()
turtle.right(150)
turtle.forward(55)

turtle.pendown()
turtle.right(90)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.clear()
turtle.penup()

#Hollow Star

turtle.home()
turtle.pendown()
for i in range(2):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
turtle.clear()

#Stick Figure
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.circle(30)
turtle.right(90)
turtle.forward(40)
turtle.right(120)
turtle.forward(50)
turtle.left(180)
turtle.forward(50)
turtle.left(60)
turtle.forward(50)
turtle.left(180)
turtle.forward(50)
turtle.left(60)
turtle.forward(70)
turtle.right(40)
turtle.forward(50)
turtle.right(180)
turtle.forward(50)
turtle.right(100)
turtle.forward(50)
turtle.penup()
turtle.clear()

#House
turtle.home()
def drawRectangle(t, width, height, color):
  t.fillcolor(color)
  t.begin_fill()
  t.forward(width)
  t.left(90)
  t.forward(height)
  t.left(90)
  t.forward(width)
  t.left(90)
  t.forward(height)
  t.left(90)
  t.end_fill()
  
def drawTriangle(t, length, color):
  t.fillcolor(color)
  t.begin_fill()
  t.forward(length)
  t.left(135)
  t.forward(length / math.sqrt(2))
  t.left(90)
  t.forward(length / math.sqrt(2))
  t.left(135)
  t.end_fill()

def drawParallelogram(t, width, height, color):
  t.fillcolor(color)
  t.begin_fill()
  t.left(30)
  t.forward(width)
  t.left(60)
  t.forward(height)
  t.left(120)
  t.forward(width)
  t.left(60)
  t.forward(height)
  t.left(90)
  t.end_fill()
  
def drawFourRays(t, length, radius):
  for i in range(4):
    t.penup()
    t.forward(radius)
    t.pendown()
    t.forward(length)
    t.penup()
    t.backward(length + radius)
    t.left(90)

turtle.penup() 
turtle.goto(-150, -120)
turtle.pendown()
drawRectangle(turtle, 100, 110, "blue")
turtle.penup()
turtle.goto(-120, -120)
turtle.pendown()
drawRectangle(turtle, 40, 60, "black")

turtle.penup()
turtle.goto(-150, -10)
turtle.pendown()
drawTriangle(turtle, 100, "red")

turtle.penup()
turtle.goto(-50, -120)
turtle.pendown()
drawParallelogram(turtle, 60, 110, "blue")

turtle.penup()
turtle.goto(-30, -60)
turtle.pendown()
drawParallelogram(turtle, 20, 30, "white")

turtle.penup()
turtle.goto(-50, -10)
turtle.pendown()
turtle.fillcolor("pink")
turtle.begin_fill()
turtle.left(30)
turtle.forward(60)
turtle.left(105)
turtle.forward(100 / math.sqrt(2))
turtle.left(75)
turtle.forward(60)
turtle.left(105)
turtle.forward(100 / math.sqrt(2))
turtle.left(45)
turtle.end_fill()
#tree
turtle.penup() 
turtle.goto(100, -130)
turtle.pendown()
drawRectangle(turtle, 20, 40, "brown")

turtle.penup() 
turtle.goto(65, -90)
turtle.pendown()
drawTriangle(turtle, 90, "lightgreen")
turtle.penup() 
turtle.goto(70, -45)
turtle.pendown()
drawTriangle(turtle, 80, "lightgreen")
george.penup() 
turtle.goto(75, -5)
turtle.pendown()
drawTriangle(turtle, 70, "lightgreen")
trutle.clear()

#Draw Polygon with sides
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
turtle.clear()
#Draw 3 Figures
answer = input("Enter either a Triangle, Square, or Rectangle:")

if answer == 'Triangle' :
    print('Triangle')

    turtle.forward(100) 
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
   
if answer == 'Rectangle' :
    print('Rectangle')

    turtle.forward(200)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(50)
    

if answer == 'Square' :
    print('Square')
    
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)



