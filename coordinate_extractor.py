from pynput import mouse


class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class CoordinateExtractor:

    def __init__(self):
        pass

    def from_mouse_pointer(self):
        left = mouse.Button.left
        return Coordinate()