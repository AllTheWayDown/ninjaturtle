from engine import *
from turtle import *

t = NinjaTurtle(ENGINE)

t.right(45)
t.back(100)

ENGINE.run_until_empty()
