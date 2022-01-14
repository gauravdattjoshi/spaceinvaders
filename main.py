# box which shoots lazers
# boxlayers in center
# box shooting lazers automatically above
# lazers is a turtle
# box layers |||||||||||||||| |||||||| |||||||
#
#
#
#
#
import functools
import threading
import time
from turtle import *

from enemy.enemy_fleet import EnemyFleet
from Protection.protection_layers import ProtectionLayer
from spaceship import SpaceShip
from text import Text

screen = Screen()
screen.bgcolor((0, 0, 0))
screen.setup(width=800, height=800)
screen.listen()
screen.title('Space Invaders Game')
screen.colormode(255)

heading = Text(text='Space Invaders Game', height=380)

protection_layers = ProtectionLayer()
enemy_fleet = EnemyFleet(protection=protection_layers)
spaceship = SpaceShip(protection=protection_layers, enemyfleet=enemy_fleet)
start_game = Text('Press s to start the game', height=0)

time.sleep(3)
start_game.clear()
screen.onkeypress(spaceship.move_left, 'Left')
screen.onkeypress(spaceship.move_right, 'Right')
screen.onkeypress(spaceship.shoot_lasers, 'Up')
screen.onkeypress(functools.partial(enemy_fleet.check, spaceship), 's')

screen.exitonclick()
