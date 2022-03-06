from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("slow")
        self.refresh()

    def refresh(self):
        ramnd_x = random.randint(-280, 280)
        ramnd_y = random.randint(-280, 280)
        self.goto(ramnd_x, ramnd_y)