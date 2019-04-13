from opengl.main import OpenGl

# [(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)]


def fill_polygon():
    test = OpenGl()

    test.glInit()
    test.glCreateWindow(400, 500)
    test.glViewPort(0, 0, 400, 500)
    test.glColor(1, 1, 1)
    test.glFillPolygon([(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383)])
    test.glFinish()