from abc import ABC

from game_objects.GameObject import GameObject


class Bullet(GameObject):
    damage = 0

    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)

    def set_damage(self, damage):
        self.damage = damage

    def fire(self):
        self.set_y(self.get_y() - 5)


