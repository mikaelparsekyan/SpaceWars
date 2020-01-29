import pygame
from pygame import key
from pygame.constants import K_DOWN, K_UP, K_LEFT, K_RIGHT

import Screen
from Player import Player

FPS = 100
screenWidth = 500
screenHeight = 500
backgroundY = 0

clock = pygame.time.Clock()

screenColor = (255, 255, 255)

player = Player(100, 100)

playerSpeed = player.moveSpeed

pygame.init()
pygame.display.set_caption("PyGame")

screen = Screen#TODO

done = False


def move_down():
    if player.get_y() < screenHeight - Player.height:
        player.set_y(player.get_y() + playerSpeed)


def move_up():
    if player.get_y() >= 0:
        player.set_y(player.get_y() - playerSpeed)


def move_left():
    if player.get_x() >= 0:
        player.set_x(player.get_x() - playerSpeed)


def move_right():
    if player.get_x() < screenWidth - Player.width:
        player.set_x(player.get_x() + playerSpeed)


while not done:
    clock.tick(FPS)

    backgroundY += 5
    screen.move(backgroundY)
    screen.add_player(player.get_x(), player.get_y())

    keys = key.get_pressed()
    if keys[K_DOWN]:
        move_down()
    if keys[K_UP]:
        move_up()
    if keys[K_LEFT]:
        move_left()
    if keys[K_RIGHT]:
        move_right()

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pygame.display.flip()
