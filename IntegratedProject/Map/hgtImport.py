import os
import math
import numpy
import matplotlib.pyplot as plot

def readHGT(filename):
    fn = filename
    # print(fn)
    fn = r'C:\Users\chris\PycharmProjects\school\IntegratedProject\Map\\' + fn
    siz = os.path.getsize(fn)
    dim = int(math.sqrt(siz / 2))
    assert dim * dim * 2 == siz, 'Invalid file size'
    data = numpy.fromfile(fn, numpy.dtype('>i2'), dim * dim).reshape((dim, dim))
    return data, dim

def setNulls(hgtData, setTo = 0):
    hgtDataX = hgtData.copy()
    hgtDataX[hgtDataX == -32768] = setTo
    # for i in range(3600):
    #     for j in range(3600):
    #         if hgtDataX[i,j] == -32768:
    #             hgtDataX[i,j] = setTo
    return hgtDataX

def hgtPlot(data):
    minimum = data.min()
    if minimum == -32768:
        minimum = 0
    maximum = data.max()
    plot.imshow(data, vmax=maximum,vmin=minimum, cmap='terrain')
    plot.show()
    return

dat = readHGT('MapData\\N38W112.hgt')
hgtPlot(dat[0])

# dat = readHGT('MapData/N42W002.hgt')
# hgtPlot(dat[0])




#
#
#
# fn = 'N42W001.hgt'
# siz = os.path.getsize(fn)
# dim = int(math.sqrt(siz/2))
# assert dim*dim*2 == siz, 'Invalid file size'
# data = numpy.fromfile(fn, numpy.dtype('>i2'), dim*dim).reshape((dim, dim))
#
# dita = data.copy()
# minimum = data.min()
# maximum = data.max()
# print(minimum, maximum)
# for i in range(3600):
#     for j in range(3600):
#         if data[i,j] == minimum:
#             dita[i,j] = maximum
# print(dita.min())
#
# minimum = dita.min()
# maximum = dita.max()
# print(minimum, maximum)
# for i in range(3600):
#     for j in range(3600):
#         if dita[i,j] == minimum:
#             dita[i,j] = maximum
# print(dita.min())
#
# data = readHGT('N42W001.hgt')
# print(data.min())
# data1 = setNulls(data,0)
# #
# #
# plot.imshow(data)
# plot.show()
# plot.imshow(data1)
# plot.show()
#
# plot.imshow(data, vmax=3288, vmin=0)
# plot.show()
#
# plot.imshow(data, vmax=3288, vmin=minimum)
# plot.show()