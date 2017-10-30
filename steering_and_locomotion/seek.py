import sys
import pygame
from pygame import Rect, display
from pygame.locals import QUIT

from vehicle import Vehicle


class SeekWidget():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.target = Vector(400, 100)
        self.seeker = Vehicle(self.target)
        self.seeker.target = self.target
        self.canvas.add(Ellipse(pos=(self.target), size=(10, 10)))

    def on_touch_down(self, touch):
        self.canvas.add(Rectangle(size=(50, 50)))

    def update(self, dt):
        self.seeker.update(dt)
        self.seeker.render(self.canvas)


class MyPaintApp():

    def build(self):
        game = SeekWidget()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    pygame.init()

    #Set up the window
    windowSurface = pygame.display.set_mode((620, 480), 0, 32)
    pygame.display.set_caption('Steering and locomotion')

    vh = Vehicle()

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        vh.render(windowSurface)
        display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()