import random

import pygame

from game_objects.players.Player import Player


class Enemy(Player):
    health = 100 #boss

    isAlive = True
    moving_left = True
    moving_right = False

    l_stop = 0
    r_stop = 0
    player_x_center = 200

    image = pygame.image.load("res/enemy.png")
    destroyed_image = pygame.image.load("res/dead.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.moveSpeed = 2
        self.image = pygame.transform.scale(self.image, (super().get_width(), super().get_height()))
        self.destroyed_image = pygame.transform.scale(self.destroyed_image, (super().get_width(), super().get_height()))

    def get_img(self):
        return self.image

    def is_alive(self):
        return self.health > 0

    def take_life_points(self, damage):
        self.health -= damage

    def set_img(self, img):
        self.image = img

    def move(self, player, screen_width):
        if self.moving_left:
            if self.l_stop < 0:
                self.l_stop = 0
            super().move_left()
            if super().get_x() <= self.l_stop:
                self.player_x_center = player.get_x() + player.get_width() / 2
                if self.get_x() < player.get_x() + 30 + 100:
                    self.r_stop = round(random.randrange(player.get_x(), player.get_x() + 30 + 100, 10))
                else:
                    self.l_stop = 0
                    self.r_stop = 500
                self.moving_left = False
                self.moving_right = True
        else:
            if self.r_stop > screen_width:
                self.r_stop = screen_width
            super().move_right(screen_width)
            if super().get_x() >= self.r_stop - self.width:
                self.player_x_center = player.get_x() + player.get_width() / 2
                if player.get_x() - 70 < self.get_x():
                    self.l_stop = round(random.randrange(player.get_x() - 70, player.get_x(),
                                                         10))  # TODO fix the problem with range (0, 0 - 40)????
                else:
                    self.l_stop = 0
                    self.r_stop = 500
                self.moving_left = True
                self.moving_right = False
