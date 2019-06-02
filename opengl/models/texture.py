
import struct
from opengl.models.byte_struct import *
from opengl.models.vectors import V3

def color(r, g, b):
    return bytes([round(b), round(g), round(r)])

class Texture(object):
    def __init__(self, filename, flag_texture=False):
        if filename.find('.bmp', len(filename) - 4) == -1:
            filename = filename + '.bmp'
        self.filename = filename
        self.flag_texture = flag_texture
        f = open(self.filename, 'rb')

        f.seek(10)
        header_size = struct.unpack('=l', f.read(4))[0]

        f.seek(18)
        self.width = struct.unpack('=l', f.read(4))[0]
        self.height = struct.unpack('=l', f.read(4))[0]

        f.seek(header_size)
        self.colors = []
        self.colors_outline = []
        for y in range(self.height):
            vec = []
            if self.flag_texture:
                vec2 = []
            for x in range(self.width):
                b = ord(f.read(1))
                g = ord(f.read(1))
                r = ord(f.read(1))
                vec.append([r, g, b])
                if self.flag_texture:
                    vec2.append([r, b, g])

            self.colors.append(vec)
            if (self.flag_texture):
                self.colors_outline.append(vec2)
        f.close()

    def in_range(self, x, y):
        return y < len(self.colors) and x < len(self.colors[0])

    def __line(self, point0, point1):

        x0, y0 = point0
        x1, y1 = point1

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
        # print(point1, point0)
        for x in range(round(x0), round(x1) + 1):
            if (x < self.width and y < self.height) or (steep and x < self.height and y < self.width):
                if steep and self.in_range(y, x):
                    # print(x, y)
                    self.colors_outline[round(x)][round(y)] = [255, 255, 255]
                elif self.in_range(x, y):
                    self.colors_outline[round(y)][round(x)] = [255, 255, 255]
            
            offset += dy * 2
            if offset >= threshold:
                y += 1 if y0 < y1 else -1
                threshold += dx * 2

        return

    def outline_polygon(self, polygon_vertices):
        
        for i in range(len(polygon_vertices)):
            v0 = polygon_vertices[i - 1] 
            v1 = polygon_vertices[i]
            v0 = (v0.x * self.width, v0.y * self.height)
            v1 = (v1.x * self.width, v1.y * self.height)
            self.__line(v0, v1)




    def write_out(self):
        name = self.filename[:self.filename.find('.bmp')] + '-outline.bmp'
        print(name)
        self.width = len(self.colors[0])
        self.height = len(self.colors)

        f = open(name, 'wb')

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
                f.write(color(*self.colors_outline[y][x]))

        f.close()