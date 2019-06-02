from opengl.main import OpenGl

def paint_with_texture():
    test = OpenGl()

    test.glInit(output_dir='out/sr5', flag_texture=True)
    test.glCreateWindow(500, 500)
    test.glViewPort(0, 0, 500, 500)
    test.glColor(1, 1, 1)
    # test.glOpenModel('models/batmobile.obj', 'models/batmobile.bmp', (250, 10, 0), (10, 10, 10))
    # test.glOpenModel('models/batman.obj', 'models/batman.bmp', (250, 0, 0), (100, 100, 50))
    test.glOpenModel('models/sphere.obj', 'models/sphere.bmp', (250, 250, 0), (100, 100, 50))
    # test.glOpenModel('models/face.obj', 'models/face.bmp', (200, -250, 10), (200, 200, 50))
    # test.glOpenModel('batman2.obj', 'texture-2.bmp', (300, -100, 10), (50, 100, 50))
    test.glFinish()