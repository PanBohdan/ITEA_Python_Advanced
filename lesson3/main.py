class Coords:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def set_z(self, z):
        self._z = z

    def get_z(self):
        return self._z

    def set_y(self, y):
        self._y = y

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def get_x(self):
        return self._x

    def __add__(self, other):
        new_x = self.get_x() + other.get_x()
        new_y = self.get_y() + other.get_y()
        new_z = self.get_z() + other.get_z()
        new_coords = Coords(new_x, new_y, new_z)
        return new_coords

    def __sub__(self, other):
        new_x = self.get_x() - other.get_x()
        new_y = self.get_y() - other.get_y()
        new_z = self.get_z() - other.get_z()
        new_coords = Coords(new_x, new_y, new_z)
        return new_coords

    def __mul__(self, other):
        new_x = self.get_x() * other.get_x()
        new_y = self.get_y() * other.get_y()
        new_z = self.get_z() * other.get_z()
        new_coords = Coords(new_x, new_y, new_z)
        return new_coords

    def __truediv__(self, other):
        new_x = self.get_x() / other.get_x()
        new_y = self.get_y() / other.get_y()
        new_z = self.get_z() / other.get_z()
        new_coords = Coords(new_x, new_y, new_z)
        return new_coords

    def __neg__(self):
        new_x = self.get_x()*-1
        new_y = self.get_x()*-1
        new_z = self.get_x()*-1
        new_coords = Coords(new_x, new_y, new_z)
        return new_coords

    def get_all_coords(self):
        return self._x, self._y, self._z


coords = Coords(1, 2, 3)
other_coords = Coords(1, 2, 3)
multiplied = coords * other_coords
print(multiplied.get_all_coords())
divided = coords/other_coords
print(divided.get_all_coords())
summed = coords+other_coords
print(summed.get_all_coords())
subtracted = coords-other_coords
print(subtracted.get_all_coords())
minused = -coords
print(minused.get_all_coords())
print(coords.get_all_coords())
