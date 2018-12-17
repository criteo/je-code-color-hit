# to run the application
from kivy.uix.widget import Widget
from kivy.core.window import Window
# import kivy properties
from kivy.properties import NumericProperty


class AnimBall(Widget):
    r = NumericProperty(1)
    g = NumericProperty(0)
    b = NumericProperty(0)

    def __init__(self, **kwargs):
        super(AnimBall, self).__init__(**kwargs)
        size = Window.width / 50 + Window.height / 50
        self.height = size
        self.width = size
        self.x = (Window.width / 2 - self.width / 2)
        self.y = (Window.height / 5 - self.height / 2)
