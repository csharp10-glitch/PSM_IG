import math


def range(tx, power):
    pt = tx.power
    pr = power
    range = math.sqrt(pt/(4*math.pi*pr))
    return range


def signalStrength(tx, distance):
    pr = tx.power/(4*math.pi*distance*distance)
    return pr
