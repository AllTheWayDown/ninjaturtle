import engine
import tk_renderer
r = tk_renderer.TkRenderer(600, 600)
e = engine.Engine(r)
from ninja import *
t = InteractiveTurtle(e)
