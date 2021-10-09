import math as m
import sphericalCoordinateMath as SCM
import transmitter as tm

k = SCM.averageCurvature

# stim = max((gi + 500*k*di*(d-di)-htc)/di)

def slopeIntermediate(terrain, tx):
    slope = terrain.de + 500 * k + tx.height
    return slope

def slopeTxRx(tx, rx):
    d = SCM.greatCircleDistance(tx, rx)
    slope = rx.height - tx.height
    slope /= d
    return slope


tm1 = tm.transmitter(40, 114, 1000)
tm2 = tm.transmitter(40, 113, 1000)


# print(SCM.greatCircleDistance(object1 = tm1,object2 = tm2)/3600)
# print(slopeTxRx(tm1,tm2))