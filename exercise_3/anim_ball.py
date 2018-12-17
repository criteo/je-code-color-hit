# to run the application
from kivy.uix.widget import Widget
from kivy.core.window import Window
# animation
from kivy.animation import Animation
# import kivy properties
from kivy.properties import NumericProperty

# import classes
from color_ball import *


class AnimBall(Widget):
    r = NumericProperty(0)
    g = NumericProperty(0)
    b = NumericProperty(1)
    count_touch = NumericProperty(0)

    def __init__(self, **kwargs):
        super(AnimBall, self).__init__(**kwargs)
        size = Window.width / 50 + Window.height / 50
        self.width = size
        self.height = size
        self.x = (Window.width / 2 - self.width / 2)
        self.y = (Window.height / 5 - self.height / 2)  
        color = RandomColor()
        self.r, self.g, self.b = color.update_color()
        self.add_widget(ColorBall())
        Clock.schedule_interval(self.update_color_on_hit, UPDATE_CLOCK)

    def on_touch_down(self, touch):
        initial_y = Window.height / 5 - self.height / 2
        initial_x = (Window.width / 2 - self.width / 2)
        y = Window.height / 10 + self.y
        max_y = 2*Window.height - self.height / 2
        if self.y + y < max_y:
            Animation.cancel_all(self)
            # TO do animation = ... jump!
            animation = Animation(x=initial_x, y=y, duration=0.3, t='out_cubic')
            animation += Animation(x=initial_x, y=initial_y, duration=0.3, t='in_cubic')
            animation.start(self)

    def update_color_on_hit(self, *args):
        # update color if hit
        if self.children and self.check_hit_ball():
            color_ball = self.children[0]
            self.r, self.g, self.b = color_ball.r, color_ball.g, color_ball.b
            self.remove_widget(self.children[0])
                
    def check_hit_ball(self):
        color_ball = self.children[0]
        return False

# It's here the file to modify for the ex_3

    # 1: the objective is to code check_hit_ball
        # remove False
        # Use color_ball.y, color_ball.width, self.y and self.width to find the hit
        # (for more details see the slides)

        # To compare too variables A and B:
            # A >= B
            # A <= B
            # A > B
            # A < B
            # A == B
            # A != B
