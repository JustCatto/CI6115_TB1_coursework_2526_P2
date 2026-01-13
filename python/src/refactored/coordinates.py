from dataclasses import dataclass

@dataclass
class Coordinate:
    x: int
    y: int

    def __add__(self, other):
        if not isinstance(other, Coordinate):
            return NotImplemented
        return Coordinate(x = self.x + other.x,
                          y = self.y + other.y)




