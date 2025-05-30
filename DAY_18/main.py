from turtle import Turtle, Screen
import random

colors = ["blue", "red", "brown", "coral", "medium slate blue"]

t = Turtle()
t.shape("turtle")


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)


for sides in range(3, 11):
    t.color(random.choice(colors))
    draw_shape(sides)


s = Screen()
s.exitonclick()
