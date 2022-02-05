import matplotlib.pyplot as plot
import time as t
# Get an area
from IntegratedProject.Loss.LineOfSight import losLoss
from IntegratedProject.Math import SphericalGeometry as SCM
import IntegratedProject.Map.Area as A
from IntegratedProject.Loss.Diffraction import slopeTxRx, slopeIntermediate, etaLoS, slopeRxPoint, bullingtonDistance, \
    etaTH, bullingtonLoss, marginalLoSDistance, minClear, hReq, lossDSph, j
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

print(sweet.minLat, ":", sweet.minLong, ":", sweet.maxLat, ":", sweet.maxLong)
print(sweet.de.shape)

# Add transmitters to the area, check to see they're within the area
# texas = Transmitter(39,-113, 100, 1500)
texas = Transmitter(38.97222222222222, -111.505, 100, 1875)
# texas = Transmitter(40.5,-112.5, 100, 1500)
cali = Transmitter(39.5,-113, 100, 1400)
tenn = Transmitter(39.5,-113, 100, 1200)
range = PowerAndRange.range(texas, 1)*1000
print("Loc Alt: ", A.getAltitude(sweet, texas.lat, texas.long))
print(range, ":", int(range/30.87))

# Run Line of sight, documenting the power imparted to each point
x, y = getIndex(sweet, texas)
texIndex = (x, y)
print(texIndex)

xy = midPointCircleDraw(0, 0, int(range*2/30.87))
# xy = midPointCircleDraw(0, 0, 5)
xy.sort()
xy = fillPointsZero(xy)
# test = xy
xy = moveFullCircle(xy, x, y)
# test = moveFullCircle(xy, x/2, y/2)
xy = list(set(xy))
print("xy filled and listed")
xy.sort()
print("xy sorted ")
# print(getLatLong(sweet, (3493,9000)))
# print(getLatLong(sweet, (5500, 9000)))
# print(getLatLong(sweet, (3500, 8982)))

# x, y = zip(*xy)
# plot.scatter(x, y)
# x, y = zip(*test)
# plot.scatter(x, y)


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

print("Number of points: ", len(xy))
print("COUNT:", count)
high = 0
hiList = list()
low = 0
for i in xy:
    count +=1
    rxll = getLatLong(sweet, i)
    rxalt = A.getAltitude(sweet, rxll[0], rxll[1])
    rx = GeoObject(rxll[0], rxll[1], rxalt)
    # print(i[0], i[1], )
    # sloppyXm.append((i[0],i[1], rxalt+200))
    rxcount += 1
    discard, line, di, hi, subRx = bresenhamsLine(sweet, texas, rx)
    if (count%1000)==0:
        print("COUNT:", count)
    #     print("RX_XY Lat/Long: ", rxll, ", Alt: ", rxalt)
    #     print(slopeTxRx(texas, rx))
    #     print("RX Lat: ", rx.lat, ", Long: ", rx.long, ", Alt: ", rx.altitude)
    #     print("Discard?: ", discard)
    #     print("Line indecies: ", line)
    #     print(count, "th distance: ", di)
    #     print("Height of ", count, "th terraing: ", hi)
    #     print("getIndex of swath and transmitter?: ", getIndex(sweet, texas))
    if len(subRx) !=0:
        slope = list()
        # print(slope)
        # print("RX Lat: ", rx.lat, ", Long: ", rx.long, ", Alt: ", rx.altitude)
        # print("Distance: ", SCM.greatCircleDistance(texas, rx))
        # print("Difference in height: ", (texas.altitude-rx.altitude))
        # print("Slope: ", (texas.altitude-rx.altitude)/SCM.greatCircleDistance(texas, rx))
        # print("TX-RX Slope: ", slopeTxRx(texas, rx))
        for j_index in subRx:
            # srx = GeoObject(j[0],j[1], j[2])
            # print("SubRX Lat: ", srx.lat, ", Long: ", srx.long, ", Alt: ", srx.altitude)
            trs = slopeTxRx(texas, j_index)

            slope.append(trs)
            # if (count%1000)==0:
            #     print("RX Lat: ", srx.lat, ", Long: ", srx.long, ", Alt: ", srx.altitude)
            #     print(texas.lat, texas.long, texas.altitude)
            #     print("slope", trs)
        # print(max(slope), slope[-1], max(slope)==slope[-1])
        # print(max(slope))
        # print(slopeTxRx(texas,rx))
        # print(max(slopeTxRx(texas, rx),min(slope)))
        sloppyXm.append((i[0], i[1], 10*max(slopeTxRx(texas, rx),min(slope))))
        if max(slope) >= slopeTxRx(texas, rx):
            str = slopeTxRx(texas, rx)
            etaArray = list()
            for srx in subRx:
                # print("rx: ", rx.lat)
                etaArray.append(etaLoS(texas,rx, srx))
            etaMax = max(etaArray)
            # print("v_max",etaMax, ", Type: ", type(etaMax))
            j_etaMax = j(etaMax)
            etaBPD = etaTH(texas, rx, srx)
            L_bull = bullingtonLoss(texas, rx, srx)
            d_los = marginalLoSDistance(texas, rx)
            sloppyXm.append((i[0],i[1], 2000))
            minimumClearance = minClear(texas, rx)
            h_req = hReq(texas, rx)
            sphericalDiffractionLoss = lossDSph(sweet, texas, rx)
        #     high+=1
        #     hiList.append(i)
        else:
            lineOfSight = losLoss(texas, rx)
            sloppyXm.append((i[0], i[1], lineOfSight))
        #     low+=1


            # break
        # break
    # if (count % 1000) == 0:
    #     print(slope)
    #     print(srx.lat, srx.long, srx.altitude)
    #     print(texas.lat, texas.long, texas.altitude)
    #     print(srx.altitude)
    #     print("slope", trs)
    #     print(max(slope), slope[-1], max(slope)==slope[-1])
# print(len(sloppyXm), len(xy))

print("High: ", high)
print(hiList)
print("Low: ", low)

# Paint the location
plot.imshow(sweet.de)
# Paint the power
# # x, y, z = zip(*xyz)
y, x, z = zip(*sloppyXm)
plot.scatter(x, y, 1, z, alpha=1.0)
# # Show
plot.show()