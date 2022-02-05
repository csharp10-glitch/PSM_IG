import scipy.constants as c
from IntegratedProject.Map.GeoObject import GeoObject
# from hgt.sphericalCoordinateMath import modifiedEffectiveEarthRadius
from IntegratedProject.Math.SphericalGeometry import modifiedEffectiveEarthRadius


class Transmitter(GeoObject):
    """a class that represents transmitters"""
    def __init__(self, lat, long, power = 1, altitude = 1, freq = 0.03, polarization = 'horizontal', pMean = 1.0, pLoc = 1.0):
        self.altitude = altitude
        self.freq = freq
        self.waveLength = c.c/(freq*1000000000)
        self.lat = lat
        self.long = long
        self.power = power
        self.range = 0
        self.polarization = polarization
        self.pMean = pMean
        self.pLoc = pLoc

def polarNorm(tx: Transmitter):
    kh = 0.036*(modifiedEffectiveEarthRadius()*tx.freq)**(-1/3)

