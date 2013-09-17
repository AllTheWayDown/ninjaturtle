from __future__ import division, print_function, absolute_import
import sys
import functools
from turtle import Turtle as stdlib_turtle

from ninjaturtle.common import (
    MOVE,
    ROTATE,
    DEFAUlT_MAX_SPEED,
    DEFAULT_MAX_TURN,
)
from ninjaturtle.tk_colors import COLORS


# model[0] - X position
# model[1] - Y position
# model[2] - X scale
# model[3] - Y scale
# model[4] - angle/orientation in degrees
# model[5] - speed
# model[6] - cos(radians(angle)) - a cache
# model[7] - sin(radians(angle)) - a cache
def stdlib_docstring(func):
    stdlib_func = getattr(stdlib_turtle, func.__name__)
    func.__doc__ = stdlib_func.__doc__
    return func


class NinjaTurtle(object):

    def __init__(
            self,
            engine,
            max_speed=DEFAUlT_MAX_SPEED,
            max_turn=DEFAULT_MAX_TURN):

        self.engine = engine
        self.model = engine.create_model()
        self.data = self.model.data
        self.queue_action = self.model.queue_action

        self._max_speed = max_speed  # world distance/sec
        self._max_turn = max_turn    # degrees/sec
        self._calculate_speeds()
        self._set_color = None

    def max_speed(self, max_speed=None):
        if max_speed is None:
            return self._max_speed
        self._max_speed = max_speed
        self._calculate_speeds()

    def max_turn(self, max_turn=None):
        if max_turn is None:
            return self._max_turn
        self._max_turn = max_turn
        self._calculate_speeds()

    def _calculate_speeds(self):
        self._throttle = throttle = self.data[5]/10.0
        self._throttled_move_speed = self._max_speed * throttle
        self._throttled_turn_speed = self._max_turn * throttle

    #-----------------------------------------------
    # stdlib turtle api
    #-----------------------------------------------

    _speed_strings = {
        'fastest': 0,
        'fast': 10.0,
        'normal': 6.0,
        'slow': 3.0,
        'slowest': 1.0,
    }

    @stdlib_docstring
    def speed(self, speed=None):
        if speed is None:
            return self.data[5]
        if hasattr(speed, 'lower'):
            speed = speed.lower()
        if speed in self._speed_strings:
            speed = self._speed_strings[speed]
        assert speed <= 10.0
        if speed == 0:
            speed = sys.maxsize
        self.data[5] = speed
        self._calculate_speeds()

    throttle = speed

    def forward(self, distance=None):
        if distance is None:
            self.queue_action(MOVE, self._throttled_move_speed)
        else:
            self.queue_action(MOVE, self._throttled_move_speed, distance)

    fd = forward

    def back(self, distance=None):
        if distance is None:
            self.queue_action(MOVE, -self._throttled_move_speed)
        else:
            self.queue_action(MOVE, -self._throttled_move_speed, -distance)

    bk = back

    def left(self, angle=None):
        if angle is None:
            self.queue_action(ROTATE, self._throttled_turn_speed)
        else:
            self.queue_action(ROTATE, self._throttled_turn_speed, angle)

    lt = left

    def right(self, angle):
        if angle is None:
            self.queue_action(ROTATE, -self._throttled_turn_speed)
        else:
            self.queue_action(ROTATE, -self._throttled_turn_speed, -angle)

    rt = right

    def xcor(self):
        return self.data[0]

    def setx(self, x):
        self.data[0] = x

    def ycor(self):
        return self.data[1]

    def sety(self, y):
        self.data[1] = y

    def position(self):
        return self.data[0], self.data[1]

    pos = position

    def heading(self):
        return self.data[4]

    def setheading(self, heading):
        diff = abs(heading - self.data[4])
        if heading > self.data[4]:
            self.left(diff)
        else:
            self.right(diff)

    @stdlib_docstring
    def shape(self, shape):
        new_data = self.engine.renderer.set_shape(self.model.id, shape)
        self.model.data = new_data
        self.data = new_data

    @stdlib_docstring
    def shapesize(self, stretch_wid=None, stretch_len=None, outline=None):
        if stretch_wid is not None:
            self.data[2] = stretch_wid
        if stretch_len is not None:
            self.data[3] = stretch_len

    turtlesize = shapesize

    @stdlib_docstring
    def pencolor(self, color):
        if color in COLORS:
            color = COLORS[color]
        elif color[0] == '#':
            color = (
                int(color[1:3], 16),
                int(color[3:5], 16),
                int(color[5:7], 16)
            )
        else:
            assert len(color) == 3

        self.data[8] = color[0] / 255.0
        self.data[9] = color[1] / 255.0
        self.data[10] = color[2] / 255.0

    def penup(self):
        pass

    def pendown(self):
        pass

    def hideturtle(self):
        self._set_color = self.data[8:10]
        self.pencolor('#ffffff')

    ht = hideturtle

    def showturtle(self):
        if self._set_color:
            self.data[8:10] = self._set_color
        self._set_color = None

    st = showturtle


def interactive(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        self.engine.run_until_empty()
    return wrapper


class InteractiveTurtle(NinjaTurtle):
    forward = interactive(NinjaTurtle.forward)
    back = interactive(NinjaTurtle.back)
    left = interactive(NinjaTurtle.left)
    right = interactive(NinjaTurtle.right)

    shape = interactive(NinjaTurtle.shape)
    shapesize = interactive(NinjaTurtle.shapesize)

    pencolor = interactive(NinjaTurtle.pencolor)
