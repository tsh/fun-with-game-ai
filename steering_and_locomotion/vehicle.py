from kivy.vector import Vector
from kivy.graphics import Canvas, Rectangle

class Vehicle():
    def __init__(self):
        self.location = Vector(5, 15)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.max_speed = 10
        self.max_force = 0.1


    def update(self, dt):
        self.velocity += self.acceleration
        self.location += self.velocity * dt

    def render(self, canvas: Canvas):
        canvas.add(Rectangle(pos=self.location, size=(50, 50)))