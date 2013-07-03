import itertools
from random import shuffle

from common import (
    MOVE,
    ROTATE,
)
from turtle import TurtleModel
import vector

_ENGINE = None


def get_engine():
    return _ENGINE

def run_until_empty():
    _ENGINE.run_until_empty()


class DummyRender(object):
    def render(self):
        pass

class Engine(object):

    def __init__(self, animator=None, renderer=None):
        if animator is None:
            animator = LinearAnimator()
        if renderer is None:
            renderer = DummyRender()
        self.renderer = renderer
        self.animator = animator
        self.turtles = []

    def create_turtle(self):
        data = [0, 0, 0, 0]
        model = TurtleModel(self, data)
        self.turtles.append(model)
        return model

    def tick(self):
        """run all the model calculations for a tick"""

        shuffle(self.turtles)
        updated = False
        for turtle in self.turtles:
            action = value = None
            if turtle.frames:
                action, value = turtle.frames.popleft()
            if action is not None:
                updated = True
                getattr(turtle, action)(value)

        return updated

    def run_until_empty(self):
        updated = True
        tick = self.tick
        render = self.renderer.render
        while updated:
            updated = tick()
            if updated:
                render()



class LinearAnimator(object):
    move_iter = itertools.repeat(MOVE)
    rotate_iter = itertools.repeat(ROTATE)

    def interpolate(self, action, value, speed):
        if action == MOVE:
            return zip(self.move_iter,
                       vector.interpolate_linear_move(value, speed))
        elif action == ROTATE:
            return zip(self.rotate_iter,
                       vector.interpolate_linear_rotation(value, speed))

_ENGINE = Engine()




