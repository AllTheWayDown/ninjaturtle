from __future__ import division

from math import sin, cos, radians

#    data[0]  - X position
#    data[1]  - Y position
#    data[2]  - X scale
#    data[3]  - Y scale
#    data[4]  - angle/orientation in degrees
#    data[5]  - speed
#    data[6]  - cos(radians(angle)) - a cache
#    data[7]  - sin(radians(angle)) - a cache
#    data[8]  - red
#    data[9]  - green
#    data[10] - blue
#    data[11] - alpha


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
