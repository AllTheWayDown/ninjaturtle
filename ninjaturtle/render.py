from __future__ import division, print_function, absolute_import
from ninjaturtle.turtleapi import RenderTurtleAPI


class BaseRenderer(object):
    """Describes interface for renderer functionality.

    The NinjaTurtle engine expects to work with a list-like data data structure
    for each turtle of size TURTLE_DATA_SIZE. This is an optimisation that
    allows for zero-copy when dealing with C/OpenGL. Other renderers will need
    to provide/emulate a similar inteface if they don't use a list-like one
    natively.
    """

    def create_turtle(self, model):
        """Allocate renderer specific storage for a turtle.

        This should look like a list of TURTLE_DATA_SIZE length."""

    def render(self):
        """Render the current state"""


class DummyBackend(object):
    """Backend turtle that does nothing"""


def dummy(*args, **kwargs):
    pass


for api in RenderTurtleAPI:
    setattr(DummyBackend, api, dummy)


class DummyRender(BaseRenderer):
    """Render to stdout for debugging"""

    def __init__(self, engine):
        self.engine = engine

    def create_turtle(self, model):
        model.backend = DummyBackend()

    def render(self):
        for t in self.engine.turtles:
            print(t)
