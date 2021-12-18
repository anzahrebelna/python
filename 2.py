class Road:
    def __init__(self,_lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def mass(self):
        return self._lenght * self._width * 25 * 5

road = Road(20000, 20)

print(f'{road.mass()}kg')