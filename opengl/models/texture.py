
import struct
from opengl.models.byte_struct import *
from opengl.models.vectors import V3

def color(r, g, b):
    return bytes([round(b), round(g), round(r)])

class Texture(object):
    def __init__(self, filename):
        if filename.find('.bmp', len(filename) - 4) == -1:
            filename = filename + '.bmp'
        self.filename = filename
        f = open(self.filename, 'rb')

        f.seek(10)
        header_size = struct.unpack('=l', f.read(4))[0]

        f.seek(18)
        self.width = struct.unpack('=l', f.read(4))[0]
        self.height = struct.unpack('=l', f.read(4))[0]

        f.seek(header_size)
        self.colors = []
        for y in range(self.height):
            vec = []
            for x in range(self.width):
                b = ord(f.read(1))
                g = ord(f.read(1))
                r = ord(f.read(1))
                vec.append(color(r, g, b))

            self.colors.append(vec)
        f.close()

    def __in_range(self, x, y):
        return y < len(self.colors) and x < len(self.colors[0])

    def __line(self, point0, point1):

        x0, y0, z0 = point0
        x1, y1, z1 = point1

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)
        steep = dy > dx

        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1
        
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        offset = 0
        threshold = dx
        y = y0

        for x in range(round(x0), round(x1) + 1):
            if (x < self.width and y < self.height) or (steep and x < self.height and y < self.width):
                if steep and self.__in_range(y, x):
                    self.colors[round(x)][round(y)] = color(255, 255, 255)
                elif self.__in_range(x, y):
                    self.colors[round(y)][round(x)] = color(255, 255, 255)
            
            offset += dy * 2
            if offset >= threshold:
                y += 1 if y0 < y1 else -1
                threshold += dx * 2

        return

    def outline_polygon(self, polygon_vertices):
        
        for i in range(len(polygon_vertices)):
            v0 = polygon_vertices[i - 1] 
            v1 = polygon_vertices[i]
            print(v1 * V3(self.width, self.height, 0))
            self.__line(v0, v1)




    def write_out(self):
        name = self.filename[:self.find('.bmp')] + '-outline.bmp'
        self.width = len(self.colors[0])
        self.height = len(self.colors)

        f = open(self.filename, 'wb')

        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        for y in range(self.height):
            for x in range(self.width):
                f.write(self.colors[y][x])

        f.close()