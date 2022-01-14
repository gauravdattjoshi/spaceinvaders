from turtle import Turtle


class Text(Turtle):
    def __init__(self, text, height):
        super().__init__()
        self.create_protection_box(text, height)

    def create_protection_box(self, text, height):
        self.hideturtle()
        self.penup()
        self.color((255,255,0))
        self.goto(-150,height)
        self.write(text, move=False, font=("Verdana", 50, "bold"))