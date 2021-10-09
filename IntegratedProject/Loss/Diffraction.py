import math
import math as m

from IntegratedProject.Map.Transmitter import Transmitter
from IntegratedProject.Map.GeoObject import GeoObject
from IntegratedProject.Math import SphericalGeometry as SCM

# eq 12 pg 10
def j(eta: float):
    jOfEta = 6.9 + 20*m.log10(m.sqrt((eta-0.1)**2 +1) + eta -0.1)
    return jOfEta

k = SCM.averageCurvature

# stim = max((gi + 500*k*di*(d-di)-htc)/di)

# eq 13 pg 11
def slopeIntermediate(terrain: GeoObject, tx:Transmitter, rx: GeoObject):
    fullDistance = SCM.greatCircleDistance(rx, tx)
    slope = slopeIntermediate(terrain, tx, fullDistance)
    return slope

# eq 13 pg 11
def slopeIntermediate(terrain: GeoObject, tx:Transmitter, rxDistance):
    pointDistance = SCM.greatCircleDistance(terrain,tx)
    slope = terrain.altitude + 500 * k * pointDistance*(rxDistance-pointDistance) - tx.height
    slope /= pointDistance
    return slope

# eq 14 pg 11
def slopeTxRx(tx: Transmitter, rx: GeoObject):
    d = SCM.greatCircleDistance(tx, rx)
    if d<1:
        print(d)
    slope = rx.altitude - tx.altitude
    # print(slope)
    slope /= d
    # print(slope)
    return slope

# eq 15 pg 11
def etaLoS(terrain: GeoObject, tx:Transmitter, rxDistance, rxAltitude):
    pointDistance = SCM.greatCircleDistance(terrain, tx)
    totalTossPointD = rxDistance - pointDistance
    eta = terrain.altitude + 500*k*pointDistance*totalTossPointD
    eta -= (tx.altitude*totalTossPointD+rxAltitude*pointDistance)/rxDistance
    eta *= m.sqrt((0.002*rxDistance)/(tx.waveLength*pointDistance*totalTossPointD))
    return eta

# eq 16 pg 11
def Luc(etaArray):
    return max(etaArray)

#eq 17 pg 12
def slopeRxPoint(terrain: GeoObject, rx:GeoObject, txDistance):
    pointDistance = SCM.greatCircleDistance(terrain,rx)
    slope = terrain.altitude + 500 * k * pointDistance*(txDistance-pointDistance) - rx.altitude
    slope /= txDistance - pointDistance
    return slope

#eq 17 pg 12
def slopeRxPoint(terrain: GeoObject, rx:GeoObject, tx: Transmitter):
    fullDistance = SCM.greatCircleDistance(rx, tx)
    slope = slopeRxPoint(terrain, rx, fullDistance)
    return slope

# eq 18 pg 12
def bullingtonDistance(rx: GeoObject, tx: Transmitter, stim, srim):
    fullDistance = SCM.greatCircleDistance(rx,tx)
    bullD = rx.altitude - tx.altitude + srim*fullDistance
    bullD /= (stim+srim)
    return bullD

# eq 19 pg 12 eta for transhorizon path
def etaTH(bullingtonDistance, tx: Transmitter, rx: GeoObject, stim):
    fullDistance = SCM.greatCircleDistance(rx,tx)
    eta = tx.altitude + stim+bullingtonDistance
    eta -= (tx.altitude*(fullDistance-bullingtonDistance)+rx.altitude*bullingtonDistance)/fullDistance
    eta *= m.sqrt((0.002*fullDistance)/(tx.waveLength*bullingtonDistance*(fullDistance-bullingtonDistance)))
    return eta

# eq 21 pg 12 bullington diffraction loss
def bullingtonLoss(terrain: GeoObject, tx: Transmitter, rx: GeoObject):
    stim = slopeIntermediate(terrain, tx, rx)
    srim = slopeRxPoint(terrain, rx, tx)
    bullDist = bullingtonDistance(rx, tx, stim, srim)
    loss = j(etaTH(bullDist, tx, rx, stim))
    return loss

# eq 22 pg 12 marginal LoS distance for a smooth path
def marginalLoSDistance(tx: Transmitter, rx: GeoObject):
    lat = (tx.lat + rx.lat)/2.0
    eRad = SCM.geocentricRadius(lat)
    dLoS = math.sqrt(2*eRad)*(m.sqrt(0.001*tx.altitude)+m.sqrt(0.001*tx.altitude))
    return dLoS

# eq 23 pg 12 minimum clearance height between the curved-Earth
# path and the ray between the antennas
def minClear(tx: Transmitter, rx: GeoObject):
    lat = (tx.lat + rx.lat) / 2.0
    eRad = SCM.geocentricRadius(lat)
    d = SCM.greatCircleDistance(tx,rx)
    dse2 = eq24b(tx,rx)
    dse1 = d-dse2
    group1 = (tx.altitude-500*dse1*dse1/eRad)*dse2
    group2 = (rx.altitude-500*dse2*dse2/eRad)*dse1
    height = (group1+group2)/2.0
    return height

# eq 24a pg 12
def eq24a(tx: Transmitter, rx: GeoObject):
    d = SCM.greatCircleDistance(tx,rx)
    b = eq24c(tx,rx)
    dse1 = (1+b)*d/2.0
    return dse1

# eq 24b pg 12
def eq24b(tx: Transmitter, rx: GeoObject):
    d = SCM.greatCircleDistance(tx, rx)
    dse1 = eq24a(tx,rx)
    dse2 = d-dse1
    return dse2

# eq 24c pg 12
def eq24c(tx: Transmitter, rx: GeoObject):
    c = eq24d(tx, rx)
    mc = eq24e(tx, rx)
    acdeg = (((3*c)/2.0)*m.sqrt((3*mc)/((mc+1)**3)))
    cdeg = m.cos((acdeg+m.pi)/3.0)
    b = 2.0*cdeg*m.sqrt((mc+1)/(3*mc))
    return b

# eq 24d pg 13
def eq24d(tx: Transmitter, rx: GeoObject):
    c = (tx.altitude-rx.altitude)/(tx.altitude+rx.altitude)
    return c

# eq 24e pg 13
def eq24e(tx: Transmitter, rx: GeoObject):
    lat = (tx.lat + rx.lat) / 2.0
    eRad = SCM.geocentricRadius(lat)
    d = SCM.greatCircleDistance(tx, rx)
    mc = (250*d*d)/(eRad*(tx.altitude+rx.altitude))
    return mc

# eq 25 pg 13 Required clearance for zero diffraction loss
def hReq(tx: Transmitter, rx):
    d = SCM.greatCircleDistance(tx, rx)
    dse2 = eq24b(tx, rx)
    dse1 = d - dse2
    lambdas = tx.waveLength
    hreq = 17.456*m.sqrt(dse1*dse2*lambdas/d)
    return hreq

# eq 26 pg 13
def modEarthRad(tx: Transmitter, rx: GeoObject):
    d = SCM.greatCircleDistance(tx, rx)
    hchs = m.sqrt(tx.altitude)+m.sqrt(rx.altitude)
    aem = 500*((d/hchs)**2)
    return aem

# eq 27 pg 11
def lossDSph(ter, tx: Transmitter, rx: GeoObject):
    ldsph = (1-(minClear(tx,rx)/hReq(tx,rx)))*lossDft(ter, tx, rx)
    return ldsph

# eq 28 pg 11
def lossDft(terrain: GeoObject,tx: Transmitter, rx: GeoObject):
    w = omega(terrain, tx, rx)
    ldft = w*ldftSea() + (1-w)*ldftLand()
    return ldft

# eq 28 pg 11
def omega(terrain: GeoObject, tx: Transmitter, rx: GeoObject):
    w = tx.altitude
    return w

# eq 28 pg 11
def ldftSea():
    er = 80.0
    sigma = 5.0
    return 0

# eq 28 pg 11
def ldftLand():
    er = 22.0
    sigma = 0.003
    return 0

def sig():
    return 0.003

def epsilon():
    return 22.0

# eq 29a pg 14 Normalized factor for surface admittance for horizontal polarization
def kH(terrain: GeoObject,tx: Transmitter, rx: GeoObject):
    eRad = modEarthRad(tx, rx)
    sigma = sig()
    er = epsilon()
    kh = 18.0*sigma/tx.freq
    kh = kh*kh
    kh += (er-1.0)**2.0
    kh = m.sqrt(m.sqrt(kh))
    kh = 1/kh
    kh *= 0.036
    addf = eRad*tx.freq
    addf = addf**(-1.0/3.0)
    kh = kh*addf
    return kh

# eq 29b pg 14
def kV(ter, tx, rx):
    er = epsilon()
    sigma = sig()
    kh = kH(ter,tx,rx)
    g1 = 18*sigma/tx.freq
    g1 = g1*g1
    g1 += er*er
    g1 = m.sqrt(g1)
    kv = kh*g1
    return kv

# eq 30 pg 14
def betaDFT(k):
    num = 1+1.6*k*k+0.67*k*k*k*k
    den = 1 + 4.5*k*k + 1.53 *k*k*k*k
    beta = num/den
    return beta

# eq 31 pg 14
def normedDist(ter, tx: Transmitter, rx):
    k = 0
    if (tx.polarization == "horizontal"):
        k = kH(ter, tx, rx)
    else:
        k = kV(ter, tx, rx)
    beta = betaDFT(k)
    eRad = modEarthRad(tx, rx)
    d = SCM.greatCircleDistance(tx, rx)
    f = tx.freq
    x = f/(eRad*eRad)
    x = x**(1.0/3.0)
    x = 21.88*beta*x*d
    return x

# eq 32 pg 14
def normedHeights(ter, tx, rx):
    k = 1
    pol = tx.polarization
    if (pol == "vertical"):
        k = kV(ter, tx, rx)
    else:
        k = kH(ter, tx, rx)
    bdft = betaDFT(k)
    eRad = modEarthRad(tx, rx)
    base = 0.9575*bdft*((tx.frequency*tx.frequency/eRad)**(1.0/3.0))
    normTx = base*hesph(tx)
    normRx = base*hesph(rx)
    return normTx, normRx

# eq 33 pg 14
def difDisFunc(x):
    fx = 1
    if (x < 1.6):
        fx = -20*m.log10(x)-5.6488*x**1.425
    else:
        fx = 11 + 10*m.log10(x)-17.6*x
    return fx

# eq 34 pg 14 and eq 35 pg 14
def normedHeightFunc(y, k):
    gy = 1
    B = betaDFT(k)*y #eq 35
    if (B > 2):
        gy = 17.6*(B-1.1)**0.5-5*m.log10(B-1.1-8.0)
    else:
        gy = 20*m.log10((B+0.1*B*B*B))
    return gy

# eq 36 pg 14
def L_dft(fx, gyt, gyr):
    ldft = -fx-gyt-gyr
    return ldft

# eq 37/38/a/b pg 15 FIX THIS LATER
def hesph(geoobject):
    return geoobject.altitude

# eq 39 pg15
def L_d(L_bulla, L_dsph, L_bulls):
    ld = L_bulla + max(L_dsph - L_bulls, 0)
    return ld





