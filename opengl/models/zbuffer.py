
Z_MIN = -1000


def color(r, g, b):
    return bytes([round(b), round(g), round(r)])

class ZBuffer(object):
    def __init__(self, x, y):
        self.pixels = [[float('-inf') for i in range(x)] for j in range(y)]
        self.width = x
        self.height = y
        self.max = 0
        self.min = 0

    def add_z(self, x, y, z):
        if self.min > z:
            self.min = z
        if self.max < z:
            self.max = z

        self.pixels[y][x] = z

    def normalize(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.pixels[y][x] <= self.min:
                    self.pixels[y][x] = color(0, 0, 0)
                else:
                    if (self.max == self.min):
                        col = 255
                    else:
                        col = (self.pixels[y][x] - self.min) / (self.max - self.min) * 255
                    self.pixels[y][x] = color(col, col, col)


         