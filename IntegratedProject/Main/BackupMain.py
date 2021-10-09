import matplotlib.pyplot as plot
import time as t
# Get an area
from IntegratedProject.Map.Area import swath, getAltitude
from IntegratedProject.Map.Transmitter import Transmitter
from IntegratedProject.Map.findInArray import getIndex
from IntegratedProject.Map.roundRobyn import midPointCircleDraw, fillPoints, moveFullCircle, fillPointsZero
from IntegratedProject.RadarEquations import PowerAndRange

time = 0
pt0 = t.perf_counter()

sweet = swath([], ['Map\MapData\\N38W112.hgt','Map/MapData\\N38W114.hgt','Map/MapData\\N38W113.hgt','Map/MapData\\N38W115.hgt','Map/MapData\\N39W114.hgt','Map/MapData\\N39W113.hgt', \
                   'Map/MapData\\N39W112.hgt','Map/MapData\\N39W115.hgt','Map/MapData\\N40W112.hgt','Map/MapData\\N40W113.hgt','Map/MapData\\N40W115.hgt','Map/MapData\\N40W114.hgt'], setNullsTo = 1200)

pt1 = t.perf_counter()
time += pt1-pt0
pt0 = pt1
print(time)

print(getAltitude(sweet, 39.03,-113.5))

# Add transmitters to the area, check to see they're within the area
texas = Transmitter(39,-113, 100, 2500)
range = PowerAndRange.range(texas, 1)*1000*5
print(range)

pt1 = t.perf_counter()
time += pt1-pt0
pt0 = pt1
print(time)

# Run Line of sight, documenting the power imparted to each point
x, y = getIndex(sweet, texas)
texIndex = (x, y)
# xy = midPointCircleDraw(x, y, int(range/30.87))
xy = midPointCircleDraw(0, 0, int(range/30.87))

# xy.sort()
# print("xy sorted")
# pt1 = t.perf_counter()
# time += pt1-pt0
# pt0 = pt1
# print(time)

print(len(xy))

# print(len(xy))
xy = list(set(xy))
print("xy listed")
pt1 = t.perf_counter()
time += pt1-pt0
pt0 = pt1
print(time)

print(len(xy))

# drawFull(xy)
xy = fillPointsZero(xy)
print("xy filled")
pt1 = t.perf_counter()
time += pt1-pt0
pt0 = pt1
print(time)

print(len(xy))



# print(len(xy))
xy = list(set(xy))
print("xy listed")
pt1 = t.perf_counter()
time += pt1-pt0
pt0 = pt1
print(time)

print(len(xy))

# print(len(xy))
xy.sort()
print("xy sorted 2")
pt1 = t.perf_counter()
time += pt1-pt0
pt0 = pt1
print(time)

# xy = moveFullCircle(xy, x, y)

print("starting xyz")
pt1 = t.perf_counter()
time += pt1-pt0
pt0 = pt1
print(time)


xyz = list()
for h in xy:
    # print(i)
    i = h[0]
    j = h[1]
    z = i*i+j*j
    xyz.append((i,j,z))

# xy = moveFullCircle(xy, x, y)
xyz = moveFullCircle(xyz, x, y)

print("ending xyz")
pt1 = t.perf_counter()
time += pt1-pt0
pt0 = pt1
print(time)


# print(xy)
# x, y = zip(*xy)
# plot.scatter(x, y, alpha=0.8)

print("zipping xyz")
pt1 = t.perf_counter()
time += pt1-pt0
pt0 = pt1
print(time)

x, y, z = zip(*xyz)
plot.scatter(x, y, 1, z, alpha=0.05)

print("ziped xyz")
pt1 = t.perf_counter()
time += pt1-pt0
pt0 = pt1
print(time)



# Paint the location
plot.imshow(sweet.de)
# Paint the power

# Show
plot.show()