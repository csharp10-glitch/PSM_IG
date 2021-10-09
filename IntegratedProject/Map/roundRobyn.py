# This class rotates the three classes of loss about the transmitter

# Python3 program for implementing
# Mid-Point Circle Drawing Algorithm
import math

import matplotlib.pyplot as plot
import numpy as np
from numpy import linspace


def midPointCircleDraw(x_centre, y_centre, r):
    x = r
    y = 0
    xy = list()
    # xy.append()

    # Printing the initial point the
    # axes after translation
    xy.append((x + x_centre, y + y_centre))

    # When radius is zero only a single
    # point be printed
    if (r > 0):
        xy.append((x_centre, -x + y_centre))
        xy.append((x_centre, x + y_centre))
        xy.append((-x + x_centre, y_centre))

    # Initialising the value of P
    P = 1 - r

    while x > y:

        y += 1

        # Mid-point inside or on the perimeter
        if P <= 0:
            P = P + 2 * y + 1

        # Mid-point outside the perimeter
        else:
            x -= 1
            P = P + 2 * y - 2 * x + 1

        # All the perimeter points have
        # already been printed
        if (x < y):
            break

        # Printing the generated point its reflection
        # in the other octants after translation
        xy.append((x + x_centre, y + y_centre))
        xy.append((-x + x_centre, y + y_centre))
        xy.append((x + x_centre, -y + y_centre))
        xy.append((-x + x_centre, -y + y_centre))

        # If the generated point on the line x = y then
        # the perimeter points have already been printed
        if x != y:
            xy.append((y + x_centre, x + y_centre))
            xy.append((-y + x_centre, x + y_centre))
            xy.append((y + x_centre, -x + y_centre))
            xy.append((-y + x_centre, -x + y_centre))
    return xy

def fillPointsZero(xy):
    # xy.sort()
    length = len(xy) // 2
    halfXY = xy[:length]
    otherHalf = xy[length:]
    for i in halfXY:
        x = int(math.fabs(2 * i[0]))
        # print(i)
        line = linspace(i[0], -1 * i[0], num=2*x, dtype=int)
        for j in line:
            xy.append((j,i[1]))
            # print(j, i[1])
    return xy

# def moveFullCircle(xy, x, y):
#     newXY = list()
#     for i in xy:
#         newXY.append((i[0]+x, i[1]+y))
#     return newXY

def moveFullCircle(xy, x, y):
    newXY = list()
    if len(xy[0])==2:
        for i in xy:
            newXY.append((i[0]+x, i[1]+y))
    else:
        for i in xy:
            newXY.append((i[0]+x, i[1]+y, i[2]))
    return newXY

def fillPoints(xy):
    xy.sort()
    print(xy)
    length = len(xy) // 2
    halfXY = xy[:length]
    otherHalf = xy[length:]
    for i in range(length):
        x = int(math.fabs(2 * halfXY[i][0]))
        print(x, halfXY[i][1])
        print(otherHalf[i][0], otherHalf[i][1])
        line = linspace(halfXY[i][0], otherHalf[i][0], int(math.fabs(halfXY[i][0] - otherHalf[i][0])), dtype=int)
        print(line)
        for j in line:
            xy.append((j,i[1]))
            # print(j, i[1])
    return xy

def drawFull(xy):
    xy.sort()
    length = len(xy)//2
    halfXY = xy[:length]
    for i in halfXY:
        x = int(math.fabs(2*i[0]))
        # print(x)
        line = linspace(i[0], -1*i[0],num=2*x, dtype=int)
        y = np.ones(2*x, dtype=int)
        y = y*i[1]
        plot.scatter(line, y)
    return 0


# xy = midPointCircleDraw(0, 0, 1000)
# xy.sort()
#
# # print(xy)
# # drawFull(xy)
# xy = fillPointsZero(xy)
# xy = moveFullCircle(xy, 45, 13)
# # print(len(xy))
# xy = list(set(xy))
# # print(len(xy))
# xy.sort()
#
# # print(xy)
# x, y = zip(*xy)
# plot.scatter(x, y)
# plot.show()

# Contributed by: SHUBHAMSINGH10
# Improved by: siddharthx_07