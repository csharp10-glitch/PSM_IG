import math as m
import numpy as np
import os
import binascii as b

# Main file: file.shp
# Index file: file.shx
# dBASE table: file.dbf
shapeType = {0:'null',1:'point',3:'polyline',5:'polygon',8:'multipoint',31:'multipatch'}

# datatypes
# Integer: Signed 32-bit integer (4 bytes)
# Double: Signed 64-bit IEEE double precision floating point number (8 bytes)
# inf, -inf, and NaN are verbote

noData = -1e38

class shapefile:
    def __init__(self, fn):
        filename = fn
        shx = filename[:-3] + 'shx'
        index = readSHX(shx)
        self.fileCode = 9994
        if 9994 != np.fromfile(filename, np.dtype('>i4'), 1):
            raise ValueError(filename, ' does not appear to be a .shp shapefile')
        self.fileLength = np.fromfile(filename, np.dtype('>i4'), 1, offset = 24)
        self.shapeType = np.fromfile(filename, np.dtype('<i4'), 1, offset=32)
        self.minLat, self.minLong, self.maxLat, self.maxLong, self.zMin, self.zMax, self.mMin, self.mMax = np.fromfile(filename, np.dtype('<d'), 8, offset=36)
        self.recordNumber, self.contentLength = np.fromfile(filename, np.dtype('>i4'), 2, offset=100)
        self.shapes = []
        for i in index:
            shapeType = np.fromfile(filename, np.dtype('<i4'), 1, offset=2 * i + 8)
            boundingBox = np.fromfile(filename, np.dtype('<d'), 4, offset=2 * i + 12)
            numberOfParts = np.fromfile(filename, np.dtype('<i4'), 1, offset=2 * i + 44)
            numberOfPoints = np.fromfile(filename, np.dtype('<i4'), 1, offset=2 * i + 48)
            partIndex = np.fromfile(filename, np.dtype('<i4'), 1, offset=2 * i + 52)
            points = np.fromfile(filename, np.dtype('<d'), 2 * numberOfPoints[0], offset=2 * i + 56)
            self.shapes.append(shape(shapeType, boundingBox, numberOfParts, numberOfPoints, partIndex, points))

    def __repr__(self):
        stringShapes = []
        for i in self.shapes:
            stringShapes.append(i.__repr__())
        return stringShapes

class shape:
    def __init__(self, shapeType, boundingBox, numberOfParts, numberOfPoints, partIndex, points):
        self.shapeType = shapeType
        self.boundingBox = boundingBox
        self.numberOfParts = numberOfParts
        self.numberOfPoints = numberOfPoints
        self.partIndex = partIndex
        self.pointX = points[0]
        self.pointY = points[1]
        self.points = points

    def __repr__(self):
        return str(round(self.pointX, 4)) + ' ' + str(round(self.pointY,4))


def readSHP(filename):
    filename = 'tl_2019_49027_addrfeat.shp'
    shx = filename[:-3] + 'shx'
    index = readSHX(shx)
    # size = os.path.getsize(filename)
    # print(size)
    fileCode, z1, z2, z3, z4, z5, fileLength = np.fromfile(filename, np.dtype('>i4'), 7)
    headerPart1 = [fileCode, z1, z2, z3, z4, z5, fileLength]
    shapefileVersion, shapeType = np.fromfile(filename, np.dtype('<i4'), 2, offset=28)
    headerPart2 = [shapefileVersion, shapeType]
    minLat, minLong, maxLat, maxLong, zMin, zMax, mMin, mMax = np.fromfile(filename, np.dtype('<d'), 8, offset=36)
    headerPart3 = minLat, minLong, maxLat, maxLong, zMin, zMax, mMin, mMax
    shapes = []
    for i in index:
        shapeType = np.fromfile(filename, np.dtype('<i4'), 1, offset=2*i+8)
        boundingBox = np.fromfile(filename, np.dtype('<d'), 4, offset=2*i+12)
        numberOfParts = np.fromfile(filename, np.dtype('<i4'), 1, offset=2*i+44)
        numberOfPoints = np.fromfile(filename, np.dtype('<i4'), 1, offset=2*i+48)
        partIndex = np.fromfile(filename, np.dtype('<i4'), 1, offset=2*i+52)
        points = np.fromfile(filename, np.dtype('<d'), 2*numberOfPoints, offset=2*i+56)
        shapes.append(shape(shapeType,boundingBox,numberOfParts,numberOfPoints,partIndex,points))
    return headerPart1

def readSHX(filename):
    offset_contentLength = np.fromfile(filename, np.dtype('>i4'), offset=100)
    offset = offset_contentLength[::2]
    return offset

print(readSHX('tl_2019_49027_addrfeat.shx'))

def readDBF(filename):
    return

def writeSHP(filename):
    return

def writeSHX(filename):
    return

def writeDBF(filename):
    return

def readPoint():
    return

def readLine():
    return

def readPolygon():
    return


# filename = 'tl_2019_49027_addrfeat.shp'
# shx = filename[:-3] + 'shx'
# print(shx)
# # filename = 'tl_2019_49027_addrfeat.shx'
# fileCode, z1, z2, z3, z4, z5, fileLength = np.fromfile(filename, np.dtype('>i4'), 7)
# headerPart1 = [fileCode, z1, z2, z3, z4, z5, fileLength]
# shapefileVersion, shapeType = np.fromfile(filename, np.dtype('<i4'), 2, offset=28)
# headerPart2 = [shapefileVersion, shapeType]
# minLat, minLong, maxLat, maxLong, zMin, zMax, mMin, mMax = np.fromfile(filename, np.dtype('<d'), 8, offset=36)
# headerPart3 = minLat, minLong, maxLat, maxLong, zMin, zMax, mMin, mMax
# fileCode, z1, z2, z3, z4, z5, fileLength = np.fromfile(filename, np.dtype('>i4'), 7)
# headerPart1 = [fileCode, z1, z2, z3, z4, z5, fileLength]
# shapefileVersion, shapeType = np.fromfile(filename, np.dtype('<i4'), 2, offset=28)
# headerPart2 = [shapefileVersion, shapeType]
# minLat, minLong, maxLat, maxLong, zMin, zMax, mMin, mMax = np.fromfile(filename, np.dtype('<d'), 8, offset=36)
# headerPart3 = minLat, minLong, maxLat, maxLong, zMin, zMax, mMin, mMax
#
# recordNumber, contentLength = np.fromfile(filename, np.dtype('>i4'), 2, offset=100)
# recordHeader = [recordNumber, contentLength]

# recordHeader = np.fromfile(filename, np.dtype('>i4'), 8, offset=100)

# for i in recordNumber:





# # polylines
# shapeType2 = np.fromfile(filename, np.dtype('<i4'), 1, offset=108)
# boundingBox = np.fromfile(filename, np.dtype('<d'), 4, offset=112)
# numberOfParts = np.fromfile(filename, np.dtype('<i4'), 1, offset=144)
# numberOfPoints = np.fromfile(filename, np.dtype('<i4'), 1, offset=148)
# partIndex = np.fromfile(filename, np.dtype('<i4'), 1, offset=152)
# points = np.fromfile(filename, np.dtype('<d'), 2*numberOfPoints[0], offset=156)
#
# print('record header' , np.fromfile(filename, np.dtype('>i4'), 2, offset=100))
# print('record header' , np.fromfile(filename, np.dtype('>i4'), 2, offset=204))
# print('record header' , np.fromfile(filename, np.dtype('>i4'), 2, offset=628))
# print('record header' , np.fromfile(filename, np.dtype('>i4'), 2, offset=956))

# print('shape type', np.fromfile(filename, np.dtype('<i4'), 1, offset=212))
# print('bounding box' , np.fromfile(filename, np.dtype('<d'), 4, offset=216))
# print('numberOfParts', np.fromfile(filename, np.dtype('<i4'), 1, offset=248))
# print('numberOfPoints', np.fromfile(filename, np.dtype('<i4'), 1, offset=252))
# print('partIndex', np.fromfile(filename, np.dtype('<i4'), 1, offset=256))
# print('points', np.fromfile(filename, np.dtype('<d'), 2*23, offset=260))
# print('record header', np.fromfile(filename, np.dtype('>i4'), 2, offset=628))
# print('record header', np.fromfile(filename, np.dtype('>i4'), 2, offset=956))

# next record header at 8 + 2*record length

# print(headerPart1)
# print(headerPart2)
# print(headerPart3)
# print(recordHeader)
# print(shapeType2)
# # print(boundingBox)
# print(numberOfParts)
# print(numberOfPoints)
# print(partIndex)
# print(points)
#
#
# filename = 'tl_2019_49027_addrfeat.dbf'
# version = np.fromfile(filename, np.dtype('i1'),1)
# date = np.fromfile(filename, np.dtype('i1'),3, offset=1)
# date[0] -= 100
# numberOfRecords = np.fromfile(filename, np.dtype('i4'),1, offset=4)
# bytesInHeader = np.fromfile(filename, np.dtype('i2'),1, offset=8)
# bytesInRecord = np.fromfile(filename, np.dtype('i2'),1, offset=10)
# incompleteTransactionFlag = np.fromfile(filename, np.dtype('i1'),1, offset=14)
# encryptionFlag = np.fromfile(filename, np.dtype('i1'),1, offset=15)
# garbageproductionMdxFileFlag = np.fromfile(filename, np.dtype('i1'),1, offset=28)
# garbageproductionMdxFileFlag = chr(garbageproductionMdxFileFlag[0])
# languageDriverID = np.fromfile(filename, np.dtype('i1'),1, offset=29)
# temp = []
# for item in languageDriverID:
#     temp.append(chr(item))
# languageDriverID = temp
# fieldName = np.fromfile(filename, np.dtype('i1'),2, offset=32)
# temp = []
# for i in fieldName:
#     temp.append(chr(i))
# fieldName = temp
# fieldType = np.fromfile(filename, np.dtype('i1'),1, offset=43)
# temp = []
# for item in fieldType:
#     temp.append(chr(item))
# fieldType = temp
# fieldLength = np.fromfile(filename, np.dtype('i1'),1, offset=48)
# fieldCount = np.fromfile(filename, np.dtype('i1'),1, offset=49)
# workAreaID = np.fromfile(filename, np.dtype('i2'),1, offset=50)
# example = np.fromfile(filename, np.dtype('i1'),10, offset=52)
# mdxFlag2 = np.fromfile(filename, np.dtype('i1'),1, offset=63)
#
#
# # #database descriptor field
# # def desFieldRead(filename):
#
#
#
#
# print(version)
# print(date)
# print(numberOfRecords)
# print(bytesInHeader)
# print(bytesInRecord)
# print(incompleteTransactionFlag)
# print(encryptionFlag)
# print(garbageproductionMdxFileFlag)
# print(languageDriverID)
# print(fieldName)
# print(fieldType)
# print(fieldLength)
# print(fieldCount)
# print(workAreaID)
# print(example)
# print(mdxFlag2)

reddit = shapefile('tl_2019_49027_addrfeat.shp')
for i in range(len(reddit.shapes)):
    print(i,  ': ' , reddit.shapes[i].points)
print(reddit.shapes[0].points)

