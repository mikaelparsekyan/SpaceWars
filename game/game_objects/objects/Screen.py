import pygame

from game_objects.Config import SCREEN_BACKGROUND_IMAGE_PATH, SCREEN_MOVE_SPEED
from game_objects.GameObject import GameObject


class Screen(GameObject):
    backgroundImage = pygame.image.load(SCREEN_BACKGROUND_IMAGE_PATH)

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h, self.backgroundImage)
        self.screen = pygame.display.set_mode((super().get_width(), super().get_height()))
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, (self.width, self.height))

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def add_player(self, player, player_image):
        self.screen.blit(player_image, (player.get_x(), player.get_y()))

    def add_enemy_if_dead(self, enemy, enemy_image):  # TODO organzing code
        if enemy.is_alive():
            self.screen.blit(enemy_image, (enemy.get_x(), enemy.get_y()))

    def add_bullet(self, bullet_x, bullet_y, bullet_image):
        self.screen.blit(bullet_image, (bullet_x, bullet_y))

    def move(self, backgroundY):
        backgroundY -= SCREEN_MOVE_SPEED
        rel_y = backgroundY % self.width
        self.screen.blit(self.backgroundImage, (0, rel_y - self.backgroundImage.get_rect().width))
        if rel_y < self.height:
            self.screen.blit(self.backgroundImage, (0, rel_y))
