from pygame.math import Vector2
from game import Game
from vehicle import Vehicle

if __name__ == '__main__':
    g = Game('Simple seek')
    vh = Vehicle(Vector2(50, 50))
    target = Vehicle(Vector2(300, 200))
    g.game_objects.extend([vh, target])
    g.run()