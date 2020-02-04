import pygame

from Controller import Controller
from game_objects.Config import *
from game_objects.players.Enemy import Enemy
from game_objects.objects.Screen import Screen
from game_objects.players.MainPlayer import MainPlayer

clock = pygame.time.Clock()
player = MainPlayer(PLAYER_START_X, PLAYER_START_Y, PLAYER_WIDTH, PLAYER_WIDTH)
enemy = Enemy(ENEMY_START_X, ENEMY_START_Y, ENEMY_WIDTH, ENEMY_HEIGHT)
screen = Screen(SCREEN_X, SCREEN_Y, SCREEN_WIDTH, SCREEN_HEIGHT)
controller = Controller(player)
#splash_screen = SplashScreen(screen)

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

    controller.get_action()

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pygame.display.flip()
