from __future__ import division, print_function, absolute_import
import functools
from ninjaturtle.turtleapi import FullNinjaTurtleAPI


def interactive(turtle, api):
    """Wraps a NinjaTurtle method to run the engine after calling it."""
    func = getattr(turtle, api)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        turtle.engine.run_until_empty()
    return wrapper


class InteractiveTurtle():
    """NinjaTurtle which forces immeadiate execution of any animation.

    Deisgned to be used in interactive mode from the python prompt, like the
    stdlib turtle API.
    """
    def __init__(self, turtle):
        self._turtle = turtle
        for api in FullNinjaTurtleAPI:
            setattr(self, api, interactive(turtle, api))
