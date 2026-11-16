import turtle
import colorsys
bob = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("RAINBOW 6")
bob.speed(0)
bob.width(2)
bob.hideturtle()
colors = 360
for i in range(360):
    color = colorsys.hsv_to_rgb(i / 360, 1, 1)
    bob.pencolor(color)
    bob.circle(i * 0.8)
    bob.left(61)
    bob.forward(i * 1.2)
    bob.left(119)
    bob.circle(i * 0.5)
    bob.right(7)
for i in range(100):
    color = colorsys.hsv_to_rgb(i / 100, 1, 1)
    bob.pencolor(color)
    bob.circle(150)
    bob.left(137)
