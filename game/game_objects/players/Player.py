from abc import ABC

from game_objects.Config import SCREEN_HEIGHT, SCREEN_WIDTH, BULLET_SPLIT_LENGTH
from game_objects.GameObject import GameObject


class Player(GameObject):
    move_speed = None
    bullets = []
    health = 10
    shooting = False
    moving_left = False
    moving_right = False

    def __init__(self, x, y, w, h, img):
        super().__init__(x, y, w, h, img)

    def move_down(self):
        if self.get_y() < SCREEN_HEIGHT - self.height:
            self.set_y(self.get_y() + self.move_speed)

    def move_up(self):
        if self.get_y() >= 0:
            self.set_y(self.get_y() - self.move_speed)

    def move_left(self):
        if self.get_x() >= 0:
            self.moving_left = True
            self.moving_right = False
            self.set_x(self.get_x() - self.move_speed)

    def move_right(self):
        if self.x < SCREEN_WIDTH - self.width:
            self.moving_left = False
            self.moving_right = True
            self.set_x(self.get_x() + self.move_speed)

    def set_move_speed(self, move_speed):
        self.move_speed = move_speed

    def is_alive(self):
        return self.health > 0

    def take_life_points(self, damage):
        self.health -= damage

    def add_bullet(self, bullet):
        self.bullets.append(bullet)
        self.set_shooting(True)

    def get_bullets(self):
        return self.bullets

    def set_shooting(self, shooting):
        self.shooting = shooting

    def shoot(self,screen, enemy):
        #b_x = self.get_x() + (self.width / 2) - 4
        #b_y = self.get_y() - 20
        if self.shooting | len(self.get_bullets()) != 0:
            for bullet in self.get_bullets():
                self.shooting = True
                if bullet.get_x() in range(round(enemy.get_x()),
                                           round(enemy.get_x() + enemy.get_width())):
                    if bullet.get_y() == enemy.get_height():
                        enemy.take_life_points(bullet.damage)

                screen.add_bullet(bullet)
                bullet.fire()
                if bullet.get_y() <= 0:
                    print("removed")
                    self.set_shooting(False)
                    self.get_bullets().remove(bullet)
                elif bullet.get_y() <= self.get_y() - BULLET_SPLIT_LENGTH:
                    self.set_shooting(False)