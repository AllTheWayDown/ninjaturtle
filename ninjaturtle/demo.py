from ninjaturtle.engine import ENGINE
from ninjaturtle.ninja import InteractiveTurtle

from turgles.renderer import Renderer

ENGINE.renderer = Renderer(800, 800, 16)

t = InteractiveTurtle(ENGINE)
