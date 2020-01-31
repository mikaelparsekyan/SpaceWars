import pygame

from players.Enemy import Enemy
from players.MainPlayer import MainPlayer


class Screen:
    x = 0
    y = 0

    moveSpeed = 10

    width = 0
    height = 0

    color = (255, 255, 255)

    backgroundImage = pygame.image.load("res/background.jpg")

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, (self.width, self.height))

    def add_player(self, player, player_image):
        self.screen.blit(player_image, (player.get_x(), player.get_y()))

    def add_enemy_if_dead(self,enemy, enemy_image):#TODO organzing code
        if enemy.is_alive():
            self.screen.blit(enemy_image, (enemy.get_x(), enemy.get_y()))

    def add_bullet(self,bullet_x, bullet_y, bullet_image):
        self.screen.blit(bullet_image, (bullet_x, bullet_y))

    def move(self, backgroundY):
        rel_y = backgroundY % self.width
        self.screen.blit(self.backgroundImage, (0, rel_y - self.backgroundImage.get_rect().width))
        if rel_y < self.height:
            self.screen.blit(self.backgroundImage, (0, rel_y))