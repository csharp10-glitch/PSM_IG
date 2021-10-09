import math as m

from IntegratedProject.Math import SphericalGeometry


def tropoScatter(point, transmitter, prob = 50):
    loss = 190.1+freqLoss(transmitter)+20*m.log10(SphericalGeometry.greatCircleDistance(point,transmitter)) \
           +0.573*SphericalGeometry.angle(point, transmitter) - 0.15*refract(point, transmitter) \
           - 10.125*m.log10(50/prob)**0.7
    return loss

def freqLoss(transmitter):
    return freqLoss(transmitter.freq)

def freqLoss(freq):
    loss = 25*m.log10(freq)-2.5*(m.log10(freq/2))**2
    return loss

def refract(point, transmitter):
    return 0