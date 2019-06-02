
import random
import math

def gen_color(r, g, b):
    return bytes([round(b), round(g), round(r)])


def dot(v0, v1):
    return v0.x * v1.x + v0.y * v1.y + v0.z * v1.z


def gouraud(normals, barycentric, color, light, x, y, z):
    u, v, w = barycentric
    n_a, n_b, n_c = normals
    intensity_a = dot(n_a, light)
    intensity_b = dot(n_b, light)
    intensity_c = dot(n_c, light)

    intensity = u * intensity_a + v * intensity_b + w * intensity_c
    r = min(max(color[0] * intensity, 0), 255)
    g = min(max(color[1] * intensity, 0), 255)
    b = min(max(color[2] * intensity, 0), 255)

    return gen_color(r, g, b)


def planet_shader(normals, barycentric, color, light, x, y, z):
    color = (255, 215, 0)

    light_gold = (99, 91, 54)
    brown_gold = (67, 40, 13)
    dark_gold = (42, 20, 9)
    light *= 2

    rand = random.random() * 0.15 + math.cos(y * 12) * 0.85

    if rand < 0.8:
        color = light_gold
    elif rand < 0.9:
        color = brown_gold
    else:
        color = dark_gold

    u, v, w = barycentric
    n_a, n_b, n_c = normals

    intensity_a = dot(n_a, light)
    intensity_b = dot(n_b, light)
    intensity_c = dot(n_c, light)

    intensity = u * intensity_a + v * intensity_b + w * intensity_c
    r = min(max(color[0] * intensity, 0), 255)
    g = min(max(color[1] * intensity, 0), 255)
    b = min(max(color[2] * intensity, 0), 255)

    return gen_color(r, g, b)

def batman_shader(normals, barycentric, color, light, x, y, z):
    light_gray = (50, 50, 50)
    black_gray = (20, 20, 20)
    white = (255, 255, 255)
    light *= 2

    rand = random.random() * 0.15 + math.cos(y * 1) * 0.85

    if z < -2355:
        color = (138, 7, 7)
    elif z < -2330:
        color = black_gray
    else:
        color = light_gray
    # elif rand < 0.95:
    #     color = black
    # else:
    #     color = white

    u, v, w = barycentric
    n_a, n_b, n_c = normals

    intensity_a = dot(n_a, light)
    intensity_b = dot(n_b, light)
    intensity_c = dot(n_c, light)

    intensity = u * intensity_a + v * intensity_b + w * intensity_c
    r = min(max(color[0] * intensity, 0), 255)
    g = min(max(color[1] * intensity, 0), 255)
    b = min(max(color[2] * intensity, 0), 255)

    return gen_color(r, g, b)

def batarang_shader(normals, barycentric, color, light, x, y, z):

    white = (255, 255, 255)
    metallic = (188, 198, 204)

    if y % 70 < 2:
        color = metallic
    else:
        color = white

    u, v, w = barycentric
    n_a, n_b, n_c = normals

    intensity_a = dot(n_a, light)
    intensity_b = dot(n_b, light)
    intensity_c = dot(n_c, light)

    intensity = u * intensity_a + v * intensity_b + w * intensity_c
    r = min(max(color[0] * intensity, 0), 255)
    g = min(max(color[1] * intensity, 0), 255)
    b = min(max(color[2] * intensity, 0), 255)

    return gen_color(r, g, b)

def batmobile_shader(normals, barycentric, color, light, x, y, z):

    if color[0] < 50:
        color = [x - 10 if x > 10 else 0 for x in color]

    u, v, w = barycentric
    n_a, n_b, n_c = normals

    intensity_a = dot(n_a, light)
    intensity_b = dot(n_b, light)
    intensity_c = dot(n_c, light)

    intensity = u * intensity_a + v * intensity_b + w * intensity_c
    r = min(max(color[0] * intensity, 0), 255)
    g = min(max(color[1] * intensity, 0), 255)
    b = min(max(color[2] * intensity, 0), 255)

    return gen_color(*color)

def cell_shader(normals, barycentric, color, light):
    pass
    # color = gen_color(
    #     r if r < 255 and r > -1 else 0,
    #     g if g < 255 and g > -1 else 0,
    #     b if b < 255 and b  > -1 else 0
    # )
    # return gen_color(
    #     r if r > 255  else 0,
    #     g if g > 255 else 0,
    #     b if b > 255 else 0
    # )
    # return color



