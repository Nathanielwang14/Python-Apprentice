"""
Make an obedient turtle that will obey commands to draw shapes.
"""

import turtle
from guizero import App, Box, Text, TextBox, PushButton, ListBox, error
from tkinter import messagebox
from tkinter import simpledialog, Tk
turtle.setup (width=500, height=500)
tina = turtle.Turtle()     
# TODO)
#   1. Create a turtle.
#   2. Write 3 function definitions for drawing a square, triangle, and
#      circle.
#   3. Ask the user for the for a shape to draw.
#   4. Draw the appropriate shape depending on their answer (call the right
#      function)



def ask_function(prompt):
    while True:
        try:
            return str(simpledialog.askstring("Textbox", prompt))
        except ValueError:
            return messagebox.showinfo("Please enter one of the options")
        
def ask_phrase(prompt):
      while True:
        try:
            return str(simpledialog.askstring("Textbox", prompt))
        except ValueError:
            print("Please enter a actual word!")

def sqaure():
    tina.pendown()
    for i in range(4):
        tina.forward(85)
        tina.right(90)
   
def triangle():
     tina.pendown()
     tina.right(120)
     tina.forward(85)
     tina.right(120)
     tina.forward(85)
     tina.right(120)
     tina.forward(85)

 
def circle():
    tina.circle(90)

circle()
shapes = ['triangle', 'sqaure', 'circle']

def draw_shape(value):
    for word in value:
        if word in shapes:
            if word == 'triangle':
                triangle()
            elif word == 'square':
                sqaure()
            elif word == 'circle':
                circle()
                
draw_shape(ask_phrase("Enter Word"))

turtle.exitonclick()