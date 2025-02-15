import turtle

turtle.setup(width=600,height=600)
tina=turtle.Turtle()
tina.speed(1)

lefts = [90, 80, 70, 60]
colors = ["red", "blue", "green", "yellow"]
forwards = [23, 45, 97, 62]

for left, color, forward in zip(lefts, colors, forwards):
    tina.color(color)
    tina.forward(forward)
    tina.left(left)


turtle.exitonclick()