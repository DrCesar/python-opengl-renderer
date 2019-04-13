from opengl.main import OpenGl

def gen_zbuffer():
    test = OpenGl()

    test.glInit(flag_zbuffer=True)
    test.glCreateWindow(300, 300)
    test.glViewPort(50, 50, 200, 200)
    test.glColor(1, 1, 1)
    test.glOpenModel('cube3.obj', (2, 2, 2), (50, 50, 50))
    test.glFinish()