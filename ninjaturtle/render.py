from __future__ import division, print_function, absolute_import

from ninjaturtle.common import TURTLE_DATA_SIZE


class DummyRender(object):

    def render(self, engine):
        for t in engine.turtles:
            print(t)

    def create_turtle_data(self):
        return [0] * TURTLE_DATA_SIZE
