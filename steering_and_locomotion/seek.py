from pygame.math import Vector2
from game import Game
from vehicle import SeekVehicle, BaseEntity

if __name__ == '__main__':
    g = Game('Simple seek')
    sv = SeekVehicle(location=Vector2(20, 0))
    target = BaseEntity(Vector2(400, 400))
    sv.set_target(target)
    g.game_objects.extend([sv, target])
    g.run()