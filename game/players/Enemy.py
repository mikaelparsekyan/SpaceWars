import random
from datetime import datetime

import pygame

from players.Player import Player


class Enemy(Player):
    health = 100

    isAlive = True
    moving_left = True
    moving_right = False

    l_stop = 0
    r_stop = 0

    image = pygame.image.load("res/enemy.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.moveSpeed = 2
        self.image = pygame.transform.scale(self.image, (super().get_width(), super().get_height()))

    def get_img(self):
        return self.image

    def is_alive(self):
        return self.health > 0

    def move(self, screen_width):

        if self.moving_left:
            super().move_left()
            if super().get_x() <= self.l_stop:
                self.r_stop = round(random.randrange(self.get_x() + 40, screen_width, 5))
                self.moving_left = False
                self.moving_right = True
        else:
            super().move_right(screen_width)
            if super().get_x() >= self.r_stop - self.width:
                self.l_stop = round(random.randrange(0, self.get_x() - 40 , 5))#TODO fix the problem with range (0, 0 - 40)????
                print(self.l_stop)
                self.moving_left = True
                self.moving_right = False