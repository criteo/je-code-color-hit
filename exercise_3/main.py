# to run the application
from kivy.app import App
# import classes
from root import *


class ColorHit(App):
    def build(self):
        root = Root()
        return root


if __name__ == '__main__':
    ColorHit().run()
