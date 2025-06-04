import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?").title()

    if answer_state == "Exit":
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data["x"].item()), int(state_data["y"].item()))
        t.write(answer_state, align="center")


# missing_states = []
# for state in all_states:
#     if state not in guessed_states:
#         missing_states.append(state)

# Updated version using List Comprehension
missing_states = [state_name for state_name in all_states if state_name not in guessed_states]

new_dataframe = pandas.DataFrame(missing_states)
new_dataframe.to_csv("states_to_learn.csv")

# screen.exitonclick()
