import pygame

from game_objects.Config import SCREEN_BACKGROUND_IMAGE_PATH, SCREEN_MOVE_SPEED
from game_objects.GameObject import GameObject


class Screen(GameObject):
    image = pygame.image.load(SCREEN_BACKGROUND_IMAGE_PATH)
    l_imgs = [pygame.image.load('res/images/p2.png'), pygame.image.load('res/images/p1.png'),
              pygame.image.load('res/images/p0.png')]
    r_imgs = [pygame.image.load('res/images/p5.png'), pygame.image.load('res/images/p6.png'),
              pygame.image.load('res/images/p7.png')]
    s_imgs = [pygame.image.load('res/images/p4.png'),pygame.image.load('res/images/p3.png'), pygame.image.load('res/images/p4.png')]
    moving_counter = 0
    standing_counter = 0

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h, self.image)
        self.screen = pygame.display.set_mode((super().get_width(), super().get_height()))

    def add_player(self, player):
        if self.moving_counter > 8:
            self.moving_counter = 8

        if player.moving_left:
            self.set_mn_pl_img(self.moving_counter // 4, self.l_imgs, player)
            self.moving_counter += 1

            player.moving_left = False
        elif player.moving_right:
            self.set_mn_pl_img(self.moving_counter // 4, self.r_imgs, player)
            self.moving_counter += 1

            player.moving_right = False
        else:
            self.moving_counter = 0

            self.standing_counter += 1
            if self.standing_counter > 2:
                self.standing_counter = 0

            print("asd", self.standing_counter)
            self.set_mn_pl_img(self.standing_counter // 2, self.s_imgs, player)

            # self.set_mn_pl_img(self.moving_counter // 4, self.r_imgs)
            #self.screen.blit(player.get_img(), (player.get_x(), player.get_y()))

    def set_mn_pl_img(self, index, imgs, player):
        imgs[index] = pygame.transform.scale(imgs[index],(120,120))
        self.screen.blit(imgs[index], (player.get_x(), player.get_y()))

    def add_enemy(self, enemy):
        if enemy.is_alive():
            self.screen.blit(enemy.get_img(), (enemy.get_x(), enemy.get_y()))

    def add_bullet(self, bullet):
        self.screen.blit(bullet.get_img(), (bullet.get_x(), bullet.get_y()))

    def add_text(self, text):
        pygame.font.init()
        font = pygame.font.Font('res/fonts/Roboto-Thin.ttf', 40)
        text = font.render(text, True, (245, 245, 245))
        self.screen.blit(text, (15, 15))

    def move(self):
        self.set_y(self.get_y() + SCREEN_MOVE_SPEED)
        rel_y = self.get_y() % self.height
        self.screen.blit(self.image, (0, rel_y - self.image.get_rect().height))
        if rel_y < self.height:
            self.screen.blit(self.image, (0, rel_y))
