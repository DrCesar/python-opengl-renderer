
import timeit



def measure_model():
    # test = OpenGl()

    print(timeit.timeit('test.glInit()', setup='from opengl.main import OpenGl; test = OpenGl()'))
