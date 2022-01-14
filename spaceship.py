
from turtle import Turtle

from laser import Laser


class SpaceShip(Turtle):
    def __init__(self, protection, enemyfleet):
        super().__init__()
        self.create_ship()
        self.box = protection
        self.enemy_fleet = enemyfleet

    def move_left(self):
        self.goto(self.xcor()-20, self.ycor())

    def move_right(self):
        self.goto(self.xcor()+20, self.ycor())

    def create_ship(self):
        self.hideturtle()
        self.goto(0,-350)
        self.shape('turtle')
        self.penup()
        self.fillcolor("green")
        self.showturtle()

    def shoot_lasers(self):
        current_x = self.xcor()
        current_y = self.ycor()
        laser = Laser(current_x, current_y)
        laser.fillcolor((255,255,255))
        laser.showturtle()
        ycor = True

        while ycor:
            laser.goto(laser.xcor(), laser.ycor() + 20)
            for enemy in self.enemy_fleet.enemy_list:
                if abs(enemy.xcor() - laser.xcor()) <= 20 and abs(enemy.ycor() - laser.ycor()) <= 20 :
                    self.enemy_fleet.enemy_list.remove(enemy)
                    print('found enemy spaceship')
                    enemy.clear()
                    enemy.reset()
                    laser.reset()
                    break
            for each in self.box.protection_box_list:
                if abs(each.xcor() - laser.xcor()) <= 20 and abs(each.ycor() - laser.ycor()) <= 20:
                    print('found box by enemy spaceship')
                    self.box.protection_box_list.remove(each)
                    each.clear()
                    each.reset()
                    ycor = False

        laser.reset()
        laser.hideturtle()
        del laser