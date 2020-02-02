from abc import ABC

from game_objects.GameObject import GameObject


class Player(GameObject):
    moveSpeed = 5
    bullets = []

    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)

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

    def shoot(self, screen, bullet):
        b_x = self.get_x() + (self.width / 2) - 4
        b_y = self.get_y() - 20
        screen.add_bullet(bullet.get_x(), bullet.get_y(), bullet.image)
        bullet.set_y(bullet.get_y() - 5)
        if bullet.get_y() > 0:
            self.shoot(screen, bullet)
        self.bullets.append(bullet)
