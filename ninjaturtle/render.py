from __future__ import division, print_function, absolute_import

from ninjaturtle.common import TURTLE_DATA_SIZE


class BaseRenderer(object):
    """Describes interface for renderer functionality.

    The NinjaTurtle engine expects to work with a list-like data data structure
    for each turtle of size TURTLE_DATA_SIZE. This is an optimisation that
    allows for zero-copy when dealing with C/OpenGL. Other renderers will need
    to provide/emulate a similar inteface if they don't use a list-like one
    natively.
    """

    def create_turtle_data(self):
        """Allocate renderer specific storage for a turtle.

        This should look like a list of TURTLE_DATA_SIZE length."""

    def set_shape(self, turtle_id, shape):
        """Used to inform the renderer of a new shape.

        Currently, just shape name is supported, but it could also be an image
        path or a list of coordinates."""

    def render(self, engine):
        """Render the current state"""


class DummyRender(BaseRenderer):
    """Render to stdout for debugging"""

    def render(self, engine):
        for t in engine.turtles:
            print(t)

    def create_turtle_data(self):
        return [0] * TURTLE_DATA_SIZE

    def set_shape(self, id, shape):
        pass
