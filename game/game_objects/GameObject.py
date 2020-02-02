from abc import ABC, abstractmethod


class GameObject(ABC):
    x = 0
    y = 0

    width = 0
    height = 0

    image = None

    def __init__(self, x, y, width, height, img):
        self.set_x(x)
        self.set_y(y)
        self.set_width(width)
        self.set_height(height)
        self.image = img

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
