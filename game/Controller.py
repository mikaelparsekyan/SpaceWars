from pygame import key
from pygame.constants import K_DOWN, K_UP, K_LEFT, K_RIGHT, K_SPACE

from game_objects.objects.bullets.MainPlayerBullet import MainPlayerBullet


class Controller():
    player = None

    def __init__(self, player):
        self.player = player

    def get_action(self):
        #if self.player.is_alive():
            keys = key.get_pressed()
            if keys[K_DOWN]:
                self.player.move_down()
            if keys[K_UP]:
                self.player.move_up()
            if keys[K_LEFT]:
                self.player.move_left()
            if keys[K_RIGHT]:
                self.player.move_right()
            if keys[K_SPACE]:
                if not self.player.shooting:
                    bullet = MainPlayerBullet(self.player.get_x(), self.player.get_y())
                    self.player.add_bullet(bullet)