from opengl.main import OpenGl

def gen_zbuffer():
    test = OpenGl()

    test.glInit(output_dir='out/sr4', name='image', flag_zbuffer=True)
    test.glCreateWindow(300, 300)
    test.glViewPort(0, 0, 300, 300)
    test.glColor(1, 1, 1)
    test.glOpenModel('cube3.obj', translate=(100, 100, 0), scale=(50, 50, 50))
    test.glFinish()