"""
Author: Troy Potter

I wasnt quite sure where to find the square.py code, so I wrote it

"""
import turtle

sideLength = int(input('Enter a side length for this square: '))

turtle.forward(sideLength)
turtle.left(90)
turtle.forward(sideLength)
turtle.left(90)
turtle.forward(sideLength)
turtle.left(90)
turtle.forward(sideLength)
turtle.left(90)

turtle.done()