
import sys


from test.sr2 import test_line
from test.sr3 import test_model
from test.lab1 import fill_polygon
from test.sr5 import paint_with_texture

if len(sys.argv) > 1:
    if sys.argv[1] == 'line':
        test_line() 
    elif sys.argv[1] == 'model':
        test_model()
    elif sys.argv[1] == 'fill':
        fill_polygon()
    elif sys.argv[1] =='texture':
        paint_with_texture()


# test = OpenGl()

# test.glInit()
# test.glCreateWindow(300, 300)
# test.glViewPort(0, 0, 300, 300)
# test.glColor(1, 1, 1)
# test.glVertex(0.1,0.1)
# test.glVertex(0.15,0.15)
# test.glLine(0, 0, -1, -1)
# test.glFinish()