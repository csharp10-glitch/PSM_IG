
class GeoObject:
    def __init__(self, lat, long, altitude):
        self.lat = lat
        self.long = long
        self.altitude = altitude

class GeoPoint(GeoObject):
    def __init__(self, lat, long, altitude):
        self.lat = lat
        self.long = long
        self.altitude = altitude

class Terrain(GeoObject):
    def __int__(self, hgt):
        self.maxLat = hgt.maxLat
        self.minLat = hgt.minLat
        self.lat = self.minLat
        self.minLong = hgt.minLong
        self.maxLong = hgt.maxLong
        self.long = self.minLong
        self.de = hgt.de
        self.dim = hgt.shape
        self.type = "inland"
        self.shape = hgt.shape
        # self.granularity = hgt.granularity
        self.granularity = 30
