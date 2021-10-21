import turtle
turtle.bgcolor("black")
turtle.pencolor('red')

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
 
 