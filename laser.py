from turtle import Turtle

class Laser(Turtle):
    def __init__(self, current_x, current_y):
        super().__init__()
        self.hideturtle()
        self.create_laser(current_x,current_y)

    def create_laser(self, current_x, current_y):
        self.shape('square')
        self.speed(0)
        self.shapesize(stretch_wid=2,stretch_len=1)
        self.penup()
        self.goto(current_x,current_y)

