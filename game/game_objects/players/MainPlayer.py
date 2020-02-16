import pygame

from game_objects.Config import PLAYER_INITIAL_IMAGE_PATH, PLAYER_MOVE_SPEED, SCREEN_WIDTH
from game_objects.players.Player import Player


class MainPlayer(Player):

    image = pygame.image.load(PLAYER_INITIAL_IMAGE_PATH)

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h, self.image)
        super().set_move_speed(PLAYER_MOVE_SPEED)