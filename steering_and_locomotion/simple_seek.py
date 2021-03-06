from pygame.math import Vector2
from game import Game
from vehicle import SimpleSeekVehicle, BaseEntity

if __name__ == '__main__':
    g = Game('Simple seek')
    ssv = SimpleSeekVehicle(location=Vector2(50, 50))
    target = BaseEntity(Vector2(300, 200))
    ssv.set_target(target)
    g.game_objects.extend([ssv, target])
    g.run()