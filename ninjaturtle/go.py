from engine import *
from turtle import *


from render import TurglesRenderer
tr = TurglesRenderer(4)

ENGINE = Engine(renderer=tr)

t = InteractiveTurtle(ENGINE)

ENGINE.renderer.render(ENGINE)


