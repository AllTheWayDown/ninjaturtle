from collections import deque
import functools

try:
    import _vector as vector
except ImportError:
    import vector

from common import (
    MOVE,
    ROTATE,
)


class TurtleModel():
    """A turtle modelled in 2D space"""

    def __init__(self, engine, data):
        self.engine = engine
        # data is [X, Y, angle, size]
        self.data = data
        self.speed = 1
        self.frames = deque()
        self.reset()

        self.MOVE = functools.partial(vector.move, self.data)
        self.ROTATE = functools.partial(vector.rotate, self.data)

    def add_action(self, cmd, value):
        frames = self.engine.animator.interpolate(cmd, value, self.speed)
        self.frames.extend(frames)

    def reset(self):
        self.data[0:3] = 0.0, 0.0, 0.0


class TurtleInterface(object):

    def __init__(self, model):
        self.model = model
        self.add_action = model.add_action

    def forward(self, distance):
        self.add_action(MOVE, distance)

    def back(self, distance):
        self.add_action(MOVE, -distance)

    def left(self, angle):
        self.add_action(ROTATE, angle)

    def right(self, angle):
        self.add_action(ROTATE, -angle)

    def speed(self, value=None):
        if value is None:
            return self.model.speed
        else:
            self.model.speed = value

def interactive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        engine.run_until_empty()
    return wrapper


class InteractiveTurtle(TurtleInterface):
    forward = interactive(TurtleInterface.forward)
    backwards = interactive(TurtleInterface.forward)
    left = interactive(TurtleInterface.left)
    right = interactive(TurtleInterface.right)


