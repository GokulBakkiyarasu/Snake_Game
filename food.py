from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.penup()
        self.refresh()
        self.position()

    def refresh(self):
        xcor = random.randint(-280, 280)
        ycor = random.randint(-280, 280)
        self.goto(xcor, ycor)

    def position(self):
        return self.pos()
