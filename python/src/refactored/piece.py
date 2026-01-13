from enum import Enum

class Colour(Enum):
    WHITE = "X"
    BLACK = "Y"
    BLANK = "-"

    def opposite(self):
        if self == Colour.BLANK:
            return Colour.BLANK
        return Colour.BLACK if self == Colour.WHITE else Colour.WHITE



class Piece:

    def __init__(self):
        self.colour: Colour = Colour.BLANK

    def set_piece(self, colour: Colour):
        self.colour = colour

    def flip_piece(self):
        if self.colour == Colour.BLANK:
            return
        self.colour = self.colour.opposite()

