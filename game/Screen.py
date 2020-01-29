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

    player = MainPlayer(0, 0)
    enemy = Enemy(0, 0)

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, (self.width, self.height))

    def add_player(self, player_x, player_y):
        self.screen.blit(self.player.get_img(), (player_x, player_y))

    def add_enemy_if_dead(self,e, enemy_x, enemy_y):
        self.screen.blit(self.enemy.get_img(), (enemy_x, enemy_y))

    def move(self, backgroundY):
        rel_y = backgroundY % self.width
        self.screen.blit(self.backgroundImage, (0, rel_y - self.backgroundImage.get_rect().width))
        if rel_y < self.height:
            self.screen.blit(self.backgroundImage, (0, rel_y))
        backgroundY += 8



