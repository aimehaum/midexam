class Furniture:
    def __init__(self, weight, material):
        self.weight = weight
        self.material = material

class Bed(Furniture):
    def bedsize(self, size):
        self.size = size
