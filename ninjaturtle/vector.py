from __future__ import division

from math import sin, cos, radians

# model[0] - X position
# model[1] - Y position
# model[2] - X scale
# model[3] - Y scale
# model[4] - angle/orientation in degrees
# model[5] - speed
# model[6] - cos(radians(angle)) - a cache
# model[7] - sin(radians(angle)) - a cache

def move(data, distance):
    data[0] += data[6] * distance
    data[1] += data[7] * distance

def rotate(data, angle):
    data[4] += angle
    theta = radians(data[4])
    data[6] = cos(theta)
    data[7] = sin(theta)

def move_with_heading(data, values):
    distance, heading = values
    theta = radians(heading)
    data[0] += cos(theta) * distance
    data[1] += sin(theta) * distance



