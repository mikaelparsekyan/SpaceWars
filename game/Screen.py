import pygame

from Player import Player

x = 0
y = 0

moveSpeed = 10

width = 500
height = 500

color = (255, 255, 255)

backgroundImage = pygame.image.load("res/background.jpg")
backgroundImage = pygame.transform.scale(backgroundImage, (width, height))

screen = pygame.display.set_mode((width, height))

player = Player(0, 0)


def add_player(player_x, player_y):
    screen.blit(player.get_img(), (player_x, player_y))


def move(backgroundY):
    rel_y = backgroundY % width
    screen.blit(backgroundImage, (0, rel_y - backgroundImage.get_rect().width))
    if rel_y < 500:
        screen.blit(backgroundImage, (0, rel_y))
    backgroundY += 8


#def shoot():

