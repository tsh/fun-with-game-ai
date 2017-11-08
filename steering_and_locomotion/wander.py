from pygame.math import Vector2
from game import Game
from vehicle import WanderVehicle, BaseEntity

if __name__ == '__main__':
    g = Game('Simple seek')
    wanderer = WanderVehicle(location=Vector2(250, 250))
    g.game_objects.extend([wanderer])
    g.run()