import pygame

from game_objects.players.Player import Player


class MainPlayer(Player):
    image = pygame.image.load("res/player.png")

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h,self.image)

    def get_img(self):
        return self.image
