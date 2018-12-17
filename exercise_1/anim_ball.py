# to run the application
from kivy.uix.widget import Widget

from kivy.core.window import Window
# animation
from kivy.animation import Animation


class AnimBall(Widget):

    def __init__(self, **kwargs):
        super(AnimBall, self).__init__(**kwargs)
        size = Window.width / 50 + Window.height / 50
        self.width = size
        self.height = size
        self.x = (Window.width / 2 - self.width / 2)
        self.y = (Window.height / 5 - self.height / 2)

    def on_touch_down(self, *args):
        initial_y = Window.height / 5 - self.height / 2
        initial_x = (Window.width / 2 - self.width / 2)
        y = Window.height / 10 + self.y

        # max_y condition to not force the ball to stay inside the window
        max_y = 2 * Window.height - self.height / 2

        animation = Animation(x=initial_x, y=y, duration=0.3, t='linear')
        animation += Animation(x=initial_x, y=initial_y, duration=0.3, t='linear')
        animation.start(self)

# It's here the file to modify for the ex_1

# 1:
    # Animate the ball to do a jump: It has to simulate the gravity

    # replace t='linear' by one of the examples:

        # t = 'linear'
        # t = 'in_out_circ'
        # t = 'in_out_back'

        # t = 'in_back'
        # t = 'out_back'

        # t = 'in_bounce'
        # t = 'out_bounce'

        # t = 'in_cubic'
        # t = 'out_cubic'


# 2:
    # If you try to jump multiple times very fast the animation would be non smooth
    # use Animation.cancel_all(self) before the animation to allow multiple jumps


# Fore more details go to https://kivy.org/docs/api-kivy.animation.html down the page
