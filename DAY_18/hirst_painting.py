# import colorgram
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     c = (r, g, b)
#     rgb_colors.append(c)

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

t = Turtle()
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(250)
t.setheading(180)
t.forward(100)
t.setheading(0)


def draw_line_of_dots():
    for _ in range(10):
        t.dot(20, random.choice(color_list))
        t.forward(50)

    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)


for _ in range(10):
    draw_line_of_dots()

s = Screen()
s.exitonclick()