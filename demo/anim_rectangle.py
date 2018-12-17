# to run the application
from kivy.uix.widget import Widget
from kivy.core.window import Window
# animation
from kivy.clock import Clock
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
        Clock.schedule_interval(self.update_width, UPDATE_CLOCK)
        Clock.schedule_interval(self.update_height, UPDATE_CLOCK_SLOW)

    def update_height(self, *args):
        self.y -= self.velocity[1]

    def update_width(self, *args):
        self.x -= self.velocity[0]
        if self.x < 0 or (self.x + self.width) > Window.width:
            self.velocity[0] *= -1

    def freeze(self):
        Clock.unschedule(self.update_width)
        Clock.unschedule(self.update_height)
        Clock.schedule_once(self.end_freeze, FREEZE_CLOCK)

    def end_freeze(self, *args):
        Clock.schedule_interval(self.update_width, UPDATE_CLOCK)
        Clock.schedule_interval(self.update_height, UPDATE_CLOCK_SLOW)
