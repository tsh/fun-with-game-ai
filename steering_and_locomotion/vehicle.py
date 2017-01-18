from kivy.vector import Vector
from kivy.graphics import Canvas, Rectangle

class Vehicle():
    def __init__(self):
        self.position = Vector(5, 15)


    def update(self, dt):
        self.position += dt

    def render(self, canvas: Canvas):
        canvas.add(Rectangle(pos=self.position, size=(50, 50)))