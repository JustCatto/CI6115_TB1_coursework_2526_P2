import constants
import copy
import globalfunctions



class Board: # FIXME: Large class

    def __init__(self):
        self.othelloBoard = []

    def _swapColor( # FIXME: Duplicate Code/Misplaced function
            self, color
    ):  # Method that flips the color that is input. For example if black is input, return white, and vice versa.
        if color == constants.BLACK:
            return constants.WHITE
        elif color == constants.WHITE:
            return constants.BLACK
        else:
            globalfunctions.reportError(
                0
            )  # If the function is improperly called, return an error.
            return False

    def generateBoard( #
        self,
    ):  # Method that generates the board and places down the starting pieces.
        self.othelloBoard = [
            [constants.BLANK for x in range(constants.BOARDX)] # FIXME: Poor naming
            for y in range(constants.BOARDY)
        ]  # Initialises the board using the dimentions in the constants file.
        self.piece = constants.BLACK
        for x in range(
            2
        ):  # These lines are then responsible for placing the starting pieces.
            self.piece = self._swapColor(self.piece)
            for y in range(2):
                self.othelloBoard[y + 3][x + 3] = self.piece # FIXME: Magic value
                self.piece = self._swapColor(self.piece)

    def placePiece( # FIXME: Long function
        self, x, y, piece, logPiece
    ):  # Method that places down the piece at the specified coordinates and flips any pieces that become directly surrounded by the piece and another friendly piece.
        offsets = constants.OFFSETS  # Loads the offsets from the constants file. # FIXME: Shotgun surgery. Can be achieved with for loops.
        self.othelloBoard[y][
            x
        ] = piece  # Sets the spot at the specified coordinates to the piece.
        oppositePiece = self._swapColor(
            piece
        )  # Finds the opposite piece by swapping the color of the originally specified piece.
        if logPiece == True:
            self.undoRedoMoves.pushCoordinates(
                x, y, piece
            )  # Pushes coordinates to the undoRedoMove stack so then it may be undone.
        for offset in offsets:  # Cycles through all the offsets.
            flipPieces = (
                []
            )  # Clears the flipPieces list each time to make sure no coordinates are carried over.
            overallOffset = copy.copy(
                offset
            )  # Takes a copy of the current offset and stores it as the total offset.
            while (
                True
            ):  # Loops while the pieces that are being scanned are not friendly pieces or blank pieces.
                checkY = (
                    y + overallOffset[1]
                )  # Adds the original coordinates plus the offsets to find the coordinates to search.
                checkX = x + overallOffset[0]
                # FIXME: Complex conditional. Logic should be broken into helper methods.
                if checkY not in range(0, constants.BOARDY) or checkX not in range(
                    0, constants.BOARDX
                ):  # If the coordinates to search arent in range of the board, break the loop and search in another direction.
                    break
                pieceToCheck = self.othelloBoard[checkY][
                    checkX
                ]  # Get the value of the piece at the coordinates to scan.
                if (
                    pieceToCheck == piece
                ):  # If the piece is friendly, flip all the pieces in the flipPieces list.
                    for flipPiece in flipPieces:
                        self.othelloBoard[flipPiece[1]][flipPiece[0]] = piece
                    break
                elif (
                    pieceToCheck == constants.BLANK
                ):  # If the piece is blank, clear the flipPieces list and break the while True loop as there can be no pieces to flip in this direction.
                    flipPieces = []
                    break
                elif (
                    pieceToCheck == oppositePiece # FIXME: Middle man
                ):  # If the piece is an enemy piece, log the coordinates down in the flipPieces list and add the original offset to the total offset.
                    flipPieces.append([checkX, checkY])
                    overallOffset[1] += offset[1]
                    overallOffset[0] += offset[0]
