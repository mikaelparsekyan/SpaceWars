import pygame


class Player:
    x = 0
    y = 0

    width = 60
    height = 60

    moveSpeed = 5

    image = pygame.image.load("res/player.png")
    image = pygame.transform.scale(image, (width, height))

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_img(self):
        return self.image
