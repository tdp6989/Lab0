"""
Author: Troy Potter

I wasnt quite sure where to find the square.py code, so I wrote it

"""
import turtle

def drawSquare(sideLength):
    """
    :param sideLength: Length of square side
    : Draws square
    :return:
    """
    turtle.forward(sideLength)
    turtle.left(90)
    turtle.forward(sideLength)
    turtle.left(90)
    turtle.forward(sideLength)
    turtle.left(90)
    turtle.forward(sideLength)
    turtle.left(90)

    """
    Moves the turtle to the right of the first drawn square by 25
    """
    turtle.up()
    turtle.forward(sideLength + 25)
    turtle.down()


sideLength = int(input('Enter a side length for this square: '))
drawSquare(sideLength)
drawSquare(sideLength)

turtle.done()