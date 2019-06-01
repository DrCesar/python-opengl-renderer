from opengl.main import OpenGl
from opengl.models.shaders import planet_shader, gouraud

def shaders():
    test = OpenGl()

    test.glInit(output_dir='out/lab3', name='image', trans_flag=True)
    test.glCreateWindow(500, 500)
    test.glViewPort(0, 0, 500, 500)
    test.glColor(1, 1, 1)
    test.glOpenModel('models/ball.obj', translate=(0, 0, 0), scale=(0.5, 0.5, 0.5), shader=planet_shader)
    test.glFinish()