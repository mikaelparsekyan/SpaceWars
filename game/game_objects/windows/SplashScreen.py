import time

import pygame
pygame.init()

class SplashScreen():
    def __init__(self, screen):
        text = str("splashhhh")
        font = pygame.font.SysFont('arial', 200)
        text = font.render(text, True, (255,0,0))

        try:
            screen.screen.blit(text, (12, 12))
            time.sleep(1.5)
        except InterruptedError:
            print("asd")
