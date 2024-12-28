import turtle
import pandas

# Set up the screen
screen = turtle.Screen()
screen.title("India Map Game")
image = "india-map.gif"
screen.addshape(image)
turtle.shape(image)

# Read the data from the CSV file
data = pandas.read_csv("india_states_data.csv")
all_states = data.indian_states.to_list()

guessed_states = []
while len(guessed_states) < 28:
    # Prompt the user to enter a state's name
    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 State Correct",
                                    prompt="What's another state's name?").title()
    print(answer_state)

    # If the user types "Exit", save the missing states to a CSV file and break the loop
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        missing_data = pandas.DataFrame(missing_state, columns=["indian_states"])
        missing_data.to_csv("missing_data.csv", index=False)
        print(pandas.read_csv("missing_data.csv"))
        break

    # If the guessed state is correct, add it to the guessed_states list and display it on the map
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.indian_states == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state, align="center", font=("Arial", 8, "bold"))