import os
import math
import numpy
import matplotlib.pyplot as plot
import numpy as np
import pandas as pd

def readHGT(filename):
    fn = filename
    # print(fn)
    fn = r'C:\Users\chris\PycharmProjects\school\IntegratedProject\Map\\' + fn
    siz = os.path.getsize(fn)
    dim = int(math.sqrt(siz / 2))
    assert dim * dim * 2 == siz, 'Invalid file size'
    data = numpy.fromfile(fn, numpy.dtype('>i2'), dim * dim).reshape((dim, dim))
    return data, dim

def readToDataframe(filename):
    fn = filename
    # print(fn)
    fn = r'C:\Users\chris\PycharmProjects\school\IntegratedProject\Map\\' + fn
    siz = os.path.getsize(fn)
    dim = int(math.sqrt(siz / 2))
    assert dim * dim * 2 == siz, 'Invalid file size'
    data = numpy.fromfile(fn, numpy.dtype('>i2'), dim * dim).reshape((dim, dim))
    data = pd.DataFrame(data)
    return data


data = readToDataframe('MapData\\N38W112.hgt')
print(data)
print(data.max().max())
print(data.min())
plot.figure()
plot.subplot(211)
plot.imshow(data, vmax = data.max().max(), vmin = -100, cmap='terrain')
data.replace(-32768, np.nan, inplace=True)
# data.fillna(data.mean(), inplace=True)
data.interpolate(method='polynomial', order = 3, inplace=True)
plot.subplot(212)
plot.imshow(data, vmax = data.max().max(), vmin = -100, cmap='terrain')
plot.show()
# data.plot(x = 'd', y = 'e', kind = 'scatter')