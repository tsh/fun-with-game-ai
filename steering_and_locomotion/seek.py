import sys
import pygame
from pygame.math import Vector2
from pygame import Rect, display
from pygame.locals import QUIT, Color

from vehicle import Vehicle


if __name__ == '__main__':
    pygame.init()

    #Set up the window
    windowSurface = pygame.display.set_mode((620, 480), 0, 32)
    pygame.display.set_caption('Steering and locomotion')

    dummy_vehicle = Vehicle(Vector2(450, 50))
    vehicle = Vehicle(Vector2(50, 50))
    target = Vehicle(Vector2(300, 200))

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        dummy_vehicle.render(windowSurface)
        vehicle.render(windowSurface)
        target.render(windowSurface)
        vehicle.seek(target)
        dummy_vehicle.simple_seek(target)

        display.update()
        windowSurface.fill(Color('black'))

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()