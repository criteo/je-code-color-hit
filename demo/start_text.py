from kivy.uix.widget import Widget
from kivy.core.window import Window
# import kivy properties
from kivy.properties import StringProperty


class TextStart(Widget):
    text = StringProperty("Ready!")

    def __init__(self, **kwargs):
        super(TextStart, self).__init__(**kwargs)
        self.x = Window.width / 2 - self.width / 2
        self.y = Window.height / 2 - self.height / 2
