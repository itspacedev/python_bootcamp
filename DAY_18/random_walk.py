import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

TURTLE_STEP = 30
TURTLE_THICKNESS = 15
directions = [0, 90, 180, 270]


def random_color():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color


def random_move():
    t.setheading(random.choice(directions))
    t.forward(TURTLE_STEP)


t = Turtle()
t.width(TURTLE_THICKNESS)
t.speed(8)

for _ in range(100):
    t.pencolor(random_color())
    random_move()

s = Screen()
s.exitonclick()
