from opengl.main import OpenGl

def transformations():
    test = OpenGl()

    test.glInit(texture_file='texture.bmp', trans_flag=True)
    test.glCreateWindow(300, 300)
    test.glViewPort(50, 50, 200, 200)
    test.glColor(1, 1, 1)
    test.glOpenModel('cube4.obj', (2, 2, 2), (2, 2, 2))
    test.glFinish()