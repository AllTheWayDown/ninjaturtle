from __future__ import division

from math import sin, cos, radians


def move(data, distance):
    r = radians(data[2])
    data[0] += cos(r) * distance
    data[1] += sin(r) * distance

def rotate(data, angle):
    data[2] += angle

def interpolate_linear_move(distance, speed):
    # taken from turtle.py
    steps = abs(distance) // int(3 * (1.1 ** speed) * speed)
    delta = distance / steps
    return [delta] * steps

def interpolate_linear_rotation(angle, speed):
    anglevel = 3.0 * speed
    steps = int(abs(angle) / anglevel)
    delta = angle / steps
    return [delta] * steps


