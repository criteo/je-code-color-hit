from kivy.uix.widget import Widget
# utilities
import random

VELOCITY_Y = 10

# Global variables colors
YELLOW = (1, 0.7, 0)
BLUE = (0, 0, 1)
RED = (1, 0, 0)
GREEN = (0, 1, 0)


class RandomColor(Widget):

    def get_color(self, value):
        if value == 0:
            return RED
        if value == 1:
            return YELLOW
        if value == 2:
            return BLUE
        if value == 3:
            return GREEN
        # default color
        return GREEN

    def update_color(self):
        return self.get_color(random.randint(0, 3))
