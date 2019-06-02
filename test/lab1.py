from opengl.main import OpenGl

# [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]


def fill_polygon():
    test = OpenGl()

    test.glInit(output_dir='out/lab1', name='poly1',)
    test.glCreateWindow(500, 500)
    test.glViewPort(0, 0, 500, 500)
    test.glColor(1, 1, 1)
    test.glFillPolygon([(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)])
    test.glFinish()

    test.glInit(output_dir='out/lab1', name='poly2',)
    test.glCreateWindow(500, 500)
    test.glViewPort(0, 0, 500, 500)
    test.glColor(1, 1, 1)
    test.glFillPolygon([(321, 335), (288, 286), (339, 251), (374, 302)])
    test.glFinish()

    test.glInit(output_dir='out/lab1', name='poly3',)
    test.glCreateWindow(500, 500)
    test.glViewPort(0, 0, 500, 500)
    test.glColor(1, 1, 1)
    test.glFillPolygon([(377, 249), (411, 197), (436, 249)])
    test.glFinish()

    test.glInit(output_dir='out/lab1', name='poly4',)
    test.glCreateWindow(800, 300)
    test.glViewPort(0, 0, 800, 300)
    test.glColor(1, 1, 1)
    test.glFillPolygon([(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52), (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230), (597, 215), (552, 214), (517, 144), (466, 180)])
    test.glFinish()

    test.glInit(output_dir='out/lab1', name='poly5',)
    test.glCreateWindow(800, 400)
    test.glViewPort(0, 0, 800, 400)
    test.glColor(1, 1, 1)
    test.glFillPolygon([(682, 175), (708, 120), (735, 148), (739, 170)])
    test.glFinish()