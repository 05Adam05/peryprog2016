from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Line
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget
from math import sin, cos, sqrt, pi, acos
from kivy.graphics import Color, Ellipse

class MyLine(Widget):
    pass

        


class MyCircle(Widget):
    def __init__(self, **kwargs):
        super(MyCircle, self).__init__(**kwargs)
        self.main_line =  MyLine()
        self.size = Window.size
        root = self
        self.radius = 0.4 * min(self.size)
        print(self.radius)

        self.draw_axis()
        self.draw_main_circle()

    def draw_axis(self):
        with self.canvas:
            Line(points=[self.center_x, 0, self.center_x, self.height], width=1)
            Line(points=[0, self.center_y, self.width, self.center_y], width=1) 

    
    def draw_main_circle(self):
        with self.canvas:
            Line(circle = (self.center_x, self.center_y, self.radius), width = 2)
            for a in range(0,361,10):
                alpha = pi/180*a;
                Line(circle = (self.center_x + self.radius * cos(alpha),
                    self.center_y + self.radius * sin(alpha), 2), width = 2)



    def draw_lines(self, x, y):
        with self.canvas:
            Color(1,0,0)
            Line(points=[self.center_x, self.center_y, x, y], width=1)
            Color(1,1,0)
            Line(points=[self.center_x, y, x, y], width=1)
            Line(points=[self.center_x, self.center_y, x, self.center_y], width=1)
            Color(0,1,0)
            Line(points=[x, self.center_y, x, y], width=1)
            Line(points=[self.center_x, self.center_y, self.center_x, y], width=1)

    def give_coords(self,touch):
        x = touch.x - self.center_x
        y = touch.y - self.center_y
        r = self.radius
        # print(touch.x, touch.y)
        # print(x, y, r)
        cangle = x * r/(sqrt(x ** 2 + y ** 2) * sqrt(r ** 2))
        # print(cangle)
        angle = acos(cangle)
        new_x = self.center_x + r * cangle
        self.gangle = 180/pi * angle
        if y > 0:
            new_y = self.center_y + r* sin(angle)

        else:
            new_y = self.center_y - r* sin(angle)
            self.gangle = 360 - self.gangle
        # new_x = touch.x
        # new_y = touch.y
        return new_x, new_y

    def show_values(self, x, y):
       
        x = x - self.center_x
        y = y - self.center_y
        r = self.radius
        # print(x, y, r)
        my_sin = y / r  
        my_cos = x / r
        print("angle:",self.gangle)
        print("sin:",my_sin)
        print("cos:",my_cos)

    def on_touch_down(self, touch):
        self.canvas.clear();
        self.draw_axis()
        self.draw_main_circle();
        new_x, new_y = self.give_coords(touch)
        self.draw_lines(new_x, new_y)
        self.show_values(new_x, new_y)








class Test1App(App):
    def build(self):
        return MyCircle()

if __name__ == '__main__':
    Test1App().run()