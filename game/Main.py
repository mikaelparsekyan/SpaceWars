import pygame
from pygame import key
from pygame.constants import K_DOWN, K_UP, K_LEFT, K_RIGHT, K_SPACE

from game_objects.Config import *
from game_objects.objects.Bullet import Bullet
from game_objects.players.Enemy import Enemy
from game_objects.objects.Screen import Screen
from game_objects.players.MainPlayer import MainPlayer

FPS = 100
backgroundY = 0

clock = pygame.time.Clock()

screenColor = (255, 255, 255)

player = MainPlayer(0, 0, 100, 100)
enemy = Enemy(200, 0)

playerSpeed = player.moveSpeed

pygame.init()
pygame.display.set_caption("Space Wars")

destroyed_image = pygame.image.load("res/dead.png")

screen = Screen(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
bullets = []

done = False
firing = False

while not done:
    clock.tick(FPS)
    backgroundY += 4
    screen.move(backgroundY)
    enemy.move(player, SCREEN_WIDTH)
    screen.add_enemy_if_dead(enemy, enemy.get_img())
    screen.add_player(player, player.get_img())

    if firing | len(bullets) != 0:  # TODO move to bullet.py
        for bullet in bullets:
            firing = True
            if bullet.get_x() in range(round(enemy.get_x() - enemy.get_width() / 2),
                                       round(enemy.get_x() + enemy.get_width() / 2)):
                if bullet.get_y() == 60:
                    enemy.take_life_points(bullet.damage)
                    if not enemy.is_alive():
                        enemy.set_img(destroyed_image)

            screen.add_bullet(bullet.get_x(), bullet.get_y(), bullet.image)
            bullet.set_y(bullet.get_y() - 5)
            if bullet.get_y() <= 0:
                print("removed")
                firing = False
                bullets.remove(bullet)
            elif bullet.get_y() <= player.get_y() - 90:
                firing = False
    keys = key.get_pressed()
    if keys[K_DOWN]:
        player.move_down(SCREEN_HEIGHT)
    if keys[K_UP]:
        player.move_up()
    if keys[K_LEFT]:
        player.move_left()
    if keys[K_RIGHT]:
        player.move_right(SCREEN_WIDTH)
    if keys[K_SPACE]:
        if not firing:
            bullet = Bullet(player.get_x(), player.get_y())
            bullets.append(bullet)
            print(len(bullets))
            firing = True
        # player.shoot(screen, bullet)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pygame.display.flip()
