class transmitter:
    """a class that represents transpitters"""
    def __init__(self, lat, long, height = 1, freq = 0.03, ally = False):
        self.height = height
        self.freq = freq
        self.lat = lat
        self.long = long
        self.ally = ally
        self.power = 0
        self.range = 0
        self.polarization = 'horizontal'