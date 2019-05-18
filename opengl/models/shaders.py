
def color(r, g, b):
    return bytes([round(b), round(g), round(r)])

def gourad(vertices, barycentric, color, intensity):
    u, v, w = barycentric
    v_a, v_b, v_c = vertices

    intensity_a = dot(v_a, intensity)
    intensity_b = dot(v_b, intensity)
    intensity_c = dot(v_c, intensity)

    intensity = u * intensity_a + v * intensity_b + w * intensity_c




