


def forward(turtle, distance):

    steps = ...
    delta = distance / steps
    for i in range(steps):
        turtle.forward(delta)
        draw()



def tick(turtle):

    turtle.forward(10)

