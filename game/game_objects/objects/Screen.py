import pygame

from game_objects.Config import SCREEN_BACKGROUND_IMAGE_PATH, SCREEN_MOVE_SPEED
from game_objects.GameObject import GameObject


class Screen(GameObject):
    image = pygame.image.load(SCREEN_BACKGROUND_IMAGE_PATH)

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h, self.image)
        self.screen = pygame.display.set_mode((super().get_width(), super().get_height()))

    def add_player(self, player):
        self.screen.blit(player.get_img(), (player.get_x(), player.get_y()))

    def add_enemy(self, enemy):
        if enemy.is_alive():
            self.screen.blit(enemy.get_img(), (enemy.get_x(), enemy.get_y()))

    def add_bullet(self, bullet):
        self.screen.blit(bullet.get_img(), (bullet.get_x(), bullet.get_y()))

    def move(self):
        self.set_y(self.get_y() + SCREEN_MOVE_SPEED)
        rel_y = self.get_y() % self.height
        self.screen.blit(self.image, (0, rel_y - self.image.get_rect().height))
        if rel_y < self.height:
            self.screen.blit(self.image, (0, rel_y))
