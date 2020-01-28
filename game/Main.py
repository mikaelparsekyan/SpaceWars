import pygame
from pygame import key
from pygame.constants import K_DOWN, K_UP, K_LEFT, K_RIGHT

import Player
import Screen

FPS = 100
screenWidth = 500
screenHeight = 500
backgroundY = 0

clock = pygame.time.Clock()

screenColor = (255, 255, 255)

playerX = Player.x
playerY = Player.y

playerSpeed = Player.moveSpeed

pygame.init()
pygame.display.set_caption("PyGame")

screen = Screen

done = False


def move_down(playerY):
    if playerY < screenHeight - Player.height:
        playerY += playerSpeed
    return playerY


def move_up(playerY):
    if playerY >= 0:
        playerY -= playerSpeed
    return playerY


def move_left(playerX):
    if playerX >= 0:
        playerX -= playerSpeed
    return playerX


def move_right(playerX):
    if playerX < screenWidth - Player.width:
        playerX -= playerSpeed
    return playerX


while not done:
    clock.tick(FPS)

    backgroundY += 5
    screen.move(backgroundY)
    screen.add_player(playerX, playerY)

    keys = key.get_pressed()
    if keys[K_DOWN]:
        playerY = move_down(playerY)
    if keys[K_UP]:
        playerY = move_up(playerY)
    if keys[K_LEFT]:
        playerX = move_left(playerX)
    if keys[K_RIGHT]:
        playerX = move_down(playerX)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pygame.display.flip()
