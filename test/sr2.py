from opengl.main import OpenGl

def test_line():
    test = OpenGl()

    test.glInit(output_dir='out/sr2', name='sr2.bmp')
    test.glCreateWindow(300, 300)
    test.glViewPort(0, 0, 300, 300)
    test.glColor(1, 1, 1)
    test.glLine(0, 0, -1, -1)
    test.glLine(-1, 1, 0, -1)
    test.glLine(1, -1, 0, 0)
    test.glFinish()