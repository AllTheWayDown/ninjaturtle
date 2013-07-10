from array import array

from common import TURTLE_DATA_SIZE

class DummyRender(object):

    def render(self, engine):
        for t in engine.turtles:
            print(t)

    def create_turtle_data(self):
        return [0] * TURTLE_DATA_SIZE


class TurglesRenderer(object):

    def __init__(self, capacity):
        self.capacity = capacity


