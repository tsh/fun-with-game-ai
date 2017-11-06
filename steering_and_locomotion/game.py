import sys
import pygame
from pygame.math import Vector2
from pygame import Rect, display
from pygame.locals import QUIT, Color


class Game(object):
    def __init__(self, title):
        pygame.init()
        pygame.display.set_caption(title)
        self.canvas = pygame.display.set_mode((620, 480), 0, 32)
        self.game_objects = []

    def run(self):
        clock = pygame.time.Clock()
        while True:
            dt = clock.tick(60)
            for gobj in self.game_objects:
                gobj.update()
                gobj.render(self.canvas)

            display.update()
            self.canvas.fill(Color('black'))

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()