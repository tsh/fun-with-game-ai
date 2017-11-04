from pygame.math import Vector2
from pygame import Rect, draw
from pygame.locals import Color

class Vehicle():
    def __init__(self, location):
        self.location = location
        self.velocity = Vector2(1, 1)
        self.acceleration = Vector2(0, 0)
        self.max_speed = 2
        self.max_force = 0.1

    def update(self, dt):
        # self.seek(self.target)
        # self.velocity += self.acceleration
        # self.location += self.velocity * dt
        pass

    def render(self, surface):
        draw.circle(surface, Color("green"), (int(self.location.x), int(self.location.y)), 10)

    def seek(self, target):
        target_loc = target.location
        desired_velocity = (target_loc - self.location).normalize() * self.max_speed
        steer = desired_velocity - self.velocity
        self.location += steer

    def simple_seek(self, target):
        target_loc = target.location
        self.location += (target_loc - self.location).normalize()