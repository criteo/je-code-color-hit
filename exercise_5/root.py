# to run the application
from kivy.uix.widget import Widget

# to run the window
from kivy.core.window import Window

# to add movements
from kivy.clock import Clock

# import kivy properties
from kivy.properties import NumericProperty
from kivy.properties import ListProperty

# import classes
from builder import *
from anim_ball import *

# utils
from functools import partial

# fixed window size
from kivy.config import Config
Config.set('graphics', 'resizable', False)


class Root(Widget):
    attempt = NumericProperty(1)
    score = NumericProperty(0)
    max_score = NumericProperty(0)
    ball = ListProperty([])

    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)
        self.start()
        Clock.schedule_interval(self.update_score_and_attempt, UPDATE_CLOCK)

    def start(self):
        if self.ball:
            self.remove_widget(self.ball.pop())
        self.ball.append(AnimBall())
        self.add_widget(self.ball[0])
        self.attempt = 10
        self.max_score = max(self.score, self.max_score)
        self.score = 0

    def update_score_and_attempt(self, *args):
        self.score, self.attempt = self.ball[0].update_score(self.score, self.attempt)
        # To do update attempt

# It's here the second file to modify for the ex_5

    # 2:
        # in "update_score_and_attempt: update attempt
        # if attempt become less then 0 we should restart!

