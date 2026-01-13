from typing import List

import constants
import copy
import stack
import globalfunctions
from piece import Piece
from src.refactored.coordinates import Coordinate
from src.refactored.piece import Colour


class Board: # FIXME: Large class

    def __init__(self):
        self.othelloBoard: List[List[Piece]] = []
        self.moves = []

    def print_board(self):  # Used to print the current state of the board.
        print(
            " ", end=" "
        )  # Prints a blank space to compensate for the side indicators.
        for x in range(len(self.othelloBoard)):
            print(x + 1, end=" ")  # X indicators
        print(" ")
        for y in range(len(self.othelloBoard)):
            print(y + 1, end=" ")  # Y indicators
            for x in range(len(self.othelloBoard)):
                coordinate = Coordinate(x=x,y=y)
                print(self.get_piece(coordinate).colour, end=" ")  # Prints out each row of the board.
            print(
                " "
            )

    def get_possible_moves(self, colour:Colour):


    def coordinate_is_in_bounds(self, coordinate: Coordinate) -> bool:
        if not (0 < coordinate.x < len(self.othelloBoard)):
            return False
        if not (0 < coordinate.y < len(self.othelloBoard)):
            return False
        return True

    def coordinate_is_valid_move(self, coordinate: Coordinate):
        # TODO: IMPLEMENT ME
        return True

    def validate_coordinates(self, coordinate: Coordinate) -> bool:
        return self.coordinate_is_in_bounds(coordinate) & self.coordinate_is_valid_move(coordinate)


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
        if not self.validate_coordinates(coordinate):
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

    def undo_move(self):
        pass

    def redo_move(self):
        pass

    def undoMove(self):  # Method to undo the last done move.
        Coordinate = (
            self.undoRedoMoves.getUndoMoveCoordinates()
        )  # Gets the coordinates from the stack
        if (
            Coordinate == False
        ):  # If the stack returns false, there are no moves left to undo and therefore it is displayed
            print("Unable to undo move, no moves left to undo.")
            return False
        offsets = constants.OFFSETS  # Loads the offsets from the constants file.
        pieceX = Coordinate[
            0
        ]  # Breaks down the coordinate list output to x,y and piece.
        pieceY = Coordinate[1]
        pieceColor = Coordinate[2]
        oppositePieceColor = self._swapColor(
            pieceColor
        )  # Gets the oppositeColor by swapping the color of the pieceColor variable.
        self.othelloBoard[pieceY][
            pieceX
        ] = constants.BLANK  # Sets the specified coordinates to blank.
        for offset in offsets:  # Cycles through all of the offsets.
            flipPieces = []  # Clears/Initialises the flipPieces list.
            overallOffset = copy.copy(
                offset
            )  # Copies the offset into the overallOffset variable.
            while (
                True
            ):  # this loop is broken if the piece is blank, or if an enemy piece is found.
                checkX = (
                    pieceX + overallOffset[0]
                )  # Adds the offset and original coordinates together to get the coordinates of the spot to search.
                checkY = pieceY + overallOffset[1]
                if checkX not in range(0, constants.BOARDX) or checkY not in range(
                    0, constants.BOARDY
                ):  # If the coordinates of the spot to search are out of range of the board, break the loop and search in another direction.
                    break
                pieceToCheck = self.othelloBoard[checkY][
                    checkX
                ]  # If the coordinates are in range, get the value of the piece at the specified coordinates
                if (
                    pieceToCheck == pieceColor
                ):  # If the piece is friendly, ammend this to the flipPieces list.
                    flipPieces.append([checkX, checkY])
                    overallOffset[0] += offset[0]
                    overallOffset[1] += offset[1]
                elif (
                    pieceToCheck == oppositePieceColor
                ):  # If the piece is an enemy piece, remove the last coordinate from the flipPieces list and flip all the pieces to be enemy pieces.
                    if len(flipPieces) > 0:
                        flipPieces.pop()
                        for piece in flipPieces:
                            self.othelloBoard[piece[1]][piece[0]] = oppositePieceColor
                    break
                elif (
                    pieceToCheck == constants.BLANK
                ):  # If the piece is blank, break the loop.
                    if len(flipPieces) > 0:
                        flipPieces.pop()
                        for piece in flipPieces:
                            self.othelloBoard[piece[1]][piece[0]] = oppositePieceColor
                    break
                else:
                    globalfunctions.reportError(0)
                    return False
        return pieceColor  # Once all the directions have been searched, return the original piece color.

    def redoMove(self):  # Method to redo the last undone move
        Coordinate = (
            self.undoRedoMoves.getRedoMoveCoordinates()
        )  # Gets the coordinates from the stack
        if ( # FIXME: Unnecessary nesting, can be avoided with guard clause
            Coordinate != False
        ):  # As long as the coordinate is not false, attempt to place the piece as normal and return the original color of that piece.
            self.placePiece(Coordinate[0], Coordinate[1], Coordinate[2], False)
            return self._swapColor(Coordinate[2])
        else:  # If the coordinate is false, return False and display to the user that there are no moves left to undo.
            return False

    def getBoard(self):
        return self.othelloBoard

    def getStackContents(self):
        return self.undoRedoMoves.getStackContents()
