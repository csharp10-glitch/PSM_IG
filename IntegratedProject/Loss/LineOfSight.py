import math as m
import IntegratedProject.Map.Transmitter as T

from IntegratedProject.Math import SphericalGeometry
from IntegratedProject.Math.SphericalGeometry import greatCircleDistance


# eq 8 pg 9
def losLoss(d: float, freq: int):
    loss = 92.45 + 20 * m.log10(freq) + 20 * m.log10(d)
    return loss

# eq 8 pg 9
def losLoss(point: T.GeoPoint, transmitter: T.transmitter):
    return losLoss(greatCircleDistance(point,transmitter), transmitter.freq)

# eq 9a pg 10
def Esp(transmiter: T.transmitter, prob):
    return 2.6*(1-m.exp((SphericalGeometry.horizon(transmiter.altitude)/(-10))))*(m.log10(prob/50))

# eq 9b pg 10
def EsBeta(transmiter: T.transmitter, prob):
    return 2.6*(1-m.exp((SphericalGeometry.horizon(transmiter.altitude)/(-10))))*(m.log10(prob/50))

# eq 10 pg 10
def Lb0p(Lbfs, Esp):
    return Lbfs + Esp

# eq 11 pg 10
def Lb0b(Lbfs, EsBeta):
    return Lbfs + EsBeta


