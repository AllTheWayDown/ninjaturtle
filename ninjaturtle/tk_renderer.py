from __future__ import division, print_function, absolute_import
import sys
from collections import namedtuple

from turtle import TurtleScreen, RawTurtle, TK

from ninjaturtle.render import BaseRenderer

if sys.version_info[0] < 3:
    from Tkinter import Tk, mainloop
else:
    from tkinter import Tk
    mainloop = False

TkTurtle = namedtuple('TkTurtle', 'turtle data')


class TkRenderer(BaseRenderer):

    def __init__(self, width, height, title="NinjaTurtle"):
        self.width = width
        self.height = height
        self.window_title = title

        root = Tk()
        root.wm_title(self.window_title)
        window = TK.Canvas(master=root, width=self.width, height=self.height)
        window.pack()
        self.screen = TurtleScreen(window)
        self.screen.tracer(0, 0)

        self.turtles = dict()

    def create_turtle(self, model, init=None, shape='classic'):
        # TODO use init
        backend = RawTurtle(canvas=self.screen)
        model.backend = backend
        self.turtles[model.id] = model

    def render(self):
        for model in self.turtles.values():
            data = model.data
            turtle = model.backend
            if data[0] != turtle.xcor() or data[1] != turtle.ycor():
                turtle.setpos(data[0], data[1])
            if turtle.heading() != data[4]:
                turtle.setheading(data[4])
        self.screen.update()
