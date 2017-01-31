from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Line
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget
from math import sin, cos, sqrt, pi, acos
from kivy.graphics import Color, Ellipse
from kivy.core.text import Label as CoreLabel



        
class MyCircle(FloatLayout):

    def __init__(self, **kwargs):
        super(MyCircle, self).__init__(**kwargs)
        self.size = Window.size
        # root = self
        self.radius = 0.4 * min(self.size)
        print(self.radius)
        self.my_sin = 0
        self.my_cos = 0
        self.gangle = 0
        # my_label = CoreLabel()
        # my_label.text = "angle: {0}".format(self.gangle)
        # my_label.refresh()
        # hello_texture = my_label.texture
        self.gangle_label = Label(text="angle: {0}".format(self.gangle))
        self.sin_label = Label(text="sin: {0}".format(self.my_sin))
        self.cos_label = Label(text="cos: {0}".format(self.my_cos))
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
        cangle = x * r/(sqrt(x ** 2 + y ** 2) * sqrt(r ** 2))
        angle = acos(cangle)
        new_x = self.center_x + r * cangle
        self.gangle = 180/pi * angle
        if y > 0:
            new_y = self.center_y + r* sin(angle)

        else:
            new_y = self.center_y - r* sin(angle)
            self.gangle = 360 - self.gangle
        return new_x, new_y


    def show_values(self, x, y):
        x = x - self.center_x
        y = y - self.center_y
        r = self.radius
        self.my_sin = y / r  
        self.my_cos = x / r
        print("angle:",self.gangle)
        self.gangle_label.text = "angle: {0}".format(self.gangle);
        self.remove_widget(self.gangle_label)
        self.add_widget(self.gangle_label)
        self.gangle_label.pos = 10, 30
        self.cos_label.color = 1,1,1,0.5
        self.sin_label.text = "sin: {0}".format(self.my_sin);
        self.sin_label.pos = 10, 10
        self.sin_label.color = 0,1,0,0.5
        self.remove_widget(self.sin_label)
        self.add_widget(self.sin_label)
        self.cos_label.text = "cos: {0}".format(self.my_cos);
        self.cos_label.pos = 10, -10
        self.cos_label.color = 1,1,0,0.5
        
        self.remove_widget(self.cos_label)
        self.add_widget(self.cos_label)
        print("sin:",self.my_sin)
        print("cos:",self.my_cos)


    def main_changes(self, touch):
        self.canvas.clear();
        self.draw_axis()
        self.draw_main_circle();
        new_x, new_y = self.give_coords(touch)
        self.draw_lines(new_x, new_y)
        self.show_values(new_x, new_y)


    def on_touch_down(self, touch):
        self.main_changes(touch)


    def on_touch_move(self, touch):
        self.main_changes(touch)













class CircleApp(App):
    def build(self):
        return MyCircle()

if __name__ == '__main__':
    CircleApp().run()