import math
import os

import pandas as pd
from numpy import linspace
import numpy as np
from scipy.interpolate import RectBivariateSpline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# from IntegratedProject.GeoObject import Terrain


# def getRefract(terrain: Terrain):
#     lat = terrain.lat
#     long = terrain.long
    # get lat and long files, find index

    # get dN and  N0 based on lat long

def dN(lat, long):
    return 0

# eq 6 pg 8
def k50(dN):
    return 157/(157-dN)

# eq 7a pg 8
def ae(k50):
    return 6371*k50

def readInRefract():
    n50 = 'MapData/N050.TXT'
    dn50 = 'MapData/DN50.TXT'
    fn = 'MapData/LON.TXT'
    siz = os.path.getsize(n50)
    # dim = int(math.sqrt(siz / 2))
    print(siz)
    dim1 = 120
    dim2 = 240
    # assert dim1 * dim2 == siz, 'Invalid file size'
    data = np.fromfile(n50, count= dim1 * dim2, sep= '  ').reshape((dim1, dim2))
    # data = np.fromfile(fn)
    datapad = pd.read_csv(n50, '  ')
    print(data)
    # return data, dim1, dim2
    # for i in linspace(0, 360, 1.5):
    #     for j in linspace(-90, 90, 1.5):

# readInRefract()


n50 = 'MapData/N050.TXT'
dn50 = 'MapData/DN50.TXT'
fn1 = 'MapData/LAT.TXT'
fn2 = 'MapData/LON.TXT'
dim1 = 121
dim2 = 241
# Regularly-spaced, coarse grid
dx, dy = 1.5, 1.5
xmax, ymax = 360, 90
x = np.arange(0, xmax+dx, dx)
y = np.arange(-ymax, ymax+dy, dy)
X, Y = np.meshgrid(x, y)
data1 = np.fromfile(fn1, count= dim1 * dim2, sep= '  ').reshape((dim1, dim2))
data2 = np.fromfile(n50, count= dim1 * dim2, sep= '  ').reshape((dim1, dim2))
Z = data2
print(x.shape)
print(y.shape)
print(Z.shape)
print(data1)
print(data2)
print(Z)

interp_spline = RectBivariateSpline(y, x, Z)

# Regularly-spaced, fine grid
dx2, dy2 = 1, 1
x2 = np.arange(-xmax, xmax, dx2)
y2 = np.arange(-ymax, ymax, dy2)
X2, Y2 = np.meshgrid(x2, y2)
Z2 = interp_spline(y2, x2)

fig, ax = plt.subplots(nrows=1, ncols=2, subplot_kw={'projection': '3d'})
ax[0].plot_wireframe(X, Y, Z, color='k')

ax[1].plot_wireframe(X2, Y2, Z2, color='k')
for axes in ax:
    axes.set_zlim(300, 360)
    axes.set_axis_off()

fig.tight_layout()
plt.show()

