from __future__ import division, print_function, absolute_import
import functools
from common import (
    MOVE,
    ROTATE,
    DEFAUlT_MAX_SPEED,
    DEFAULT_MAX_TURN,
)


# model[0] - X position
# model[1] - Y position
# model[2] - X scale
# model[3] - Y scale
# model[4] - angle/orientation in degrees
# model[5] - speed
# model[6] - cos(radians(angle)) - a cache
# model[7] - sin(radians(angle)) - a cache


class NinjaTurtle(object):

    def __init__(self,
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

    def speed(self, speed=None):
        if speed is None:
            return self.data[5]
        self.data[5] = speed
        self._calculate_speeds()

    # alias
    throttle = speed

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

    def forward(self, distance=None):
        if distance is None:
            self.queue_action(MOVE, self._throttled_move_speed)
        else:
            self.queue_action(MOVE, self._throttled_move_speed, distance)

    def back(self, distance=None):
        if distance is None:
            self.queue_action(MOVE, -self._throttled_move_speed)
        else:
            self.queue_action(MOVE, -self._throttled_move_speed, -distance)

    def left(self, angle=None):
        if angle is None:
            self.queue_action(ROTATE, self._throttled_turn_speed)
        else:
            self.queue_action(ROTATE, self._throttled_turn_speed, angle)

    def right(self, angle):
        if angle is None:
            self.queue_action(ROTATE, -self._throttled_turn_speed)
        else:
            self.queue_action(ROTATE, -self._throttled_turn_speed, -angle)

    def xcor(self):
        return self.data[0]

    def ycor(self):
        return self.data[1]

    def position(self):
        return self.data[0], self.data[1]

    def heading(self):
        return self.data[4]


def interactive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        engine.run_until_empty()
    return wrapper


class InteractiveTurtle(NinjaTurtle):
    forward = interactive(NinjaTurtle.forward)
    back = interactive(NinjaTurtle.back)
    left = interactive(NinjaTurtle.left)
    right = interactive(NinjaTurtle.right)


