# to run the application
from kivy.uix.widget import Widget
from kivy.core.window import Window
# animation
from kivy.clock import Clock
from kivy.animation import Animation
# import kivy properties
from kivy.properties import NumericProperty

# import classes
from anim_rectangle import *


class AnimBall(Widget):
    r = NumericProperty(0)
    g = NumericProperty(0)
    b = NumericProperty(1)

    def __init__(self, **kwargs):
        super(AnimBall, self).__init__(**kwargs)    
        size = Window.width / 50 + Window.height / 50
        self.width = size
        self.height = size
        self.x = (Window.width / 2 - self.width / 2)
        self.y = (Window.height / 5 - self.height / 2)     
        color = RandomColor()
        self.r, self.g, self.b = color.update_color()
        self.add_rectangles(10)

    def on_touch_down(self, *args):
        initial_y = Window.height / 5 - self.height / 2
        initial_x = (Window.width / 2 - self.width / 2)
        y = Window.height / 10 + self.y
        max_y = 2*Window.height - self.height / 2
        if self.y + y < max_y:
            Animation.cancel_all(self)
            animation = Animation(x=initial_x, y=y, duration=0.3, t='out_cubic')
            animation += Animation(x=initial_x, y=initial_y, duration=0.3, t='in_cubic')
            animation.start(self)

    def add_rectangles(self, nb_rectangles):
        # add nb rectangles
        self.add_widget(ClockRect())

# It's here the file to modify for the ex_4

    # 1 the objective is to modify add_rectangles to add multiple rectangles
        # use a loop: for
        # use range()
