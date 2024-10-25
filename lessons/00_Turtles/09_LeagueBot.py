""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle as turtle

# screen = turtle.Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor('white')

t = turtle.Turtle()

... # Your Code Here
import turtle

def set_background_image(window, image_name):

    from pathlib import Path
    from PIL import Image


    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)
   

tina = turtle.Turtle()                 

screen = turtle.Screen()                
set_background_image(screen, "leaguebot_bolt.gif") 

tina.turtlesize(stretch_wid=10, stretch_len=10, outline=4)
tina.pencolor('blue')

tina.pendown
for i in range(6):
    tina.forward(40)
    tina.left(60)

turtle.done()      