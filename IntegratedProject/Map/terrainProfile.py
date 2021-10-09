from IntegratedProject.Map import Area
from IntegratedProject.Map.GeoObject import GeoObject, Terrain
import math as m
import IntegratedProject.Map.Area

from IntegratedProject.Math.SphericalGeometry import greatCircleDistance, decimalDegreeToDMS, DMStoS, \
    DMStoDecimal
from IntegratedProject.Map.Transmitter import Transmitter


class terrainProfile(GeoObject):
    def __init__(self, terrain: Terrain, tx: GeoObject, rx: GeoObject):
        self.n = 0
        self.xy = list()
        self.di = []
        self.hi = []
        # clutter = []
        # gi = hi + clutter
        self.n, self.xy, self.di, self.hi = bresenhamsLine(terrain, tx, rx)


def bresenhamsLine(terrain: Terrain, tx: GeoObject, rx: GeoObject):
    dms2m = 30*60*60
    dx = decimalDegreeToDMS(m.fabs(tx.long - rx.long))
    dx = int(DMStoS(dx))
    dy = decimalDegreeToDMS(m.fabs(tx.lat - rx.lat))
    dy = int(DMStoS(dy))
    # print("dx", dx, "dy", dy)
    xy = list()
    di = list([0])
    hi = list([tx.altitude])
    xyz = list()
    D = 2 * dy - dx
    # print(D)
    geo: GeoObject = GeoObject(tx.lat, tx.long, tx.altitude)
    xi = 0
    yj = 0
    xi += int(DMStoS(decimalDegreeToDMS(tx.long-terrain.minLong)))
    yj += int((tx.lat - terrain.minLat)*dms2m / terrain.granularity)
    yj1 = 0
    # print("xi", xi, "yj", yj)
    xStep: int = int(dx / terrain.granularity)
    # xn = int(dx / xStep)
    # print(terrain.de.shape)
    for x in range(0, dx):
        xi += 1
        if D > 0:
            yj += 1
            # print("yj", yj)
            D -= 2 * dx
        D += 2 * dy
        # print(D)
        geo.long += DMStoDecimal([0,0,1.0])
        if(yj != yj1):
            geo.lat += DMStoDecimal([0,0,1.0])
        # else:
            # print("works")
        # print("geolat", geo.lat, "geolong", geo.long)
        yj1 = yj
        # geo.altitude = terrain.de[xi][yj]
        xy.append((xi,yj))
        di.append(greatCircleDistance(geo,tx))
        hi.append(terrain.de[xi][yj])
        xyz.append((xi,yj,terrain.de[xi][yj]))
    return xStep, xy, di, hi, xyz

# sweet = Area.swath([], ['Map\MapData\\N38W112.hgt', 'Map/MapData\\N38W114.hgt', 'Map/MapData\\N38W113.hgt', 'Map/MapData\\N38W115.hgt', 'Map/MapData\\N39W114.hgt', 'Map/MapData\\N39W113.hgt', \
#                    'Map/MapData\\N39W112.hgt','Map/MapData\\N39W115.hgt','Map/MapData\\N40W112.hgt','Map/MapData\\N40W113.hgt','Map/MapData\\N40W115.hgt','Map/MapData\\N40W114.hgt'], setNullsTo = 1200)
# # print(sweet.area.min())
# # plot.imshow(sweet.de)
# # plot.show()
#
# # print(sweet.loc)
#
# tran = Transmitter(37.1, -115, power = 1, altitude =1000 + Area.getAltitude(sweet, 37.1,-115), freq = 0.3, polarization ='horizontal', pMean = 1.0, pLoc = 1.0)
# rx = GeoObject(37.1,-112.1,1700)
# step, xy, di, hi = bresenhamsLine(sweet, tran, rx)
# print("Steps")
# print(step)
# print("XY Output")
# print(xy)
# print("Distances")
# print(di)
# print("Profile")
# print(hi)

# x, y = zip(*xy)
# plot.scatter(x, y)
# plot.show()
