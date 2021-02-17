class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, mass1sqm1cm=25, thickness=5):
        return self._length * self._width * mass1sqm1cm * thickness


road_1 = Road(5000, 20)
print(road_1.mass())
