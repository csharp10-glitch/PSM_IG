import math as m
import numpy as np

# from IntegratedProject.GeoObject import GeoObject
# from IntegratedProject.Transmitter import Transmitter

arcSec = 30.87 # m longitude
averageEarthRadius = 6371 # km
averageCurvature = 1/6371 # km^-1
polarRadius = 6356.7523 # km
equatorialRadius = 6378.1370 # km


def geocentricRadius(lat):
    radianLat = m.radians(lat)
    cosLat = m.cos(radianLat)
    sinLat = m.sin(radianLat)
    acosLat = equatorialRadius * equatorialRadius * cosLat * cosLat
    a2cosLat = equatorialRadius * equatorialRadius * acosLat
    bsinLat = polarRadius*polarRadius*sinLat*sinLat
    b2sinLat = polarRadius*polarRadius*bsinLat
    radius = m.sqrt((a2cosLat+b2sinLat)/(acosLat+bsinLat))
    return radius

def arcSecLat(lat):
    radianLat = m.radians(lat)
    arcSecLat = arcSec*m.cos(radianLat)
    return arcSecLat

def greatCircleDistance(object1, object2):
    lat1 = m.radians(object1.lat)
    long1 = m.radians(object1.long)
    lat2 = m.radians(object2.lat)
    long2 = m.radians(object2.long)
    deltaLat = lat1 - lat2
    deltaLong = long1 - long2
    sinLat = m.sin(0.5*deltaLat)
    sinLat = sinLat*sinLat
    sinLong = m.sin(0.5*deltaLong)
    sinLong = sinLong*sinLong
    deltaSigma = 2*m.asin(m.sqrt(sinLat+m.cos(lat1)*m.cos(lat2)*sinLong))
    greatCircleDistance = deltaSigma*averageEarthRadius
    return greatCircleDistance

def curvature(lat):
    r = geocentricRadius(lat)
    k = 1/r
    return k

def decimalDegreeToDMS(angle): #in degrees
    fractional = angle - int(angle)
    minutes = int(fractional*60)
    seconds = (fractional*60-minutes)*60
    return [int(angle), minutes, seconds]

def DMStoDecimal(angle):
    decimal = angle[0] + angle[1]/60 + angle[2]/3600
    return decimal

def horizon(height, exact = False, lat = 0):
    if exact == True:
        r = geocentricRadius(lat)
        horizon = m.sqrt(height*(2*r+height)/1000)
    else:
        horizon = 3.57*m.sqrt(height)
    return horizon

def decimalToArea(coordinate,array):
    dimensions = array.bb
    minLat = array.minLat
    maxLat = array.maxLat
    minLong = array.minLong
    maxLong = array.maxLong
    print(minLat)
    print(maxLat)
    print(minLong)
    print(maxLong)
    print(coordinate)
    if minLat > coordinate[0] or maxLat < coordinate[0]:
        raise ValueError('Coordinate not in map')
    elif minLong > coordinate[1] or maxLong < coordinate[1]:
        raise ValueError('Coordinate not in map')
    deltaX = (maxLat - minLat) / dimensions[0]
    deltaY = (maxLong - minLong) / dimensions[1]
    indexX = int((coordinate[0] - minLat)/deltaX)
    indexY = int((coordinate[1] - minLong)/deltaY)
    return [indexX, indexY]

#  eq 22
def smoothLoSDistance(tx, rx):
    d = m.sqrt(0.001*tx.altitude)
    d += m.sqrt(0.001*rx.altitude)
    d *= m.sqrt(2*averageEarthRadius)
    return d

# eq 23
def minimumClearance(tx, rx):
    d = greatCircleDistance(tx, rx)
    dse1 = (arbB(tx, rx)+1)*d*0.5
    dse2 = d - dse1
    hse = (tx.altitude - 500*dse1*dse1*averageCurvature)*dse2 + (rx.altitude - 500*dse2*dse2*averageCurvature)*dse1
    hse /= d
    return hse

# eq 25
def hReq(tx, rx):
    waveLength = tx.waveLength
    d = greatCircleDistance(tx, rx)
    dse1 = (arbB(tx, rx) + 1) * d * 0.5
    dse2 = d - dse1
    reqH = 17.456*m.sqrt(*dse1*dse2*waveLength/d)
    return reqH

# eq 26
def modifiedEffectiveEarthRadius(tx, rx):
    d = greatCircleDistance(tx, rx)
    aem = 500*(d/(m.sqrt(tx.altitude)+m.sqrt(rx.altitude)))**2
    return aem

#  eq 24c
def arbB(tx, rx):
    c = arbC(tx, rx)
    mc = arbM_c(tx, rx)
    b = 3*mc/((mc+1)**3)
    b = m.sqrt(b)
    b *= 1.5*c
    b = m.acos(b)/3
    b += m.pi/3
    b = m.cos(b)
    b *= 2*m.sqrt((mc+1)/(3*mc))
    return b

#  eq 24d
def arbC(tx, rx):
    c = tx.altitude-rx.altitude
    c /= tx.altitude + rx.altitude
    return c

#  eq 24e
def arbM_c(tx, rx):
    d = greatCircleDistance(tx, rx)
    mc = 250*d*d
    mc /= (averageEarthRadius*(tx.altitude + rx.altitude))
    return mc





