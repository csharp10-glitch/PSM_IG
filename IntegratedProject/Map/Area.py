import IntegratedProject.Map.hgtImport as hgt
import math as m
import numpy as np
import matplotlib.pyplot as plot

from IntegratedProject.Math.SphericalGeometry import decimalDegreeToDMS, DMStoS


class area:
    def __init__(self, filename, setNulls = True, setNullsTo = 0.0, show = False, granularity = 30.87):
        self.loc = filename[0+4:19]
        filename = filename[0+3:]
        self.granularity = granularity
        # Hey look at me, automate me to find north or south
        latSign = filename[9]
        # print(filename[8])
        if latSign == 'N':
            latSign = 1
        else:
            latSign = -1
        # Hey look at me, automate me to find if east or west
        longSign = filename[12]
        if longSign == 'E':
            longSign = 1
        else:
            longSign = -1

        # Hey look at me! Automate me to get the locations
        lat = int(filename[10:12])
        long = int(filename[13:16])
        self.maxLat = latSign*lat
        self.minLat = self.maxLat - 1
        self.minLong = longSign*long
        self.maxLong = self.minLong + 1
        # print(filename)
        self.de, self.shape = hgt.readHGT(filename)
        # self.granularity = m.fabs(self.maxLat - self.minLat) / self.shape
        if setNulls == True:
            self.de = hgt.setNulls(self.de, setNullsTo)
        if show == True:
            hgt.hgtPlot(self.de)

    def __str__(self):
        return self.loc

class swath(area):
    def __init__(self, areas: area = [], filenames = [], setNulls = True, setNullsTo = 0.0):
        self.granularity = 30.87
        try:
            self.granularity = areas[0].granularity
        except IndexError:
            pass
        for i in filenames:
            place = area(i, setNulls, setNullsTo)
            # print(place)
            areas.append(place)
            # print(areas)
        maxLat = areas[0].maxLat
        minLat = areas[0].minLat
        maxLong = areas[0].maxLong
        minLong = areas[0].minLong

        for i in areas:
            if i.maxLat > maxLat:
                maxLat = i.maxLat
            if i.minLat <= minLat:
                minLat = i.minLat
            if i.maxLong >= maxLong:
                maxLong = i.maxLong
            if i.minLong < minLong:
                minLong = i.minLong
        # print(minLat, minLong, maxLat, maxLong)
        self.maxLat = maxLat
        self.minLat = minLat
        self.maxLong = maxLong
        self.minLong = minLong
        self.loc = str(minLat) + ';' + str(minLong) + ';' + str(maxLat) + ';' + str(maxLong)
        # print(self.loc)
        box = [(maxLat-minLat)*3600,(maxLong-minLong)*3600]
        self.bb = box
        # print(box)
        self.de = np.zeros(box)
        # print(self.area.shape)
        for k in areas:
            # print(k)
            x = (k.maxLat - maxLat)*-3600
            # print(k.lat - maxLat)
            y = (k.minLong - minLong)*3600
            # print(k.minlong - minLong)

            # print(y,y+3600)
            self.de[x:(x + 3600), y:(y + 3600)] = k.de[:3600, :3600]
            # for i in range(3600):
            #     for j in range(3600):
            #         self.area[x+i,y+j] = k.data[i,j]
        # plot.imshow(self.area, vmax = self.area.max(), vmin = -1)
        # plot.show()

def getAltitude(terrain, lat: float, long: float):
    minlat, minlong = terrain.minLat, terrain.minLong
    maxlat, maxlong = terrain.maxLat, terrain.maxLong
    # if((m.fabs(lat) < m.fabs(minlat) | (m.fabs(lat) > m.fabs(maxlat)) | (m.fabs(long) > m.fabs(maxlong)) | (m.fabs(long) < m.fabs(minlong))):
    #     print("Oops!  That was no valid number.  Try again...")
    lat = lat - minlat
    long = long - minlong
    lat = int(DMStoS(decimalDegreeToDMS(lat)))
    long = int(DMStoS(decimalDegreeToDMS(long)))
    height = terrain.de[lat][long]
    return height




# nbnw = area('data/N42W001.hgt')
# nbne = area('data/N43W006.hgt')

# sweet = swath([], ['MapData/N38W112.hgt','MapData/N38W114.hgt','MapData/N38W113.hgt','MapData/N38W115.hgt','MapData/N39W114.hgt','MapData/N39W113.hgt','MapData/N39W112.hgt','MapData/N39W115.hgt','MapData/N40W112.hgt','MapData/N40W113.hgt','MapData/N40W115.hgt','MapData/N40W114.hgt'], setNullsTo = 1200)
# # print(sweet.area.min())
# plot.imshow(sweet.de)
# plot.show()
#
# print(sweet.loc)

# print(nbnw.lat, 'a')
# print(nbnw.long, 'b')
# print(fn[4:7])

# print(SCM.decimalToArea([39.7604,-115], sweet))