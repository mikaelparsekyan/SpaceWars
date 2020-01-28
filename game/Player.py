import pygame

x = 100
y = 100

width = 60
height = 60

moveSpeed = 5

image = pygame.image.load("res/player.png")
image = pygame.transform.scale(image, (width, height))
