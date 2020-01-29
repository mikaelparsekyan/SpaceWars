import pygame

class Player:
    x = 0
    y = 0

    width = 60
    height = 60

    moveSpeed = 5

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

    def move_down(self, screen_height):
        if self.get_y() < screen_height - self.height:
            self.set_y(self.get_y() + self.moveSpeed)

    def move_up(self):
        if self.get_y() >= 0:
            self.set_y(self.get_y() - self.moveSpeed)

    def move_left(self):
        if self.get_x() >= 0:
            self.set_x(self.get_x() - self.moveSpeed)

    def move_right(self, screen_width):
        if self.x < screen_width - self.width:
            self.set_x(self.get_x() + self.moveSpeed)
