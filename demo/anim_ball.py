# to run the application
from kivy.uix.widget import Widget
from kivy.core.window import Window
# animation
from kivy.animation import Animation
# import kivy properties
from kivy.properties import NumericProperty
from kivy.properties import ListProperty
from kivy.properties import BooleanProperty

# import classes
from anim_rectangle import *
from color_ball import *


class AnimBall(Widget):
    r = NumericProperty(0)
    g = NumericProperty(0)
    b = NumericProperty(1)
    freeze = BooleanProperty(False)
    count_touch = NumericProperty(0)
    list_rectangles = ListProperty([])
    list_color_ball = ListProperty([])

    def __init__(self, **kwargs):
        super(AnimBall, self).__init__(**kwargs)
        size = Window.width / 50 + Window.height / 50
        self.width = size
        self.height = size
        self.x = (Window.width / 2 - self.width / 2)
        self.y = (Window.height / 5 - self.height / 2)
        self.add_rectangles(2)
        color = RandomColor()
        self.r, self.g, self.b = color.update_color()

    def on_touch_down(self, *args):
        if not self.freeze:
            for r in self.list_rectangles:
                r.update_height()
            if not self.list_color_ball:
                self.count_touch += 1
            # add color ball
            if not self.list_color_ball and self.count_touch > 5:
                self.count_touch = 0
                self.add_color_ball()
            self.animate_on_touch()

    def animate_on_touch(self):
        initial_y = Window.height / 5 - self.height / 2
        initial_x = (Window.width / 2 - self.width / 2)
        y = Window.height / 10 + self.y

        # max_y condition to not force the ball to stay inside the window
        max_y = 2 * Window.height - self.height / 2

        if not self.freeze and self.y + y < max_y:
            Animation.cancel_all(self)
            animation = Animation(x=initial_x, y=y, duration=0.3, t='out_cubic')
            animation += Animation(x=initial_x, y=initial_y, duration=0.3, t='in_cubic')
            animation.start(self)

    def update_score(self, score, attempt):
        # update color if hit
        if self.list_color_ball and self.check_hit_ball():
            color_ball = self.list_color_ball[0]
            self.r, self.g, self.b = color_ball.r, color_ball.g, color_ball.b
            self.remove_widget(self.list_color_ball.pop())
        # update the rectangles position and the color ball position
        self.update_objects()
        # update the score according to the rectangles position and the ball position
        for r in self.list_rectangles:
            if self.check_color(r):
                if self.check_collision(r):
                    score += 10
            else:
                if self.check_collision(r):
                    attempt -= 1
        return score, attempt

    def add_color_ball(self):
        color_ball = ColorBall()
        self.list_color_ball.append(color_ball)
        self.add_widget(color_ball)

    def add_rectangles(self, nb):
        # remove previous rectangles before adding the new ones
        while self.list_rectangles:
            self.remove_widget(self.list_rectangles.pop())
        self.add_rectangles_withoutremove(nb)

    def add_rectangles_withoutremove(self, nb):
        # add rectangles increase the total number by 1
        for i in range(0, max(1, nb)):
            r = ClockRect()
            self.list_rectangles.append(r)
            self.add_widget(r)

    def update_objects(self):
        # remove rectangles if < min window and create new ones
        r = self.list_rectangles[0]
        if r.y + r.height < Window.height / 3:
            self.add_rectangles(len(self.list_rectangles) + 1)
        # remove color ball if < min window
        if self.list_color_ball:
            b = self.list_color_ball[0]
            if b.y + b.height < Window.height / 3:
                self.remove_widget(self.list_color_ball.pop())

    def check_hit_ball(self):
        color_ball = self.list_color_ball[0]
        return color_ball.y - color_ball.width / 2 <= self.y + self.width / 2

    def check_color(self, r):
        return (self.r, self.g, self.b) == (r.r, r.g, r.b)

    def check_collision(self, r):
        return self.collision_vertical(r) or self.collision_horizontal(r)

    def collision_vertical(self, r):
        return (self.check_vertical_edge(r.x) or self.check_vertical_edge(r.x + r.width)) \
               and self.check_horizontal_position(r)

    def collision_horizontal(self, r):
        return (self.check_horizontal_edge(r.y) or self.check_horizontal_edge(
            r.y + r.height)) and self.check_vertical_position(r)

    def check_vertical_edge(self, edge_x):
        return self.x - self.width / 2 <= edge_x <= self.x + self.width / 2

    def check_horizontal_edge(self, edge_y):
        return self.y - self.height / 2 <= edge_y <= self.y + self.height / 2

    def check_horizontal_position(self, r):
        return r.y <= self.y + self.height / 2 and r.y + r.height >= self.y - self.height / 2

    def check_vertical_position(self, r):
        return r.x <= self.x + self.width / 2 and r.x + r.width >= self.x - self.width / 2

    def freeze_rectangles(self):
        self.freeze = True
        for r in self.list_rectangles:
            r.freeze()
