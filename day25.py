import pandas as pd
import turtle

df = pd.read_csv("50_states.csv")
data = df["state"].to_list()
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guesses = []
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed("fastest")
while len(guesses) < 50:
    guess = screen.textinput(title=f"{len(guesses)}/50 Guess the states",prompt="Enter state: ").title()
    guesses.append(guess)
    if guess in data:
        curr = df[df["state"]==guess]
        t.goto(int(curr['x']),int(curr["y"]))
        t.write(guess)
        data.remove(guess)
data = pd.DataFrame(data)
data.to_csv("wrong guesses.csv")


screen.exitonclick()