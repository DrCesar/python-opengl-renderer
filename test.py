
import sys


from test.sr2 import test_line
from test.sr3 import test_model
from test.sr4 import gen_zbuffer
from test.sr5 import paint_with_texture
from test.sr6 import transformations

from test.lab1 import fill_polygon
from test.lab3 import shaders

from test.project import project

if len(sys.argv) > 1:
    if sys.argv[1] == 'line' or sys.argv[1] == 'sr2':
        test_line() 
    elif sys.argv[1] == 'model' or sys.argv[1] == 'sr3':
        test_model()
    elif sys.argv[1] == 'zbuffer' or sys.argv[1] == 'sr4':
        gen_zbuffer()
    elif sys.argv[1] == 'fill' or sys.argv[1] == 'lab1':
        fill_polygon()
    elif sys.argv[1] == 'texture' or sys.argv[1] == 'sr5':
        paint_with_texture()
    elif sys.argv[1] == 'trans' or sys.argv[1] == 'sr6':
        transformations()
    elif sys.argv[1] == 'shaders' or sys.argv[1] == 'lab3':
        shaders()
    elif sys.argv[1] == 'project':
        project()


# test = OpenGl()

# test.glInit()
# test.glCreateWindow(300, 300)
# test.glViewPort(0, 0, 300, 300)
# test.glColor(1, 1, 1)
# test.glVertex(0.1,0.1)
# test.glVertex(0.15,0.15)
# test.glLine(0, 0, -1, -1)
# test.glFinish()