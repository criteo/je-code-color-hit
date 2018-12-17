# to run the application
from kivy.uix.widget import Widget
from kivy.core.window import Window
# animation
from kivy.clock import Clock
# import kivy properties
from kivy.properties import NumericProperty

# import classes
from utils import *


class ColorBall(Widget):
    r = NumericProperty(0)
    g = NumericProperty(0)
    b = NumericProperty(1)
    
    def __init__(self, **kwargs):
        super(ColorBall, self).__init__(**kwargs)      
        size = Window.width / 50 + Window.height / 50
        self.width = size
        self.height = size
        self.x = (Window.width / 2 - self.width / 2)
        self.y = (Window.height * 4 / 5 - self.height / 2)
        color = RandomColor()
        self.r, self.g, self.b = color.update_color()
        Clock.schedule_interval(self.update_height, UPDATE_CLOCK_SLOW)
    
    def update_height(self, *args):
        self.y -= 1.2 * VELOCITY_Y
