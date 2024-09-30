#fractals
import turtle
turtle.speed(-100)
def triangle(length,count):
    for i in range(3):
        turtle.forward(length)
        turtle.right(120)
        if count>=0:
            triangle(length/2,count-1)
        

turtle.right(300)
triangle(300,4)
