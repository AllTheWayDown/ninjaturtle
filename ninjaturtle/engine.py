from __future__ import division, print_function, absolute_import
from collections import deque
from time import time, sleep
from random import shuffle

try:
    from ninjaturtle import _vector as vector
except ImportError:
    from ninjaturtle import vector

from ninjaturtle.common import (
    MOVE,
    ROTATE,
    TURTLE_DATA_SIZE,
    DEFAULT_TIME_DELTA,
)

from ninjaturtle.render import DummyRender


class TurtleModel():
    """A turtle modelled in 2D space.

    The data attribute exposes a list like interface for turtle data that is
    used for maths calulations and rendering. Uses normal attribute for other
    data (e.g. shape)

    model[0]  - X position
    model[1]  - Y position
    model[2]  - X scale
    model[3]  - Y scale
    model[4]  - angle/orientation in degrees
    model[5]  - speed
    model[6]  - cos(radians(angle)) - a cache
    model[7]  - sin(radians(angle)) - a cache
    model[8]  - red
    model[9]  - green
    model[10] - blue
    model[11] - alpha

    The reason of using a list like interface is performance with OpenGL.
    This interface is not exposed directly to the user - just the NinjaTurtle
    object and math functions.

    Convienience properties are slow causing ~3x speed penalty for get/set, and
    turtle model calculations are the slowest part of the whole thing.
    """

    DEFAULT_TURTLE = [
        0.0,  # X
        0.0,  # Y
        1.0,  # scale x
        1.0,  # scale y
        0.0,  # angle
        6.0,  # speed
        1.0,  # cos angle
        0.0,  # sin angle
        0.0,  # r
        0.0,  # g
        0.0,  # b
        1.0,  # alpha
    ]
    DEFAULT_SHAPE = 'classic'

    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.actions = deque()
        self.reset()
        self.shape = self.DEFAULT_SHAPE

    def reset(self):
        for i, value in zip(range(TURTLE_DATA_SIZE), self.DEFAULT_TURTLE):
            self.data[i] = value
        self.actions.clear()

    def queue_action(self, action, value, goal=None):
        self.actions.append((action, value, goal))

    def __str__(self):
        return "TurtleModel({:.1f},{:.1f}):{:.1f})".format(
            self.data[0], self.data[1], self.data[4])

    __repr__ = __str__


class Engine(object):

    ACTIONS = {
        MOVE: vector.move,
        ROTATE: vector.rotate,
    }

    def __init__(self, renderer=None):
        if renderer is None:
            renderer = DummyRender(self)
        self.renderer = renderer
        self.turtles = []
        self.actions = []

    def create_model(self):
        id, data = self.renderer.create_turtle_data(
            TurtleModel.DEFAULT_SHAPE,
            TurtleModel.DEFAULT_TURTLE,
        )
        model = TurtleModel(id, data)
        self.turtles.append(model)
        return model

    def tick(self, dt):
        """run all the model calculations for dt seconds"""

        shuffle(self.turtles)
        updated = False
        actions = self.ACTIONS

        for turtle in self.turtles:
            if turtle.actions:
                updated = True
                action, step, goal = turtle.actions.popleft()
                value = step * dt

                # are more steps needed to reach the goal
                if goal is not None:
                    if abs(value) >= abs(goal) - 0.01:
                        value = goal
                    else:
                        turtle.actions.appendleft((action, step, goal - value))

                # actually move the model
                actions[action](turtle.data, value)

        return updated

    def run_until_empty(self):
        # TODO use a proper loop
        updated = True
        tick = self.tick
        render = self.renderer.render
        freq = DEFAULT_TIME_DELTA
        last = time() - DEFAULT_TIME_DELTA
        first = True
        while updated:
            ts = time()
            dt = ts - last
            last = ts
            updated = tick(dt)
            if updated or first:
                render()
                first = False
            elapsed = time() - ts
            if elapsed < freq:
                sleep(freq - elapsed)


ENGINE = Engine()


def get_engine():
    return ENGINE


def run_until_empty():
    ENGINE.run_until_empty()
