from __future__ import division, print_function, absolute_import

import itertools

from ninjaturtle.common import TURTLE_DATA_SIZE


class BaseRenderer(object):
    """Describes interface for renderer functionality.

    The NinjaTurtle engine expects to work with a list-like data data structure
    for each turtle of size TURTLE_DATA_SIZE. This is an optimisation that
    allows for zero-copy when dealing with C/OpenGL. Other renderers will need
    to provide/emulate a similar inteface if they don't use a list-like one
    natively.
    """
    id_seq = itertools.count()

    def create_turtle_data(self, shape, defaults):
        """Allocate renderer specific storage for a turtle.

        This should look like a list of TURTLE_DATA_SIZE length."""
        return next(self.id_seq), defaults[:]

    def set_shape(self, id, shape):
        """Used to inform the renderer of a new shape.

        Currently, just shape name is supported, but it could also be an image
        path or a list of coordinates."""

    def render(self):
        """Render the current state"""


class DummyRender(BaseRenderer):
    """Render to stdout for debugging"""

    def __init__(self, engine):
        self.engine = engine

    def render(self):
        for t in self.engine.turtles:
            print(t)

    def set_shape(self, id, shape):
        pass
