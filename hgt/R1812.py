import hgt
import math as m
import matplotlib.pyplot as plot

data = hgt.readHGT('N43W006.hgt')
hgt.hgtPlot(data)

clutter = {'water':[0,10], 'rural':[0,10], 'suburban':[10,10],
           'urban':[15,15],'forest':[15,15], 'city':[20,20]}
radioClimate = {'costal':'A1', 'inland':'A2', 'sea':'B'}

def lineOfSight(f, d):
    loss = 92.45 + 20*m.log10(f) + 20*m.log10(d)
    return loss

def J(v):
    J = 6.9 + 20*m.log10((m.sqrt(v*v-0.2*v+1.01)+v-0.1))
    if v <= -0.78:
        J = 0
    return J

def bullingtonDiffraction(hgt,hr):
    return

def arcsec(lat):
    lat = m.radians(lat)
    arcsec = 30.87*m.cos(lat)
    return arcsec

def eta():
    return

def DistToI(i,j,k,l, lat):
    x = i*i - k*k
    y = j*j - l*l
    dist = m.sqrt(x*x+y*y)
    dist = dist * arcsec(lat)
    return dist

def effectiveEarthRadius():
    dn = 0
    k50 = 157/(157-dn)
    ae = 6371*k50
    return ae



# f: frequency in GHz [0.03,3.0]
# phi: latitude in degrees [-80,80]
# psi: longitude in degrees [-180,180]
# h: antenna height above ground level in meters [1,3000]
# polarization: antenna polarity

def prop(f, phi_t, phi_r, psi_t, psi_r, h_t, h_r, polarization):
    lineOfSight()
    bullingtonDiffraction()
    return

# Path profile analysis variables
# d: great circle distnce km
# dht, dhr: distance to the horizon km
# thetaT, thetaR: horizon elevation angles mrad
# theta: path angular distance mrad
