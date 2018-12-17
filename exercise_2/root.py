# to run the application
from kivy.uix.widget import Widget

# import kivy properties
from kivy.properties import NumericProperty

# import classes
from builder import *
from anim_ball import *
from color_ball import *
from anim_rectangle import *

from kivy.config import Config
# fixed window size
Config.set('graphics', 'resizable', False)


class Root(Widget):
    # local variables can be seen and set through the Builder "Builder.load_string"
    # here we are using the default values as initializer some of them are reset at init
    attempt = NumericProperty(1)
    score = NumericProperty(0)
    max_score = NumericProperty(0)
    

    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)
        self.add_widget(AnimBall())
        self.add_widget(ClockRect())
        self.add_widget(ColorBall())
        self.attempt = 5
        self.max_score = max(self.score, self.max_score)
        self.score = 0

# Here is the second file to modify
    # add another ClockRect