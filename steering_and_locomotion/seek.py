from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.vector import Vector

from vehicle import Vehicle


class SeekWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.seeker = Vehicle()
        self.target = Vector(400, 100)

    def on_touch_down(self, touch):
        self.canvas.add(Rectangle(size=(50, 50)))

    def update(self, dt):
        self.canvas.add(Ellipse(pos=(self.target), size=(10, 10)))
        desired = (self.target - self.seeker.location).normalize() * self.seeker.max_speed
        steer = desired - self.seeker.velocity
        self.seeker.acceleration += steer
        self.seeker.update(dt)
        self.seeker.render(self.canvas)


class MyPaintApp(App):

    def build(self):
        game = SeekWidget()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    MyPaintApp().run()