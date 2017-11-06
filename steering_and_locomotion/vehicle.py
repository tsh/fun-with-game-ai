from pygame.math import Vector2
from pygame import Rect, draw
from pygame.locals import Color


class BaseEntity(object):
    def __init__(self, location):
        self.location = location

    def render(self, surface):
        draw.circle(surface, Color("green"), (int(self.location.x), int(self.location.y)), 10)


class MovingEntity(BaseEntity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocity = Vector2(1, 1)
        self.acceleration = Vector2(0, 0)
        self.max_speed = 2
        self.max_force = 0.1
        self.target_pos = None

    def set_target(self, target):
        self.target_pos = target.location

    def seek(self, target):
        target_loc = target.location
        desired_velocity = (target_loc - self.location).normalize() * self.max_speed
        steer = desired_velocity - self.velocity
        self.location += steer

    def flee(self, target):
        target_pos = target.location
        desired_velocity = (self.location - target_pos).normalize() * self.max_speed
        steer = desired_velocity - self.velocity
        self.location += steer

    def update(self, dt=None):
        # self.seek(self.target)
        # self.velocity += self.acceleration
        # self.location += self.velocity * dt
        pass


class SimpleSeekVehicle(MovingEntity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.action = self.simple_seek

    def simple_seek(self):
        return (self.target_pos - self.location).normalize()

    def update(self):
        self.location += self.simple_seek()