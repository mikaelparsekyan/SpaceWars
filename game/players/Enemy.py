import pygame

from players.Player import Player


class Enemy(Player):
    health = 100

    isAlive = True
    moving_left = True
    moving_right = False

    image = pygame.image.load("res/enemy.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.moveSpeed = 3
        self.image = pygame.transform.scale(self.image, (super().get_width(), super().get_height()))

    def get_img(self):
        return self.image

    def is_alive(self):
        return self.health > 0

    def move(self, screen_width):
        if self.moving_left:
            super().move_left()
            if super().get_x() <= 0:
                self.moving_left = False
                self.moving_right = True
        else:
            super().move_right(screen_width)
            if super().get_x() >= screen_width - self.width:
                self.moving_left = True
                self.moving_right = False

