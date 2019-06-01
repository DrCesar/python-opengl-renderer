from opengl.main import OpenGl
from opengl.models.shaders import gouraud

def transformations():
    # test = OpenGl()
    # test.glInit(output_dir='out/sr6', name='image', trans_flag=True)
    # test.glCreateWindow(500, 500)
    # test.glViewPort(0, 0, 500, 500)
    # test.glColor(1, 1, 1)
    # test.glOpenModel('models/sphere.obj', translate=(0, 0, 0), scale=(0.5, 0.5, 0.5), shader=gouraud)
    # test.glFinish()

    # test = OpenGl()
    # test.glInit(output_dir='out/sr6', name='medium_shot', trans_flag=True)
    # test.glCreateWindow(500, 500)
    # test.glViewPort(0, 0, 500, 500)
    # test.glColor(1, 1, 1)
    # test.glOpenModel('models/batman.obj', translate=(0, -0.6, 0), scale=(0.4, 0.4, 0.4), rotate=(0, 0, 0))
    # test.glFinish()

    test = OpenGl()
    test.glInit(output_dir='out/sr6', name='dutch_angle', trans_flag=True)
    test.glCreateWindow(500, 500)
    test.glViewPort(0, 0, 500, 500)
    test.glColor(1, 1, 1)
    test.glOpenModel('models/batman.obj', translate=(-1.2, -1.3, 0), scale=(0.7, 0.7, 0.7), rotate=(0, 0, -0.8))
    test.glFinish()

    # test = OpenGl()
    # test.glInit(output_dir='out/sr6', name='low_angle', trans_flag=True)
    # test.glCreateWindow(500, 500)
    # test.glViewPort(0, 0, 500, 500)
    # test.glColor(1, 1, 1)
    # test.glOpenModel('models/batman.obj', translate=(0, -2, 0), scale=(0.7, 0.7, 0.7), rotate=(-0.4, 0, 0))
    # test.glFinish()

    # test = OpenGl()
    # test.glInit(output_dir='out/sr6', name='high_angle', trans_flag=True)
    # test.glCreateWindow(500, 500)
    # test.glViewPort(0, 0, 500, 500)
    # test.glColor(1, 1, 1)
    # test.glOpenModel('models/batman.obj', translate=(0, -2, 0), scale=(0.7, 0.7, 0.7), rotate=(0.5, 0, 0))
    # test.glFinish()