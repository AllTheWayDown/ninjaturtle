from ninjaturtle.engine import ENGINE
from ninjaturtle.ninja import NinjaTurtle
from ninjaturtle.interactive import InteractiveTurtle

from turgles.renderer import Renderer

ENGINE.renderer = Renderer(600, 600)

n = NinjaTurtle(ENGINE)
t = InteractiveTurtle(n)

ENGINE.renderer.render()
