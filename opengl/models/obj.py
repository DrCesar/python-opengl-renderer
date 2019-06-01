

def safe_int(val):
    try:
        return int(val)
    except (ValueError, TypeError):
        return 0

class Obj(object):
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines = f.read().splitlines()
        self.vertices = []
        self.texture_vertices = []
        self.normals = []
        self.faces = []
        self.max = 0
        self.z_max = 0
        self.z_min = 0
        self.read()

    def read(self):
        for line in self.lines:
            if line:
                prefix, value = line.split(' ', 1)
                if prefix == 'v':
                    self.vertices.append(list(map(float, value.split(' '))))
                    for x in value.split(' '):
                        if abs(float(x)) > self.max:
                            self.max = float(x)
                elif prefix == 'vt':
                    self.texture_vertices.append(list(map(float, value.split(' '))))
                elif prefix == 'vn':
                    self.normals.append(list(map(float, value.split(' '))))
                elif prefix == 'f':
                    self.faces.append([list(map(safe_int, face.split('/'))) for face in value.split(' ')])