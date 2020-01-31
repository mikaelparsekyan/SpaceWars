from random import random

import pygame
from pygame import key
from pygame.constants import K_DOWN, K_UP, K_LEFT, K_RIGHT, K_SPACE

from Bullet import Bullet
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
enemy = Enemy(200, 0)

playerSpeed = player.moveSpeed

pygame.init()
pygame.display.set_caption("Space Wars")

screen = Screen(500, 500)
bullets = []

done = False
firing = False

while not done:
    clock.tick(FPS)
    backgroundY += 4
    screen.move(backgroundY)
    enemy.move(screenWidth)
    screen.add_enemy_if_dead(enemy, enemy.get_x(), enemy.get_y(), enemy.get_img())
    screen.add_player(player.get_x(), player.get_y(), player.get_img())

    if firing:
        assign = False
        for bullet in bullets:
            screen.add_bullet(bullet.get_x(), bullet.get_y(), bullet.image)
            bullet.set_y(bullet.get_y() - 5)
            if bullet.get_y() <= 0:
                bullet.set_y(300)
                bullets.remove(bullet)
                firing = False

    keys = key.get_pressed()
    if keys[K_DOWN]:
        player.move_down(screenHeight)
    if keys[K_UP]:
        player.move_up()
    if keys[K_LEFT]:
        player.move_left()
    if keys[K_RIGHT]:
        player.move_right(screenWidth)
    if keys[K_SPACE]:
        if not firing:
            bullet = Bullet(player.get_x(), player.get_y())
            bullet.set_x(player.get_x())
            bullet.set_y(player.get_y())
            bullets.append(bullet)
            firing = True
        #player.shoot(screen, bullet)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pygame.display.flip()
