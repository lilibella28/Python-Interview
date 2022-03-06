from turtle import Turtle, Screen
import random
race_still_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []


for turtle_index in range(0, 6):
    new_tim = Turtle(shape="turtle")
    new_tim.color(colors[turtle_index])
    new_tim.penup()
    new_tim.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_tim)


if user_bet:
    race_still_on = True


while race_still_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            race_still_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"you've won! the {winner_color} turtle is the winner")
            else:
                print(f"you've lose! the {winner_color} turtle is the winner")

        distance_turtle = random.randint(0, 10)
        turtle.forward(distance_turtle)


screen.exitonclick()