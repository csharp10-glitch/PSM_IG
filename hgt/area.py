import hgt as hgt
import numpy as np
import matplotlib.pyplot as plot
# import sphericalCoordinateMath as SCM

class area:
    def __init__(self, filename, setNulls = True, setNullsTo = 0.0, show = False):
        self.loc = filename[0:12]
        latSign = filename[5]
        if latSign == 'N':
            latSign = 1
        else:
            latSign = -1
        longSign = filename[8]
        if longSign == 'E':
            longSign = 1
        else:
            longSign = -1
        lat = int(filename[5+1:5+3])
        long = int(filename[5+4:5+7])
        self.maxLat = latSign*lat
        self.minLat = self.maxLat - 1
        self.minLong = longSign*long
        self.maxLong = self.minLong + 1
        self.de, self.shape = hgt.readHGT(filename)
        if setNulls == True:
            self.de = hgt.setNulls(self.de, setNullsTo)
        if show == True:
            hgt.hgtPlot(self.de)

    def __str__(self):
        return self.loc

class swath:
    def __init__(self, areas = [], filenames = [], setNulls = True, setNullsTo = 0.0):
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
        self.maxLat = maxLat
        self.minLat = minLat
        self.maxLong = maxLong
        self.minLong = minLong
        self.loc = str(maxLat) + ';' + str(minLong) + ';' + str(minLat) + ';' + str(maxLong)
        box = [(maxLat-minLat)*3600,(maxLong-minLong)*3600]
        self.bb = box
        self.de = np.zeros(box)
        # print(self.area.shape)
        for k in areas:
            # print(k)
            x = (k.maxLat - maxLat)*-3600
            # print(k.lat - maxLat)
            y = (k.minLong - minLong)*3600
            # print(k.minlong - minLong)
            # print(x,(x+3600),y,y+3600)
            self.de[x:(x + 3600), y:(y + 3600)] = k.de[:3600, :3600]
            # for i in range(3600):
            #     for j in range(3600):
            #         self.area[x+i,y+j] = k.data[i,j]
        # plot.imshow(self.area, vmax = self.area.max(), vmin = -1)
        # plot.show()


# nbnw = area('data/N42W001.hgt')
# nbne = area('data/N43W006.hgt')

sweet = swath([], ['data/N38W112.hgt','data/N38W114.hgt','data/N38W113.hgt','data/N38W115.hgt','data/N39W114.hgt','data/N39W113.hgt','data/N39W112.hgt','data/N39W115.hgt','data/N40W112.hgt','data/N40W113.hgt','data/N40W115.hgt','data/N40W114.hgt'], setNullsTo = 1200)
# print(sweet.area.min())
plot.imshow(sweet.de)
plot.show()

print(sweet.loc)

# print(nbnw.lat, 'a')
# print(nbnw.long, 'b')
# print(fn[4:7])

# print(SCM.decimalToArea([39.7604,-115], sweet))