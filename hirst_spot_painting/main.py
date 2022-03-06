# import colorgram as c
# final_colors = []
# colors = (c.extract("colors_image.jpg", 15))
# for color in colors:
#      r = color.rgb.r
#      g = color.rgb.g
#      b = color.rgb.b
#      new_colors = (r, g, b)
#      final_colors.append(new_colors)
# print(final_colors)

# Todo extract color to convert then randonly in the dog
# Todo 10 by 10 row of spot
# Todo dot must be size 20 and have 50 space in between


import turtle as t
from turtle import Screen
import random
t.colormode(255)
turtle = t.Turtle()
turtle.speed("fast")
turtle.penup()
turtle.hideturtle()
colors_list = [(235, 234, 230), (238, 230, 234), (231, 240, 235), (228, 234, 240), (237, 34, 109), (157, 22, 64), (9, 145, 91), (241, 72, 33), (180, 158, 41), (231, 163, 47), (80, 19, 73), (24, 122, 187), (46, 190, 231), (241, 219, 56), (126, 192, 79)]
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
row_dots = 100
for dots_number in range(1, row_dots + 1):
    turtle.dot(20, random.choice(colors_list))
    turtle.forward(50)
    if dots_number % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)







screen = Screen()
screen.exitonclick()