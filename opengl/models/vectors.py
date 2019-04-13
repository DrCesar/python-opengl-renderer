


class V3(object):
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return V3(self.x + other, self.y + other, self.z + other)
        elif isinstance(other, V3):
            return V3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return V3(self.x - other, self.y - other, self.z - other)
        elif isinstance(other, V3):
            return V3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return V3(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, V3):
            return V3(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x
            )

    def __matmul__(self, other):
        if isinstance(other, V3):
            return V3(1, 2, 1)

    def __len__(self):
        return 3

    def __getitem__(self, index):
        return (self.x, self.y, self.z)[index]

        return 0

    def __str__(self):
        return 'V3(%s, %s, %s)' % (self.x, self.y, self.z)