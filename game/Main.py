from random import random

import pygame
from pygame import key
from pygame.constants import K_DOWN, K_UP, K_LEFT, K_RIGHT

from players.Enemy import Enemy
from Screen import Screen
from players.MainPlayer import MainPlayer

FPS = 100
screenWidth = 500
screenHeight = 500
backgroundY = 0

clock = pygame.time.Clock()

screenColor = (255, 255, 255)

player = MainPlayer(100, 100)
enemy = Enemy(0, 400)

playerSpeed = player.moveSpeed

pygame.init()
pygame.display.set_caption("PyGame")

screen = Screen(500, 500)

done = False

while not done:
    clock.tick(FPS)
    print(round(random() * 100))
    backgroundY += 4
    screen.move(backgroundY)
    screen.add_enemy_if_dead(enemy.is_alive(), round(random() * screenWidth), 0)
    screen.add_player(player.get_x(), player.get_y())

    keys = key.get_pressed()
    if keys[K_DOWN]:
        player.move_down(screenHeight)
    if keys[K_UP]:
        player.move_up()
    if keys[K_LEFT]:
        player.move_left()
    if keys[K_RIGHT]:
        player.move_right(screenWidth)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pygame.display.flip()
