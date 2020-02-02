import random

import pygame

from game_objects.Config import ENEMY_MOVE_SPEED, SCREEN_WIDTH
from game_objects.players.Player import Player


class Enemy(Player):
    moving_left = True
    moving_right = False

    left_stop = 0
    right_stop = 0

    image = pygame.image.load("res/enemy.png")
    destroyed_image = pygame.image.load("res/dead.png")

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h, self.image)
        super().set_move_speed(ENEMY_MOVE_SPEED)
        self.destroyed_image = pygame.transform.scale(self.destroyed_image, (super().get_width(), super().get_height()))

    def move(self, player):
        if self.moving_left:
            if self.left_stop < 0:
                self.left_stop = 0
            super().move_left()
            if super().get_x() <= self.left_stop:
                self.player_x_center = player.get_x() + player.get_width() / 2
                if self.get_x() < player.get_x() + 30 + 100:
                    self.right_stop = round(random.randrange(player.get_x(), player.get_x() + 30 + 100, 10))

                self.moving_left = False
                self.moving_right = True
        else:
            if self.right_stop > SCREEN_WIDTH:
                self.right_stop = SCREEN_WIDTH
            super().move_right()
            if super().get_x() >= self.right_stop - self.width:
                self.player_x_center = player.get_x() + player.get_width() / 2
                if player.get_x() - 70 < self.get_x():
                    self.left_stop = round(random.randrange(player.get_x() - 70, player.get_x(),
                                                            10))  # TODO fix the problem with range (0, 0 - 40)????
                self.moving_left = True
                self.moving_right = False
