from kivy.uix.widget import Widget
# utilities
import random

# time updates global variables
UPDATE_CLOCK = 1/60.
UPDATE_CLOCK_SLOW = 1.
FREEZE_CLOCK = 3.

# global constant position
VELOCITY_Y = 10

# Global variables colors
YELLOW = (1, 0.7, 0)
BLUE = (0, 0, 1)
RED = (1, 0, 0)
GREEN = (0, 1, 0)


class RandomColor(Widget):

    def get_color(self, value):
        if value == 0:
            return RED
        if value == 1:
            return YELLOW
        if value == 2:
            return BLUE
        if value == 3:
            return GREEN
        # default color
        return GREEN

    def update_color(self):
        return self.get_color(random.randint(0, 3))


def check_collision(ball, x, width, y, height):
    ball_x, ball_width, ball_y, ball_height = ball
    return collision_vertical(ball_x, ball_width, ball_y, ball_height, x, width, y, height)\
        or collision_horizontal(ball_x, ball_width, ball_y, ball_height, x, width, y, height)


def collision_vertical(ball_x, ball_width, ball_y, ball_height, x, width, y, height):
    return (check_edge(ball_x, ball_width, x)
            or check_edge(ball_x, ball_width, x + width))\
           and check_position(ball_y, ball_height, y, height)


def collision_horizontal(ball_x, ball_width, ball_y, ball_height, x, width, y, height):
    return (check_edge(ball_y, ball_height, y)
            or check_edge(ball_y, ball_height, y + height))\
           and check_position(ball_x, ball_width, x, width)


def check_edge(ball_x, ball_width, edge_x):
    return ball_x - ball_width / 2 <= edge_x <= ball_x + ball_width / 2


def check_position(ball_x, ball_width, x, width):
    return x <= ball_x + ball_width / 2 and x + width >= ball_x - ball_width / 2
