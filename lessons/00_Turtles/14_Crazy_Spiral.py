"""
Crazy Spiral

Make your own crazy spiral with a pattern like
in 14_FLaming_Ninja_Star.py, but use what you've learned about loops
"""

... # Copy code to make a turtle and set up the window
import turtle
turtle.setup (width=600, height=600) 
window = turtle.Screen()
tina = turtle.Turtle()  # Create a turtle named t



# 1) Complete make_a_shape() to make the turtle move in some pattern. 
# For instance, you can make it go left 30 degrees, then forward 50 pixels, 
# then right 60 degrees, then forward 100 pixels. Make any shape you like.

def make_a_shape(t):
    """Make a shape with turtle t. Make it go left or right or forward"""    
    t.left(50)
    t.forward(50)
    t.left(50)
    t.forward(50)
    t.left(50)
    t.forward(50)
    t.left(50)
    t.forward(50)
# 2) Call make_a_shape() in a loop to make the turtle draw a spiral.
# For instance, you can call make_a_shape() 100 times to make a spiral with 100 shapes.
# The second ... in the for loop should be the number of shapes you want to make, 
# for example 100, or it could use islice(), cycle(), or a list of numbers.


for i in range(100):
    make_a_shape(tina)
    tina.right(360/5)

    turtle.done
