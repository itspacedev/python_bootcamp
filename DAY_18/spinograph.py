import turtle
from turtle import Turtle, Screen
import random
import math

turtle.colormode(255)


def random_color():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color


t = Turtle()
t.speed("fastest")
t.pensize(2)


def draw_spirograph(gap_size):
    for circle_number in range(int(360 / gap_size)):
        t.pencolor(random_color())
        t.setheading(t.heading() + gap_size)
        t.circle(100)


draw_spirograph(5)

s = Screen()
s.exitonclick()
