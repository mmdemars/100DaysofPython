import turtle
import pandas as pd 

states_df = pd.read_csv("./us-states-game-start/50_states.csv")
all_states = states_df.state.to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "./us-states-game-start/blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
guess_list = []

while len(guess_list) <50:
    answer_state = (screen.textinput(title=f"{len(guess_list)}/50 States Correct", prompt="What is anoter state's name?")).title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guess_list:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_df[states_df.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state.title())
        # if answer_state not in guess_list, append
        if answer_state not in guess_list:
            guess_list.append(answer_state)
      
