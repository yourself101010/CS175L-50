"""
Name: Tennessee Tremain
Course: CS-175L
Program: Turtle graphics STOP sign
"""

#Import
import math
import turtle

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -10
TEXT_Y = -10

#Size the window
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

#Make turtle cool
alex = turtle.Turtle()
alex.color("green")
alex.pencolor("red")
alex.shape("turtle")

#Instructions
"""
# Calculate the diameter of the octagon so we
# can center it in the graphics window.
#                s
#        ---------------
#       / |             \
#  s   /  |              \
#     /   | x             \  s
#    /    |                \
#   |------                 |
#   |   x                   |
#   |                       |
#   To get the diameter:
#     diameter = s + 2 * x
#   We know that s is 100.
#   Use Pythagoras to get x:
#   s^2 = x^2 + x^2
#   s^2 = 2*x^2
#   x = s / sqrt(2)
"""

#Calculate Diameter
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

#Setup Position
yStart = (WINDOW_HEIGHT/2) - ((WINDOW_HEIGHT-diameter)/2)
xStart = -(yStart) + x

alex.penup()
alex.goto(xStart,yStart)
alex.pendown()

#For loop
for i in range(8):
    alex.forward(100)
    alex.right(45)

#Stop Text
alex.penup()
alex.goto(TEXT_X,TEXT_Y)
alex.pendown()
alex.write("STOP")
alex.hideturtle()
