# 100 Days of Code: Python
# May 19, 2022
# Guess all the US state names!

# Import modules
import turtle
import pandas

# Setup screen with map
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Grab US states data
data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()

guessed_states = []

while len(guessed_states) < 50:
    # Get answer input
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        break

    if answer_state in all_states:
        # Lookup x, y coordinates for writing
        x = int(data.loc[data["state"] == answer_state, "x"].item())
        y = int(data.loc[data["state"] == answer_state, "y"].item())

        # Write state name to the screen
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x, y)
        t.write(answer_state)

        # Add correct state to player's list
        guessed_states.append(answer_state)

# Save gussed states to a .csv
df = pandas.DataFrame(guessed_states, columns=["state"])
df.to_csv("gussed_states.csv")

# Show which states the player needs to learn
states_to_learn = all_states
for s in guessed_states:
    if s in states_to_learn:
        states_to_learn.remove(s)

# Save those states to a .csv
df2 = pandas.DataFrame(states_to_learn, columns=["state"])
df2.to_csv("states_to_learn.csv")