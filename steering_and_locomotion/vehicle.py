from pygame.math import Vector2
from pygame import Rect, draw
from pygame.locals import Color


class BaseEntity(object):
    def __init__(self, location):
        self.location = location

    def render(self, surface):
        draw.circle(surface, Color("green"), (int(self.location.x), int(self.location.y)), 10)

    def update(self, dt=None):
        pass


class MovingEntity(BaseEntity):
    def __init__(self, velocity=Vector2(0, 0), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocity = velocity
        self.acceleration = Vector2(0, 0)
        self.max_speed = 2
        self.max_force = 0.1
        self.target_pos = None

    def set_target(self, target):
        self.target_pos = target.location

    def simple_seek(self):
        return (self.target_pos - self.location).normalize()

    def seek(self):
        desired_velocity = (self.target_pos - self.location).normalize() * self.max_speed
        steer = desired_velocity - self.velocity
        return steer

    def flee(self):
        desired_velocity = (self.location - self.target_pos).normalize() * self.max_speed
        steer = desired_velocity - self.velocity
        return steer

    def update(self, dt=None):
        # self.seek(self.target)
        # self.velocity += self.acceleration
        # self.location += self.velocity * dt
        self.location += self.action()


class SimpleSeekVehicle(MovingEntity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.action = self.simple_seek


class SeekVehicle(MovingEntity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.action = self.seek


class FleeVehicle(MovingEntity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.action = self.flee
