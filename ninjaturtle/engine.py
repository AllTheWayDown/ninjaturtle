from __future__ import division, print_function, absolute_import
import itertools
from collections import deque
from time import time, sleep
from random import shuffle

#try:
#    from ninjaturtle import cvector as vector
#except ImportError:
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

    Acts as glue object between the frontend turtle object (NinjaTurtle) and
    the backend renderer turtle object.

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

    The reason of using a list like interface is to allow for the possibility
    of direct writing to a c-backed memory store. The benefit is that we can do
    zero-copy calls out to C for acceration of animation, or OpenGL rendering,
    The drawback is that it is slightly cumbersome to develop with has you have
    to remember hardcoded offsets for different data arributes. But this
    interface is not exposed directly to the user - just the NinjaTurtle object
    and math functions. We could use properties, but they are slow, causing ~3x
    speed penalty for get/set in cpython 3.3, and turtle model calculations are
    the slowest part of the whole thing.
    """
    id_seq = itertools.count()

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

    def __init__(self, frontend):
        """Just creates an empty model"""
        self.id = next(self.id_seq)
        self.frontend = frontend
        self.backend = None
        self.actions = deque()
        # use a standard list be default for now
        self.data = self.DEFAULT_TURTLE[:]

    def reset(self):
        """Reset turtle to default position"""
        for i, value in zip(range(TURTLE_DATA_SIZE), self.DEFAULT_TURTLE):
            self.data[i] = value
        self.actions.clear()

    def queue_action(self, action, value, goal=None):
        """Queue an action (rotate or move) to be calculated"""
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
        self.turtles = {}

    def create_turtle(self, frontend):
        """Calls out to the renderer to allocate new backend turtle data.

        The renderer has to be responsible for allocating the data, as for
        OpenGL this is very importent. For other renderers, they can make it
        simpler, but we need to provide this hook.

        Note: passes a reference to the frontend turtle
        """
        model = TurtleModel(frontend)
        self.renderer.create_turtle(model)
        self.turtles[model.id] = model
        return model

    def tick(self, dt):
        """run all the model calculations for dt seconds"""

        turtles = list(self.turtles.items())
        shuffle(turtles)
        updated = False

        for id, turtle in turtles:
            actions = turtle.actions
            if not actions:
                turtle.frontend.get_actions()
            if actions:
                updated = True
                action, step, goal = actions.popleft()
                value = step * dt

                # are more steps needed to reach the goal
                if goal is not None:
                    if abs(value) >= abs(goal) - 0.01:
                        value = goal
                    else:
                        actions.appendleft((action, step, goal - value))

                # actually move the model
                self.ACTIONS[action](turtle.data, value)

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
