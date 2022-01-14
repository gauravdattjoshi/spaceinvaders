from turtle import Turtle

from laser import Laser
from text import Text


class EnemyShip(Turtle):
    def __init__(self, protection):
        super().__init__()
        self.create_enemy_ships()
        self.box = protection
        self.y_cord = True
        self.game_over= False

    def create_enemy_ships(self):
        self.shape('square')
        self.speed(0)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()

    def shoot_laser(self, current_x, current_y, spaceship):
        print('shoot')
        if not self.game_over:
            self.y_cord=True
            print('value yccooord', self.y_cord)

        laser = Laser(current_x=current_x, current_y=current_y)
        laser.showturtle()
        laser.fillcolor((0, 0, 255))
        print(laser.pos(), "POSITION")
        while self.y_cord:

            laser.goto(laser.xcor(), laser.ycor() - 20)


            if abs(spaceship.xcor() - laser.xcor()) <= 20 and abs(spaceship.ycor() - laser.ycor()) <= 20:
                print('Haad 2')
                spaceship.clear()
                spaceship.reset()
                laser.reset()
                Text(text="Game Over", height=0)
                self.y_cord = False

            for each in self.box.protection_box_list:
                # print('Haad', each.xcor(), laser.xcor(), each.ycor(), laser.ycor(), each.distance(laser))
                print(each.distance(laser))
                if each.distance(laser)<=30:
                    print('found box')
                    self.box.protection_box_list.remove(each)
                    each.clear()
                    each.reset()
                    self.y_cord = False
                elif laser.ycor()< -500:
                    print('exit')
                    return 'exit'




            print(laser.pos(), "POSITION", )
            print('Haad 3 ')

        print('shooting', self.game_over, self.y_cord)
        laser.reset()
        laser.hideturtle()
        del laser
