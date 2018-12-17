# to run the application
from kivy.uix.widget import Widget

# import classes
from builder import *
from anim_ball import *

# fixed window size
from kivy.config import Config
Config.set('graphics', 'resizable', False)


class Root(Widget):  

    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)
        self.add_widget(AnimBall())
