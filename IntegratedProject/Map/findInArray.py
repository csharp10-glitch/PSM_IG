from IntegratedProject.Math.SphericalGeometry import DMStoS, decimalDegreeToDMS

def getLatLong(area, index):
    minLat = area.minLat
    minLong = area.minLong
    lat = index[0]
    long = index[1]
    lat = minLat+lat/3600
    long = minLong+long/3600
    return lat, long

def getIndex(terrain, lat: float, long: float):
    minlat, minlong = terrain.minLat, terrain.minLong
    maxlat, maxlong = terrain.maxLat, terrain.maxLong
    # if((m.fabs(lat) < m.fabs(minlat) | (m.fabs(lat) > m.fabs(maxlat)) | (m.fabs(long) > m.fabs(maxlong)) | (m.fabs(long) < m.fabs(minlong))):
    #     print("Oops!  That was no valid number.  Try again...")
    lat = lat - minlat
    long = long - minlong
    lat = int(DMStoS(decimalDegreeToDMS(lat)))
    long = int(DMStoS(decimalDegreeToDMS(long)))
    return lat, long

def getIndex(terrain, geoobject):
    lat = geoobject.lat
    long = geoobject.long
    minlat, minlong = terrain.minLat, terrain.minLong
    maxlat, maxlong = terrain.maxLat, terrain.maxLong
    # if((m.fabs(lat) < m.fabs(minlat) | (m.fabs(lat) > m.fabs(maxlat)) | (m.fabs(long) > m.fabs(maxlong)) | (m.fabs(long) < m.fabs(minlong))):
    #     print("Oops!  That was no valid number.  Try again...")
    lat = lat - minlat
    long = long - minlong
    lat = int(DMStoS(decimalDegreeToDMS(lat)))
    long = int(DMStoS(decimalDegreeToDMS(long)))
    return lat, long