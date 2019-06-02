
from opengl.main import OpenGl

def test_model():
    test = OpenGl()

    test.glInit(output_dir='out/sr3', name='image',)
    test.glCreateWindow(300, 300)
    test.glViewPort(50, 50, 200, 200)
    test.glColor(1, 1, 1)
    test.glOpenModel('cube3.obj', translate=(150, 150, 0), scale=(50, 50, 50))
    test.glFinish()