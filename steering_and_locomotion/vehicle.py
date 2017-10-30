from pygame.math import Vector2
from pygame import Rect, draw
from pygame.locals import Color

class Vehicle():
    def __init__(self):
        self.location = Vector2(5, 15)
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.max_speed = 10
        self.max_force = 0.1


    def update(self, dt):
        # self.seek(self.target)
        # self.velocity += self.acceleration
        # self.location += self.velocity * dt
        pass

    def render(self, surface):
        # canvas.add(Rect(pos=self.location, size=(50, 50)))
        draw.circle(surface, Color("green"), (10,10), 50)

    def seek(self, target):
        desired = (target - self.location).normalize() * self.max_speed
        steer = desired - self.velocity
        self.acceleration += steer