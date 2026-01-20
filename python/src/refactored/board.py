from typing import List

from piece import Piece
from src.refactored.coordinates import Coordinate
from src.refactored.piece import Colour


class Board: # FIXME: Large class

    def __init__(self):
        self.othelloBoard: List[List[Piece]] = []

    def coordinate_is_in_bounds(self, coordinate: Coordinate) -> bool:
        if not (0 < coordinate.x < len(self.othelloBoard)):
            return False
        if not (0 < coordinate.y < len(self.othelloBoard)):
            return False
        return True

    def coordinate_is_valid_move(self, coordinate: Coordinate, color: Colour):
        return len(self.get_cascading_pieces(coordinate, color)) == 0


    def validate_coordinates(self, coordinate: Coordinate, color: Colour) -> bool:
        return self.coordinate_is_in_bounds(coordinate) & self.coordinate_is_valid_move(coordinate, color)


    def generate_board(self, area: int):
        self.othelloBoard = [
            [Piece() for x in range(area)] for y in range(area)
        ]
        self.place_starting_pieces()

    def place_starting_pieces(self):
        offset = len(self.othelloBoard)
        current_colour = Colour.WHITE
        for x in range(2):
            for y in range(2):
                coordinate = Coordinate(
                    x = x + offset,
                    y = y + offset
                )
                piece = self.get_piece(coordinate)
                piece.set_piece(current_colour)
                current_colour = current_colour.opposite()


    def get_piece(self, coordinate: Coordinate):
        return self.othelloBoard[coordinate.x][coordinate.y]

    def place_piece(self, coordinate: Coordinate, colour: Colour):
        if not self.validate_coordinates(coordinate, colour):
            return
        piece = self.get_piece(coordinate)
        if piece != Colour.BLANK:
            return
        self.get_cascading_pieces(coordinate,colour)

    def get_cascading_pieces(self, coordinate: Coordinate, colour: Colour):
        cascading: List[Piece] = []
        for x in range(-1, 1 + 1 ,1):
            for y in range(-1, 1 + 1 ,1):
                to_flip: List[Piece] = []
                offset = Coordinate(x=x,y=y)
                to_flip = self.check_direction(colour,coordinate,offset,to_flip)
                cascading.append(to_flip)
        return cascading

    def check_direction(self, colour:Colour, current_coordinate: Coordinate, offset: Coordinate, to_flip: List[Piece]):
        newCoordinate = current_coordinate + offset
        if not self.coordinate_is_in_bounds(newCoordinate):
            return to_flip
        piece = self.get_piece(newCoordinate)
        if piece.colour == colour.opposite():
            to_flip.append(piece)
            return self.check_direction(colour,newCoordinate,offset,to_flip)
        else:
            return to_flip


