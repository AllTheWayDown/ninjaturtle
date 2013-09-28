__all__ = ["NinjaTurtleAPI", "RenderTurtleAPI", "FullNinjaTurtleAPI"]

# Animation methods
# -----------------
# These methods are handled by the NinjaTurtle class and engine, and are to do
# with movement and position.

NinjaTurtleAPI = [
    'forward', 'fd',
    'backward', 'bk', 'back',
    'right', 'rt',
    'left', 'lt',
    'position', 'pos',
    'setheading', 'seth',
    'speed',
    'xcor',
    'ycor',
    'heading',

    #TODO
    'goto', 'setpos', 'setposition',
    'setx',
    'sety',
    'settiltangle',
    'tiltangle',
    'tilt',
    'towards',
    'distance',
    'home',
    'reset',
    'circle',
    'clone',

    # not doing these currently
    #'resizemode',
    #'undo',
    #'setundobuffer',
    #'undobufferentries',
    #'degrees',
    #'radians',
    #'getturtle', 'getpen',
    #'getscreen',
]


# Renderer Turtle methods
#-----------------------
#
#These methods depend on the renderer for implementation

RenderTurtleAPI = [
    'shape',
    'shapesize', 'turtlesize',
    'pencolor',

    #TODO
    'color',
    'fillcolor',
    'showturtle', 'st',
    'hideturtle', 'ht',
    'isvisible',
    'pendown', 'pd', 'down',
    'penup', 'pu', 'up',
    'pensize', 'width',
    'pen',
    'isdown',
    'begin_fill', 'end_fill',
    'dot',
    'stamp',
    'clear',
    'clearstamp', 'clearstamps',
    'write',


    # currently unsupported
    #'begin_poly',
    #'end_poly',
    #'get_poly',
]

FullNinjaTurtleAPI = NinjaTurtleAPI + RenderTurtleAPI

_msg = "NinjaTurtleAPI and RenderTurtleAPI are not disjoint!"
assert len(set(NinjaTurtleAPI) & set(RenderTurtleAPI)) == 0, _msg
