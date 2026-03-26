# --- Project 25 ---

from turtle import Turtle, Screen, shape, mainloop
import pandas as pd

screen = Screen()
screen.title("U.S. States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
shape(image)

STATES_DATA = pd.read_csv("50_states.csv")
correct_guesses = []
writer = Turtle()
writer.hideturtle()
writer.penup()

while len(correct_guesses) < len(STATES_DATA):
    answer_state = (
        str(
            screen.textinput(
                title=f"{len(correct_guesses)} / {len(STATES_DATA)} States Correct",
                prompt="What's another state's name?",
            )
        )
        .strip()
        .title()
    )

    if answer_state in ["Exit", "None", ""]:
        missing_states = []
        for state in STATES_DATA.state.to_list():
            if state not in correct_guesses:
                missing_states.append(state)
        new_df = pd.DataFrame(missing_states)
        new_df.to_csv("missed_states.csv")
        break

    if answer_state in STATES_DATA["state"].to_list():
        correct_guesses.append(answer_state)
        state_data = STATES_DATA[STATES_DATA.state == answer_state]
        writer.goto(state_data.x.item(), state_data.y.item())
        writer.write(answer_state, align="center", font=("Arial", 8, "normal"))

screen.exitonclick()
