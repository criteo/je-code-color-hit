# to run the application
from kivy.uix.widget import Widget

# to add movements
from kivy.clock import Clock

# import kivy properties
from kivy.properties import NumericProperty
from kivy.properties import ListProperty

# import classes
from builder import *
from start_text import *
from anim_ball import *

# utils
from functools import partial
from kivy.config import Config
# fixed window size
Config.set('graphics', 'resizable', False)


class Root(Widget):
    # local variables can be seen and set through the Builder "Builder.load_string"
    # here we are using the default values as initializer some of them are reset at init
    attempt = NumericProperty(1)
    score = NumericProperty(0)
    max_score = NumericProperty(0)
    ball = ListProperty([])
    text = ListProperty([])

    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)
        self.start()
        Clock.schedule_interval(self.update_score_and_position, UPDATE_CLOCK)

    def update_score_and_position(self, *args):
        self.score, self.attempt = self.ball[0].update_score(self.score, self.attempt)
        if self.attempt <= 0:
            self.start()

    def start(self):
        self.start_text()
        if self.ball:
            self.remove_widget(self.ball.pop())
        self.ball.append(AnimBall())
        self.add_widget(self.ball[0])
        self.attempt = 5
        self.max_score = max(self.score, self.max_score)
        self.score = 0
        self.freeze()

    def start_text(self):
        self.set_text("Ready! 3")
        Clock.schedule_once(partial(self.set_text, "Ready! 2"), FREEZE_CLOCK / 3)
        Clock.schedule_once(partial(self.set_text, "Ready! 1"), FREEZE_CLOCK * 2 / 3)
        Clock.schedule_once(partial(self.set_text, "Go !"), FREEZE_CLOCK)

    def set_text(self, x, *args):
        if self.text:
            self.remove_widget(self.text.pop())
        text = TextStart()
        text.text = x
        self.text.append(text)
        self.add_widget(text)

    def freeze(self):
        Clock.unschedule(self.update_score_and_position)
        self.ball[0].freeze_rectangles()
        Clock.schedule_once(self.end_freeze, FREEZE_CLOCK)

    def end_freeze(self, *args):
        Clock.schedule_interval(self.update_score_and_position, UPDATE_CLOCK)
        self.ball[0].freeze = False
