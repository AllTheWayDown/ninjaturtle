from __future__ import division

from math import sin, cos, radians

# model[0]  - X position
# model[1]  - Y position
# model[2]  - X scale
# model[3]  - Y scale
# model[4]  - heading in degrees
# model[5]  - orientation in degrees
# model[6]  - cos(radians(heading)) - a cache
# model[7]  - sin(radians(heading)) - a cache
# model[8]  - cos(radians(orientation)) - a cache
# model[9]  - sin(radians(orientation)) - a cache
# model[10] - speed
# model[11] - unused
# model[12] - unused
# model[13] - unused
# model[14] - unused
# model[15] - unused


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
