
import math
import struct
from collections import namedtuple




V2 = namedtuple('Point2', ['x', 'y'])
# V3 = namedtuple('Point3', ['x', 'y', 'z'])

from opengl.models.obj import Obj
from opengl.models.zbuffer import ZBuffer
from opengl.models.vectors import V3
from opengl.models.texture import Texture
from opengl.models.byte_struct import *

def color(r, g, b):
    return bytes([round(b), round(g), round(r)])

def sub(v0, v1):
    return V3(v0.x - v1.x, v0.y - v1.y, v0.z - v1.z)

def dot(v0, v1):
    return v0.x * v1.x + v0.y * v1.y + v0.z * v1.z

def cross(v0, v1):

    return V3(
        v0.y * v1.z - v0.z * v1.y,
        v0.z * v1.x - v0.x * v1.z,
        v0.x * v1.y - v0.y * v1.x
    )

def vect_normalize(v):
    v_len = (v.x**2 + v.y**2 + v.z**2) ** 0.5
    return V3(v.x/v_len, v.y/v_len, v.z/v_len)

def barycentric(v_a, v_b, v_c, point):

    bar = cross(
        V3(v_c.x - v_a.x, v_b.x - v_a.x, v_a.x - point.x),
        V3(v_c.y - v_a.y, v_b.y - v_a.y, v_a.y - point.y)
    )


    if abs(bar[2]) < 1:
        return -1, -1, -1

    return (
        1 - (bar[0] + bar[1]) / bar[2],
        bar[1] / bar[2],
        bar[0] / bar[2]
    )

def bonding_box(*vertices):
    return V2(
            round(min(v.x for v in vertices)),
            round(min(v.y for v in vertices))
        ), V2(
            round(max(v.x for v in vertices)), 
            round(max(v.y for v in vertices))
        )

class OpenGl:

    def __init__(self, name='image', flag_zbuffer=False, texture_file=None):
        self.name = name
        self.win_width = 0
        self.win_height = 0
        self.color = color(0, 0, 0)
        self.pixels = []
        self.light = V3(0, 0, 1)
        self.flag_zbuffer = flag_zbuffer
        self.texture = None
        if texture_file:
            self.texture = Texture(texture_file)

    def glInit(self, name='image', flag_zbuffer=False, texture_file=None):
        self.__init__(name, flag_zbuffer, texture_file)


    def glCreateWindow(self, width, height):
        self.win_width = width
        self.win_height = height
        self.pixels = [[self.color for x in range(self.win_width)] for y in range(self.win_height)]
        self.zbuffer = ZBuffer(width, height)

    def glViewPort(self, x, y, width, height):
        self.view_x = x
        self.view_y = y
        self.view_width= width
        self.view_height = height

    def denormalize_x(self, x):
        return math.trunc((x + 1) * self.view_width / 2 + self.view_x)

    def denormalize_y(self, y):
        return math.trunc((y + 1) * self.view_height / 2 + self.view_y)

    def glClear(self):
        self.pixels = [color(0, 0, 0) for y in self.win_height for x in self.win_width]

    def glClearColor(self, r, g, b):
        self.pixels = [color(r, g, b) for y in self.win_height for x in self.win_width]

    def glVertex(self, x, y):
        self.pixels[1][21] = self.color
        if (x <= 1 and x >= -1 and y <= 1 and y >= -1):
            self.__vertex(self.denormalize_y(y) -1, self.denormalize_x(x) - 1)
            # self.pixels[self.denormalize_y(y) - 1][self.denormalize_x(x) - 1] = self.color

    def __in_range(self, x, y):
        return y < len(self.pixels) and x < len(self.pixels[0])

    def __vertex(self, x, y, color=None):
        color = color if color != None else self.color
        if self.__in_range(x, y):
            self.pixels[y][x] = color

    def glColor(self, r, g, b):
        self.color = color(math.trunc(r * 255), math.trunc(g * 255), math.trunc(b * 255))

    def glLine(self, x0, y0, x1, y1):
        x0 = self.denormalize_x(x0)
        x1 = self.denormalize_x(x1)

        y0 = self.denormalize_y(y0)
        y1 = self.denormalize_y(y1)

        self.__line((x0, y0), (x1, y1))

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

        for x in range(round(x0), round(x1) + 1):
            if (x < self.win_width and y < self.win_height) or (steep and x < self.win_height and y < self.win_width):
                if steep and self.__in_range(y, x):
                    self.pixels[round(x)][round(y)] = self.color
                elif self.__in_range(x, y):
                    self.pixels[round(y)][round(x)] = self.color
            
            offset += dy * 2
            if offset >= threshold:
                y += 1 if y0 < y1 else -1
                threshold += dx * 2

        return


    def glFillPolygon(self, polygon_vertices):

        x_max = max(polygon_vertices, key=lambda a: a[0])[0]
        x_min = min(polygon_vertices, key=lambda a: a[0])[0]
        
        y_max = max(polygon_vertices, key=lambda a: a[1])[1]
        y_min = min(polygon_vertices, key=lambda a: a[1])[1]

        for i in range(len(polygon_vertices)):
            v0 = polygon_vertices[i - 1]
            v1 = polygon_vertices[i]
            self.__line((v0[0], v0[1]), (v1[0], v1[1]))

        for y in range(y_min, y_max + 1):
            intercepts = []
            for i in range(len(polygon_vertices)):
                v0 = polygon_vertices[i - 1]
                v1 = polygon_vertices[i]

                if (y <= v0[1] and y >= v1[1]) or (y <= v1[1] and y >= v0[1]):
                    x = ((v0[0] - v1[0])/(v0[1] - v1[1])) * (y - v0[1]) + v0[0] 
                    
                    if x >= x_min and x <= x_max:
                        intercepts.append(x)

            for x in range(x_min, x_max + 1):
                if self.__is_inside(intercepts, x):
                    self.__vertex(x, y)


    def glFillTriangle(self, v_a, v_b, v_c, color=None, texture_vertices=None):
        bb_min, bb_max = bonding_box(v_a, v_b, v_c)

        for y in range(bb_min.y, bb_max.y + 1):
            for x in range(bb_min.x, bb_max.x + 1):
                u, v, w = barycentric(v_a, v_b, v_c, V2(x, y))
                if u < 0 or v < 0 or w < 0:
                    continue

                z = round(v_a.z * u + v_b.z * v + v_c.z * w)
                
                if z > self.zbuffer.pixels[y][x]:
                    if texture_vertices:
                        tv_a, tv_b, tv_c = texture_vertices
                        tx = round((tv_a.x * u + tv_b.x * v + tv_c.x * w) * self.texture.width) - 1
                        ty = round((tv_a.y * u + tv_b.y * v + tv_c.y * w) * self.texture.height) - 1
                        color = self.texture.colors[ty][tx]
                        self.texture.outline_polygon(texture_vertices)

                    self.__vertex(x, y, color)
                    self.zbuffer.add_z(x, y, z)


    def __transform(self, v, translate, scale):
        return V3(
            (v[0] + translate[0]) * scale[0],
            (v[1] + translate[1]) * scale[1],
            (v[2] + translate[2]) * scale[2],
        )


    def glOpenModel(self, filename, translate=(0, 0, 0), scale=(1, 1, 1)):

        model = Obj(filename)
        print('hola')

        for face in model.faces:
            num_v = len(face)
            vertices = []

            if num_v == 3:
                v_a = model.vertices[face[0][0] - 1]
                v_b = model.vertices[face[1][0] - 1]
                v_c = model.vertices[face[2][0] - 1]

                v_a = self.__transform(v_a, translate, scale)
                v_b = self.__transform(v_b, translate, scale)
                v_c = self.__transform(v_c, translate, scale)

                face_norm = vect_normalize((v_b - v_a) * (v_c - v_a))

                intensity = dot(self.light, face_norm)

                if self.texture:
                    tv_a = V3(*model.texture_vertices[face[0][1] - 1])
                    tv_b = V3(*model.texture_vertices[face[1][1] - 1])
                    tv_c = V3(*model.texture_vertices[face[2][1] - 1])
                    # print('safo')
                    self.glFillTriangle(v_a, v_b, v_c, texture_vertices=(tv_a, tv_b, tv_c))
                else:
                    if intensity >= 0 and intensity <= 1:
                        self.glFillTriangle(v_a, v_b, v_c, color(255 * intensity, 255 * intensity, 255 * intensity))
            else:
                print('hola')

            # for j in range(num_v):
            #     f1 = face[j][0]
            #     f2 = face[(j + 1)%num_v][0]

            #     v1 = model.vertices[f1 - 1]
            #     v2 = model.vertices[f2 - 1]

            #     scaleX, scaleY = scale
            #     translateX, translateY = translate

            #     x0 = (v1[0] + translateX) * scaleX
            #     y0 = (v1[1] + translateY) * scaleY
            #     x1 = (v2[0] + translateX) * scaleX
            #     y1 = (v2[1] + translateY) * scaleY
            #     print(x0, y0, x1, y1)
            #     self.__line((x0, y0), (x1, y1))




    def __is_inside(self, intercepts, x):
        return len(list(filter(lambda i: i > x, intercepts))) & 1 and len(list(filter(lambda i: i < x, intercepts))) & 1

            


    def glFinish(self):
        f = open(self.name + '.bmp', 'bw')
        z = open(self.name + '-zbuffer.bmp', 'bw')

        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.win_width * self.win_height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        f.write(dword(40))
        f.write(dword(self.win_width))
        f.write(dword(self.win_height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.win_width * self.win_height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        z.write(char('B'))
        z.write(char('M'))
        z.write(dword(14 + 40 + self.win_width * self.win_height * 3))
        z.write(dword(0))
        z.write(dword(14 + 40))

        z.write(dword(40))
        z.write(dword(self.win_width))
        z.write(dword(self.win_height))
        z.write(word(1))
        z.write(word(24))
        z.write(dword(0))
        z.write(dword(self.win_width * self.win_height * 3))
        z.write(dword(0))
        z.write(dword(0))
        z.write(dword(0))
        z.write(dword(0))

        if self.flag_zbuffer:
            self.zbuffer.normalize()
        for y in range(self.win_height):
            for x in range(self.win_width):
                f.write(self.pixels[y][x])
                if self.flag_zbuffer:
                    z.write(self.zbuffer.pixels[y][x])

        f.close()
        z.close()