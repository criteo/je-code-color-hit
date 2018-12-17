# to run the application
from kivy.uix.widget import Widget
from kivy.core.window import Window
# animation/
from kivy.animation import Animation
# import kivy properties
from kivy.properties import NumericProperty

# import classes
from utils import *
from anim_rectangle import *


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
        self.add_rectangles(2)
        self.update_color()
            
    def update_color(self):
        color = RandomColor()
        self.r, self.g, self.b = color.update_color()

    def on_touch_down(self, *args):
        for r in self.children:
            r.update_height()
        self.count_touch += 1
        if self.count_touch > 10:
            self.count_touch = 0
            self.update_color()
        self.animate_on_touch()

    def animate_on_touch(self):
        initial_y = Window.height / 5 - self.height / 2
        initial_x = (Window.width / 2 - self.width / 2)
        y = Window.height / 10 + self.y
        max_y = 2 * Window.height - self.height / 2
        if self.y + y < max_y:
            Animation.cancel_all(self)
            animation = Animation(x=initial_x, y=y, duration=0.3, t='out_cubic')
            animation += Animation(x=initial_x, y=initial_y, duration=0.3, t='in_cubic')
            animation.start(self)

    def add_rectangles(self, nb):
        # clear previous rectangles before adding the new ones
        while self.children:
            self.remove_widget(self.children[0])
        for i in range(max(1, nb)):
            self.add_widget(ClockRect())

    def update_objects(self):
        # remove rectangles if < min window and create new ones
        r = self.children[0]
        if r.y + r.height < Window.height / 3:
            self.add_rectangles(len(self.children) + 1)

    def check_color(self, r):
        return (self.r, self.g, self.b) == (r.r, r.g, r.b)

    def update_score(self, score, attempt):
        self.update_objects()
        b = self.x, self.width, self.y, self.height
        # update the score according to the rectangles position and the ball position
        for r in self.children:
            # update score and attempt
            pass
        return score, attempt

# It's here the first file to modify for the ex_5

    # 1: the objective is to code update_score by modifying attempt and score:
        # if same color score should increase and attempt decrease
        # remove pass
        # use self.check_color(r) and check_collision(b, r.x, r.width, r.y, r.height)
