from __future__ import division, print_function, absolute_import

from array import array

from common import TURTLE_DATA_SIZE

class DummyRender(object):

    def render(self, engine):
        for t in engine.turtles:
            print(t)

    def create_turtle_data(self):
        return [0] * TURTLE_DATA_SIZE

from turgles.renderer import Renderer
from turgles.util import measure

class TurglesRenderer(object):

    def __init__(self, capacity, shape='classic'):
        self.capacity = capacity
        self.turtles = array('f', [0] * capacity * TURTLE_DATA_SIZE)
        self.view = memoryview(self.turtles)
        self.num_turtles = 0

        self.renderer = Renderer(800, 800,
            shape=shape,
            vertex_shader='../../turgles/turgles/' + Renderer.vertex_shader,
            fragment_shader='../../turgles/turgles/' + Renderer.fragment_shader,
        )

    def create_turtle_data(self):
        offset = self.num_turtles * TURTLE_DATA_SIZE
        view = self.view[offset:offset + TURTLE_DATA_SIZE]
        self.num_turtles += 1
        return view

    def render(self, engine):
        self.renderer.render(self.turtles, self.num_turtles)
        with measure('flip'):
            self.renderer.window.flip()


