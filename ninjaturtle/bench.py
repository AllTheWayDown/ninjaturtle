from time import time

from ninjaturtle.render import DummyRender
from ninjaturtle import NinjaTurtle, get_engine


class Worker1(NinjaTurtle):
    def get_actions(self):
        self.left()


class Worker2(NinjaTurtle):
    def get_actions(self):
        self.forward()

engine = get_engine()
engine.renderer = DummyRender(engine)

N = 100
iterations = list(range(N))

# kick off with 1000
n = 1000
inc = 200
for i in range(n//2):
    Worker1(engine)
    Worker2(engine)

target = 1/30 * 1000
while 1:
    start = time()
    for i in iterations:
        engine.tick(target)
    tick_time = (time() - start) / N * 1000
    print("{}: {:.2f} ms/tick".format(n, tick_time))
    if tick_time > target * 0.7:
        break

    for i in range(inc//2):
        Worker1(engine)
        Worker2(engine)
    n += inc
