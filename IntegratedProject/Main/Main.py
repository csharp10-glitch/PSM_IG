import matplotlib.pyplot as plot
import time as t
# Get an area
import IntegratedProject.Map.Area as A
from IntegratedProject.Loss.Diffraction import slopeTxRx
from IntegratedProject.Map.GeoObject import GeoObject
from IntegratedProject.Map.Transmitter import Transmitter
from IntegratedProject.Map.findInArray import getIndex, getLatLong
from IntegratedProject.Map.roundRobyn import midPointCircleDraw, fillPoints, moveFullCircle, fillPointsZero
from IntegratedProject.Map.terrainProfile import bresenhamsLine
from IntegratedProject.Math.SphericalGeometry import greatCircleDistance
from IntegratedProject.RadarEquations import PowerAndRange


# sweet = A.swath([], ['Map\MapData\\N38W112.hgt','Map/MapData\\N38W114.hgt','Map/MapData\\N38W113.hgt','Map/MapData\\N38W115.hgt','Map/MapData\\N39W114.hgt','Map/MapData\\N39W113.hgt', \
#                    'Map/MapData\\N39W112.hgt','Map/MapData\\N39W115.hgt','Map/MapData\\N40W112.hgt','Map/MapData\\N40W113.hgt','Map/MapData\\N40W115.hgt','Map/MapData\\N40W114.hgt'], setNullsTo = 1200)

sweet = A.swath([], ['Map/MapData\\N39W114.hgt','Map/MapData\\N39W113.hgt', \
                   'Map/MapData\\N39W112.hgt','Map/MapData\\N40W112.hgt','Map/MapData\\N40W113.hgt','Map/MapData\\N40W114.hgt'], setNullsTo = 1200)


# Add transmitters to the area, check to see they're within the area
texas = Transmitter(39,-113, 100, 4000)
cali = Transmitter(39.5,-113, 100, 1400)
tenn = Transmitter(39.5,-113, 100, 1200)
range = PowerAndRange.range(texas, 1)*500
print(range)

# Run Line of sight, documenting the power imparted to each point
x, y = getIndex(sweet, texas)
texIndex = (x, y)

xy = midPointCircleDraw(0, 0, int(range/30.87))
xy.sort()
xy = fillPointsZero(xy)
test = xy
xy = moveFullCircle(xy, x, y)
test = moveFullCircle(xy, x/2, y/2)
xy = list(set(xy))
print("xy filled and listed")
xy.sort()
print("xy sorted ")

# x, y = zip(*xy)
# plot.scatter(x, y)
x, y = zip(*test)
plot.scatter(x, y)


sloppyXm = list()
# print(len(xy))
rxcount = 0
count = 0
# a, b = getIndex(sweet, texas)
# see = (a, b)
# print(see)
# print(xy[0])
# print(see in xy)

# print(greatCircleDistance(texas, cali))
# print(greatCircleDistance(texas, tenn))
# print(greatCircleDistance(tenn, texas))
# print(greatCircleDistance(texas, texas))
# print(slopeTxRx(texas, cali))
# print(slopeTxRx(texas, tenn))
for i in xy:
    count +=1
    if count%1000==0:
        print(count)
    rxll = getLatLong(sweet, i)
    # print(rxll)
    rxalt = A.getAltitude(sweet, rxll[0], rxll[1])
    # print(rxalt)
    rx = GeoObject(rxll[0], rxll[1], rxalt)
    # print(rx.lat, rx.long, rx.altitude)
    rxcount += 1
    discard, line, di, hi, subRx = bresenhamsLine(sweet, texas, rx)
    # print(discard)
    # print(line)
    # print(di)
    # print(hi)
    print(line)
    print(getIndex(sweet, texas))
    if len(subRx) !=0:
        slope = list()
        # print(slope)
        for j in subRx:
            srx = GeoObject(j[0],j[1], j[2])
            # print(srx.lat, srx.long, srx.altitude)
            # print(texas.lat, texas.long, texas.altitude)
            # print(srx.altitude)
            trs = slopeTxRx(texas, srx)
            slope.append(trs)
            # print("slope", trs)
        # print(max(slope), slope[-1], max(slope)==slope[-1])
        if max(slope) == slope[0]:
            sloppyXm.append((i[0],i[1], 5000))
            # print("higher")
        else:
            sloppyXm.append((i[0], i[1], 0))
            # print("lower")
            # break
    break
# print(len(sloppyXm), len(xy))

# Paint the location
plot.imshow(sweet.de)
# Paint the power
# # x, y, z = zip(*xyz)
x, y, z = zip(*sloppyXm)
plot.scatter(x, y, 1, z, alpha=1)
# # Show
plot.show()