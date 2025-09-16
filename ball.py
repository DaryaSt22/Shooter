import pygame
from constants import BALL_STEP


class Ball:
    def __init__(self, fighter):
        self.image = pygame.image.load('images/rocket.png')
        self.width, self.height = self.image.get_size()
        self.x, self.y = 0, 0
        self.stop = BALL_STEP
        self.was_fired = False
        self.fighter = fighter
