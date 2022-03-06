import turtle as t
from turtle import  Screen
import random
tim = t.Turtle()
t.colormode(255)

# dashed line challege
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#  Multiple Shapes Challenge

# def draw_shapes(sides_number):
#     angles = 360 / sides_number
#     for _ in range(sides_number):
#         tim.forward(100)
#         tim.right(angles)
#
#
# for shape_sides in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shapes(shape_sides)

#  Random walk

# def ran_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     colours = (r, g, b)
#     return colours
# directions = [0, 90,  180, 270]
# tim.speed("fast")
# tim.pensize(15)
#
# for _ in range(200):
#     tim.color(ran_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#
def ran_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_randoms = (r, g, b)
    return color_randoms

tim.speed(0)

def drawinf_circle(size_gap):
    for _ in range(int(360 / size_gap)):
        tim.color(ran_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_gap)
        tim.circle(100)

drawinf_circle(5)


screen = Screen()
screen.exitonclick()







