# to run the application
from kivy.uix.widget import Widget
from kivy.core.window import Window
# import kivy properties
from kivy.properties import NumericProperty
from kivy.properties import ListProperty

# import classes
from utils import *


class ClockRect(Widget):
    velocity = ListProperty([10, 15])
    r = NumericProperty(0)
    g = NumericProperty(0)
    b = NumericProperty(1)
    s = NumericProperty(100)

    def __init__(self, **kwargs):
        super(ClockRect, self).__init__(**kwargs)
        size = min(Window.height, Window.width)  
        self.s = random.randint(size / 40, size / 5)
        self.x = Window.width / 2 - self.width / 2
        self.y = 5 * Window.height / 6 - self.height / 2
        self.velocity = [random.choice([-1, 1]) * random.randint(2, 8), VELOCITY_Y]
        color = RandomColor()
        self.r, self.g, self.b = color.update_color()
