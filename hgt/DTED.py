import hgt
import area
import numpy
import math
import os
import matplotlib.pyplot as plot

DTED0 = {0:30,50:60,70:90,75:120,80:180}
DTED1 = {0:3,50:6,70:9,75:12,80:18}
DTED2 = {0:1,50:2,70:3,75:4,80:6}

# N39W113 = hgt.readHGT()
# N39W113 = area.area('N39W113.hgt')
# plot.imshow(N39W113.de)
# plot.show()

# data = numpy.fromfile(fn, numpy.dtype('>i1'), 20)
# header = []
# for i in data:
#     header.append(chr(i))
# print(header)
#
# data = numpy.fromfile(fn, numpy.dtype('>i1'),8,offset=20)
# ssss = []
# for i in data:
#     ssss.append(chr(i))
# print(ssss)
#
# data = numpy.fromfile(fn, numpy.dtype('>i1'),4,offset=28)
# VMA = [] # vertical measure of accuracy
# for i in data:
#     VMA.append(chr(i))
# print(VMA)
#
# data = numpy.fromfile(fn, numpy.dtype('>i1'),3,offset=32)
# USC = [] # vertical measure of accuracy
# for i in data:
#     USC.append(chr(i))
# print(USC)
#
# data = numpy.fromfile(fn, numpy.dtype('>i1'),12,offset=35)
# URC = [] # vertical measure of accuracy
# for i in data:
#     URC.append(chr(i))
# print(URC)
#
# data = numpy.fromfile(fn, numpy.dtype('>i1'),4,offset=47)
# NumLongLines = [] # vertical measure of accuracy
# for i in data:
#     NumLongLines.append(chr(i))
# print(NumLongLines)
#
# data = numpy.fromfile(fn, numpy.dtype('>i1'),4,offset=51)
# NumLatPoints = [] # vertical measure of accuracy
# for i in data:
#     NumLatPoints.append(chr(i))
# print(NumLatPoints)
#
# data = numpy.fromfile(fn, numpy.dtype('>i1'),1,offset=55)
# MultiAccuracy = [] # vertical measure of accuracy
# for i in data:
#     MultiAccuracy.append(chr(i))
# print(MultiAccuracy)
#
# data = numpy.fromfile(fn, numpy.dtype('>i1'),4,offset=80)
# DSIU = [] # vertical measure of accuracy
# for i in data:
#     DSIU.append(chr(i))
# print(DSIU)
#
# data = numpy.fromfile(fn, numpy.dtype('>i1'),5,offset=139)
# SeriesDesignator = [] # vertical measure of accuracy
# for i in data:
#     SeriesDesignator.append(chr(i))
# print(SeriesDesignator)
#
# data = numpy.fromfile(fn, numpy.dtype('>i1'),15,offset=144)
# UniqueReferenceNumber = [] # vertical measure of accuracy
# for i in data:
#     UniqueReferenceNumber.append(chr(i))
# print(UniqueReferenceNumber)
#
# data = numpy.fromfile(fn, numpy.dtype('>i1'),2,offset=167)
# DataEdition = [] # vertical measure of accuracy
# for i in data:
#     DataEdition.append(chr(i))
# print(DataEdition)
#
# data = numpy.fromfile(fn, numpy.dtype('>i1'),1,offset=169)
# mergeVersion = [] # vertical measure of accuracy
# for i in data:
#     mergeVersion.append(chr(i))
# print(mergeVersion)
#
# data = numpy.fromfile(fn, numpy.dtype('>i1'),4,offset=170)
# maintenanceDate = [] # vertical measure of accuracy
# for i in data:
#     maintenanceDate.append(chr(i))
# print(maintenanceDate)
#
# data = numpy.fromfile(fn, numpy.dtype('>i1'),4,offset=174)
# mergeDate = [] # vertical measure of accuracy
# for i in data:
#     mergeDate.append(chr(i))
# print(mergeDate)
#
# data = numpy.fromfile(fn, numpy.dtype('>i1'),4,offset=178)
# maintenanceDescriptorCode = [] # vertical measure of accuracy
# for i in data:
#     maintenanceDescriptorCode.append(chr(i))
# print(maintenanceDescriptorCode)
#
# data = numpy.fromfile(fn, numpy.dtype('>i1'),8,offset=182)
# producerCode = [] # vertical measure of accuracy
# for i in data:
#     producerCode.append(chr(i))
# print(producerCode)

# data = numpy.fromfile(fn, numpy.dtype('>i1'),50,offset=190)
# productSpec = [] # vertical measure of accuracy
# for i in data:
#     productSpec.append(chr(i))
# print(productSpec)


# YYMM
# data = numpy.fromfile(fn, numpy.dtype('>i1'),4,offset=218)
# productSpecDate = [] # vertical measure of accuracy
# for i in data:
#     productSpecDate.append(chr(i))
# print(productSpecDate)
#
# data = numpy.fromfile(fn, numpy.dtype('>i1'),3,offset=222)
# verticalDatum = [] # vertical measure of accuracy
# for i in data:
#     verticalDatum.append(chr(i))
# print(verticalDatum)
#
# data = numpy.fromfile(fn, numpy.dtype('>i1'),300,offset=222)
# verticalDatum = [] # vertical measure of accuracy
# for i in data:
#     verticalDatum.append(chr(i))
# print(verticalDatum)

# in_file = open(fn, "rb") # opening for [r]eading as [b]inary
# data = in_file.read(3428) # if you only wanted to read 512 bytes, do .read(512)
# in_file.close()
#
# data = data.decode("utf-8")
#
# out_file = open("header.txt", "w") # open for [w]riting as [b]inary
# out_file.write(data)
# out_file.close()
# data = []
# for i in range(100):
#     dat1 = numpy.fromfile(fn, numpy.dtype('i1'),1,offset=3429+i*14)
#     dat2 = numpy.fromfile(fn, numpy.dtype('B'),3,offset=3430+i*14)
#     dat3 = numpy.fromfile(fn, numpy.dtype('i2'),3,offset=3433+i*14)
#     dat4 = numpy.fromfile(fn, numpy.dtype('i4'),1,offset=3437+i*14)
#     data.append([dat1,dat2,dat3,dat4])
# # data.append(numpy.fromfile(fn, numpy.dtype('i1'),3,offset=3429))
# # data.append(numpy.fromfile(fn, numpy.dtype('i1'),2,offset=3432))
#
# for i in data:
#     print(i)
# print(len(data))

fn = 'n39_w113_1arc_v3.dt2'
# data = numpy.fromfile(fn, numpy.dtype('i2'), 8, offset=3428)
# print(data)

elev = []
for i in range(10):
    data = numpy.fromfile(fn, numpy.dtype('i2'), 3601, offset=3428+i*3607)
    ind = 0
    for i in data:
        ind += 1
        if i == 170:
            print(ind)
    elev.append(data)
    print(data)
# print(elev)
#
# plot.imshow(elev,vmin=0)
# plot.show()

# fn = 'N39W113.hgt'
# siz = os.path.getsize(fn)
# dim = int(math.sqrt(siz / 2))
# assert dim * dim * 2 == siz, 'Invalid file size'
# data = numpy.fromfile(fn, numpy.dtype('>i2'), dim * dim).reshape((dim, dim))
# plot.imshow(data,vmin=-100)
# plot.show()
#
#
# print(data)

