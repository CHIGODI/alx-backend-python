#!/usr/bin/env python3

import turtle

# Set up the turtle
turtle.penup()       # Lift the pen so it doesn't draw
turtle.color('red')  # Set the color of the turtle to red
turtle.goto(0, -100) # Move the turtle to the starting position (centered, 100 units down)
turtle.pendown()     # Put the pen down to start drawing

# Draw a circle
turtle.circle(100)   # Draw a circle with a radius of 100 units

# Hide the turtle and display the result
turtle.hideturtle()  # Hide the turtle cursor
turtle.done()        # Finish the turtle graphics

print(turtle)