# to run the application
from kivy.uix.widget import Widget
from kivy.core.window import Window
# import kivy properties
from kivy.properties import NumericProperty


class ColorBall(Widget):
    r = NumericProperty(1)
    g = NumericProperty(0.7)
    b = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super(ColorBall, self).__init__(**kwargs)
        size = Window.width / 50 + Window.height / 50
        self.width = size
        self.height = size
        self.x = (Window.width / 2 - self.width / 2)
        self.y = (Window.height * 3 / 5 - self.height / 2)