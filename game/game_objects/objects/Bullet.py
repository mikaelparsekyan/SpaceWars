import pygame


class Bullet:

    x = 0
    y = 0
    damage = 5

    image = pygame.image.load("res/fire.png")
    image = pygame.transform.scale(image, (10,20))

    def __init__(self, b_x, b_y):
        self.x = b_x
        self.y = b_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_y(self, b_y):
        self.y = b_y

    def set_x(self, b_x):
        self.x = b_x