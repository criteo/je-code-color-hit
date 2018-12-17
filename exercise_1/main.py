# to run the application
from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget
# import classes
from anim_ball import *
from builder import *

# fixed window size
Config.set('graphics', 'resizable', False)


class Root(Widget):

    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)
        self.add_widget(AnimBall())


class ColorHit(App):
    def build(self):
        root = Root()
        return root


if __name__ == '__main__':
    ColorHit().run()
