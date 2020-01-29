import pygame

from players.Player import Player


class MainPlayer(Player):

    image = pygame.image.load("res/player.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(self.image, (super().get_width(), super().get_height()))

    def get_img(self):
        return self.image


