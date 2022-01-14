import random

from enemy.enemy_ships import EnemyShip


class EnemyFleet():
    def __init__(self, protection):
        super().__init__()
        self.enemy_list = []
        self.count = 0
        self.box = protection
        self.create_enemy_fleet()

    def create_enemy_fleet(self):
        for item in range(0, 6):
            enemy_ship = EnemyShip(self.box)
            enemy_ship.fillcolor((255, 0, 0))
            self.enemy_list.append(enemy_ship)
            enemy_ship.goto(380 - item * 60, 300)

    def check(self, spaceship):
        print('RUNNING')
        if any(enemy.xcor() > 370 for enemy in self.enemy_list):
            while any(enemy.xcor() > -170 for enemy in self.enemy_list):
                print('fun run')
                self.run_loop(left=True, spaceship=spaceship)
                print('fun run 2')
            self.check(spaceship)
        elif any(enemy.xcor() < -359 for enemy in self.enemy_list):
            while any(enemy.xcor() < 170 for enemy in self.enemy_list):
                self.run_loop(left=False, spaceship=spaceship)
            for enemy in self.enemy_list:
                enemy.sety(enemy.ycor() - 50)
            self.check(spaceship)

    def run_loop(self, left, spaceship):
        for enemy in self.enemy_list:
            self.count += 1
            if left:
                enemy.backward(20)
            else:
                enemy.forward(20)

            current_x = enemy.xcor()
            current_y = enemy.ycor()
            if self.count > random.randint(0, len(self.enemy_list)):
                enemy.shoot_laser(current_x=current_x, current_y=current_y, spaceship=spaceship)
                self.count = 0
