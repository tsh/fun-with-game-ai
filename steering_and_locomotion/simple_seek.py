from pygame.math import Vector2
from game import Game
from vehicle import SimpleSeekVehicle, MovingEntity

if __name__ == '__main__':
    g = Game('Simple seek')
    ssv = SimpleSeekVehicle(Vector2(50, 50))
    target = MovingEntity(Vector2(300, 200))
    ssv.set_target(target)
    g.game_objects.extend([ssv, target])
    g.run()