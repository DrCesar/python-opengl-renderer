from opengl.main import OpenGl

def paint_with_texture():
    test = OpenGl()

    test.glInit(texture_file='texture.bmp')
    test.glCreateWindow(300, 300)
    test.glViewPort(50, 50, 200, 200)
    test.glColor(1, 1, 1)
    test.glOpenModel('cube4.obj', (200, 200, 200), (50, 50, 50))
    test.glFinish()