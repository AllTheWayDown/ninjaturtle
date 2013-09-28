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

    def create_turtle_data(self, shape, defaults):
        id, data = super(TkRenderer, self).create_turtle_data(shape, defaults)
        turtle = RawTurtle(canvas=self.screen, shape=shape)
        self.turtles[id] = TkTurtle(turtle, data)
        return id, data, turtle

    def set_shape(self, id, shape):
        """Pass thru to RawTurtle"""
        self.turtles[id].turtle.shape(shape)

    def render(self):
        for turtle, data in self.turtles.values():
            if data[0] != turtle.xcor() or data[1] != turtle.ycor():
                turtle.setpos(data[0], data[1])
            if turtle.heading() != data[4]:
                turtle.setheading(data[4])
        self.screen.update()
