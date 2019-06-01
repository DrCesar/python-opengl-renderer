from opengl.main import OpenGl
from opengl.models.shaders import batarang_shader, gouraud, batman_shader, batmobile_shader

def project():
    test = OpenGl()

    test.glInit(output_dir='out/project', name='image', trans_flag=True)
    test.glCreateWindow(image='models/background.bmp')
    # test.glCreateWindow(500, 500)
    test.glViewPort(0, 0, 500, 500)
    test.glColor(0, 0, 0)
    test.glOpenModel('models/batman.obj', translate=(1.5, -0.7, -20), scale=(0.37, 0.37, 0.37), rotate=(-0.02, -0.5, 0), shader=batman_shader)
    test.glColor(1, 1, 1)
    # test.glOpenModel('models/batarang.obj', translate=(0.6, -0.2, 10), scale=(0.006, 0.006, 0.006), rotate=(-0.6, 1.2, -0.3), shader=batarang_shader)
    # test.glOpenModel('models/batmobile.obj', 'models/batmobile.bmp', translate=(2.5, -0.5, -30), scale=(0.16, 0.16, 0.16), rotate=(0.12, 0.6, -0.03), shader=batmobile_shader)
    # test.glOpenModel('models/joker.obj', 'models/joker.bmp', translate=(-0.2, -1.8, 16), scale=(0.2, 0.2, 0.2), rotate=(0, 3, 0))
    test.glFinish() 