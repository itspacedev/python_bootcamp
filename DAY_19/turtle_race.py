from turtle import Turtle, Screen
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
DISTANCE = 20
FINISH_LINE = 210
is_race_on = False

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

position_x = - (SCREEN_WIDTH / 2 - DISTANCE)
position_y = - ((SCREEN_HEIGHT - 6 * 2 * DISTANCE) / 2)

turtles = []
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=position_x, y=(position_y + i * 2 * DISTANCE))
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for t in turtles:
        random_step = random.randint(5, 10)
        t.forward(random_step)

        turtle_position = t.pos()
        if turtle_position[0] >= FINISH_LINE:
            is_race_on = False
            print(f"Turtle {t.pencolor()} win the race!")
            if user_bet == t.pencolor():
                print("Congratulations! You was right!!")
            else:
                print("Sorry, you got it wrong :(")

            break


screen.exitonclick()
