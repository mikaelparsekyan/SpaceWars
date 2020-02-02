import pygame
from pygame import key
from pygame.constants import K_DOWN, K_UP, K_LEFT, K_RIGHT, K_SPACE

from game_objects.Config import *
from game_objects.objects.bullets.MainPlayerBullet import MainPlayerBullet
from game_objects.players.Enemy import Enemy
from game_objects.objects.Screen import Screen
from game_objects.players.MainPlayer import MainPlayer

clock = pygame.time.Clock()
player = MainPlayer(PLAYER_START_X, PLAYER_START_Y, PLAYER_WIDTH, PLAYER_WIDTH)
enemy = Enemy(ENEMY_START_X, ENEMY_START_Y, ENEMY_WIDTH, ENEMY_HEIGHT)
screen = Screen(SCREEN_X, SCREEN_Y, SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()
pygame.display.set_caption(GAME_TITLE)

done = False
firing = False
while not done:
    clock.tick(FPS)

    screen.move()
    enemy.move(player)
    screen.add_enemy(enemy)
    screen.add_player(player)

    player.shoot(screen, enemy)

    keys = key.get_pressed()
    if keys[K_DOWN]:
        player.move_down()
    if keys[K_UP]:
        player.move_up()
    if keys[K_LEFT]:
        player.move_left()
    if keys[K_RIGHT]:
        player.move_right()
    if keys[K_SPACE]:
        if not player.shooting:
            bullet = MainPlayerBullet(player.get_x(), player.get_y())
            player.add_bullet(bullet)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pygame.display.flip()
