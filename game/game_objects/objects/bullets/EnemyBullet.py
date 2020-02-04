import pygame

from game_objects.Config import MAIN_PLAYER_BULLET_IMAGE_PATH, BULLET_WIDTH, BULLET_HEIGHT
from game_objects.objects.bullets.Bullet import Bullet


class EnemyBullet(Bullet):
    image = pygame.image.load(MAIN_PLAYER_BULLET_IMAGE_PATH)

    def fire(self):
        self.set_y(self.get_y() + 5)

    def __init__(self, x, y):
        super().__init__(x, y, BULLET_WIDTH, BULLET_HEIGHT, self.image)
        super().set_damage(10)