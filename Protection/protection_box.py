import random
from turtle import Turtle


class ProtectionBox(Turtle):
    def __init__(self):
        super().__init__()
        self.create_protection_box()

    def create_protection_box(self):
        self.hideturtle()
        self.shape('square')
        self.speed(0)
        self.fillcolor((random.randint(0, 255), random.randint(10, 255), random.randint(0, 255)))
        self.shapesize(stretch_wid=1, stretch_len=2 )
        self.penup()