from opengl.main import OpenGl

def paint_with_texture():
    test = OpenGl()

    test.glInit(texture_file='texture.bmp')
    test.glCreateWindow(300, 300)
    test.glViewPort(50, 50, 200, 200)
    test.glColor(1, 1, 1)
    test.glOpenModel('cub4.obj', (2, 2, 2), (50, 50, 50))
    test.glFinish()