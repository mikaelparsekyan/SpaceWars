import random

import pygame

from game_objects.Config import ENEMY_MOVE_SPEED, SCREEN_WIDTH, BULLET_SPLIT_LENGTH, SCREEN_HEIGHT
from game_objects.objects.bullets.EnemyBullet import EnemyBullet
from game_objects.players.Player import Player


class Enemy(Player):
    left_stop = 0
    right_stop = 0
    bullets = []

    image = pygame.image.load("res/images/enemy.png")
    destroyed_image = pygame.image.load("res/images/dead.png")

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h, self.image)
        super().set_move_speed(ENEMY_MOVE_SPEED)
        self.destroyed_image = pygame.transform.scale(self.destroyed_image, (super().get_width(), super().get_height()))

    def move(self, player):
        if self.get_x() in range(round(player.get_x() - 40), round(player.get_x() + 80)):
            if not self.shooting:
                bullet = EnemyBullet(self.get_x(), self.get_y())
                self.add_bullet(bullet)

        if self.moving_left:
            if self.left_stop < 0:
                self.left_stop = 0
            super().move_left()
            if super().get_x() <= self.left_stop:
                if self.get_x() < player.get_x() + 30 + 100:
                    self.right_stop = round(random.randrange(player.get_x(), player.get_x() + 30 + 100, 10))

                self.moving_left = False
                self.moving_right = True
        else:
            if self.right_stop > SCREEN_WIDTH:
                self.right_stop = SCREEN_WIDTH
            super().move_right()
            if super().get_x() >= self.right_stop - self.width:
                if player.get_x() - 70 < self.get_x():
                    self.left_stop = round(random.randrange(player.get_x() - 70, player.get_x(),
                                                            10))  # TODO fix the problem with range (0, 0 - 40)????
                self.moving_left = True
                self.moving_right = False

    def shoot(self,screen, player): #TODO move it to PLAYER.py (polymorphism)
        #b_x = self.get_x() + (self.width / 2) - 4
        #b_y = self.get_y() - 20
        if self.shooting | len(self.get_bullets()) != 0:
            for bullet in self.get_bullets():
                self.shooting = True
                if bullet.get_x() in range(round(player.get_x()),
                                           round(player.get_x() + player.get_width())):
                    if bullet.get_y() == player.get_height():
                        player.take_life_points(bullet.damage)

                screen.add_bullet(bullet)
                bullet.fire()
                if bullet.get_y() > SCREEN_HEIGHT:
                    print("removed")
                    self.set_shooting(False)
                    self.get_bullets().remove(bullet)
                elif bullet.get_y() > self.get_y() + 140:
                    self.set_shooting(False)