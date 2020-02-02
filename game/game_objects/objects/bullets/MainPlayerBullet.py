import pygame

from game_objects.Config import *
from game_objects.objects.bullets.Bullet import Bullet


class MainPlayerBullet(Bullet):

    image = pygame.image.load(MAIN_PLAYER_BULLET_IMAGE_PATH)

    def __init__(self, x, y):
        super().__init__(x, y, BULLET_WIDTH, BULLET_HEIGHT, self.image)
        super().set_damage(MAIN_PLAYER_BULLET_DAMAGE)
