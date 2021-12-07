class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass(self):
        mass = self._length * self._width * 25 * (5 / 100)
        return mass

new_road = Road(10, 20)
print(new_road.get_mass())
