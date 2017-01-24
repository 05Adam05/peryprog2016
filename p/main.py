from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Line
from kivy.uix.label import Label
from kivy.core.window import Window
from math import sin, cos, sqrt, radians

class MyCircle(FloatLayout):
    def __init__(self, **kwargs):
        super(MyCircle, self).__init__(**kwargs)
        self.size = Window.size
        root = self
        radius = 100


        with self.canvas:
             Line(circle = (self.center_x, self.center_y, radius), width = 2)
             for a in range(0,361,10):
                alpha = radians(a);
                Line(circle = (self.center_x + radius * cos(alpha) ,self.center_y+radius * sin(alpha), 2), width = 2)

           
class Test1App(App):
    def build(self):
        return MyCircle()

if __name__ == '__main__':
    Test1App().run()