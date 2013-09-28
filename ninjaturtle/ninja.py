from __future__ import division, print_function, absolute_import
import sys
from turtle import Turtle as stdlib_turtle

from ninjaturtle.common import (
    MOVE,
    ROTATE,
    DEFAULT_MAX_SPEED,
    DEFAULT_MAX_TURN,
)
from ninjaturtle.turtleapi import RenderTurtleAPI


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
    """The main user interface to a Turtle.

    Provides an indentical API to the stdlib turtle module, warts and all, plus
    a few new ones. Responsibility for implemented the API is split in half.
    NinjaTurtle directly provides all movement related APIs, and the renderer
    implementation provides all drawing related APIs. Uses runtime object
    composition and explicit method injection to do this, rather than multiple
    inheritance with mixins. Because, eww.
    """

    def __init__(
            self,
            engine,
            max_speed=DEFAULT_MAX_SPEED,
            max_turn=DEFAULT_MAX_TURN):

        self.engine = engine

        self.model = engine.create_turtle(self)
        # inject renderer responsibilities
        self._inject_backend(self.model.backend)

        # shortcuts
        self.data = self.model.data
        self.queue_action = self.model.queue_action

        self._max_speed = max_speed  # world distance/sec
        self._max_turn = max_turn    # degrees/sec
        self._calculate_speeds()

        # temporary hack
        self._set_color = None

    def _inject_backend(self, backend):
        """Inject methods from the provided RenderTurtleAPI into NinjaTurtle"""
        self.backend = backend
        for api in RenderTurtleAPI:
            assert not hasattr(self, api)
            setattr(self, api, getattr(backend, api))

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
    # NinjaTurtle portion of stdlib turtle api
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
        elif 0.5 < speed < 10.5:
            speed = int(round(speed))
        else:
            speed = 0
        if speed == 0:
            speed = sys.maxsize
        self.data[5] = speed
        self._calculate_speeds()

    def forward(self, distance=None):
        if distance is None:
            self.queue_action(MOVE, self._throttled_move_speed)
        else:
            self.queue_action(MOVE, self._throttled_move_speed, distance)

    fd = forward

    def backward(self, distance=None):
        if distance is None:
            self.queue_action(MOVE, -self._throttled_move_speed)
        else:
            self.queue_action(MOVE, -self._throttled_move_speed, -distance)

    bk = back = backward

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

    def setx(self, x):
        # WRONG. Should animate
        self.data[0] = x

    def sety(self, y):
        # WRONG. Should animate
        self.data[1] = y

    def goto(self, x, y):
        pass

    setpos = setposition = goto

    def settiltangle(self, ):
        pass

    def tiltangle(self, ):
        pass

    def tilt(self):
        pass

    def towards(self):
        pass

    def distance(self):
        pass

    def home(self):
        pass

    def reset(self):
        pass

    def circle(self):
        pass

    def clone(self):
        pass

    def setheading(self, heading):
        diff = abs(heading - self.data[4])
        if heading > self.data[4]:
            self.left(diff)
        else:
            self.right(diff)

    seth = setheading

    def xcor(self):
        return self.data[0]

    def ycor(self):
        return self.data[1]

    def position(self):
        return self.data[0], self.data[1]

    pos = position

    def heading(self):
        return self.data[4]
