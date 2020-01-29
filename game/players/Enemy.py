import pygame

from players.Player import Player


class Enemy(Player):
    health = 100

    isAlive = True

    image = pygame.image.load("res/enemy.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(self.image, (super().get_width(), super().get_height()))

    def get_img(self):
        return self.image

    def is_alive(self):
        return self.health > 0