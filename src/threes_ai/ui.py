from abc import ABC

import numpy as np


class IUi(ABC):
    """Interface for UI classes."""

    @staticmethod
    def game_over(board):
        """Print game over message and final score."""
        ...

    @staticmethod
    def get_move(valid_moves):
        """Get move from user."""
        ...

    @staticmethod
    def show_board(board, next_tiles):
        """Print board and next tile(s)."""
        ...


class TextUi(IUi):
    """Text-based UI."""

    MOVE_SYMBOLS = "UDLR"

    @staticmethod
    def game_over(board):
        """Print game over message and final score."""
        print("Game over.")
        your_score = TextUi.to_score(board).sum()
        print(f"Your score: {your_score}.")

    @staticmethod
    def get_move(self, valid_moves):
        """Get move from user."""

        # Convert valid moves from indices to symbols
        valid_move_symbols = "".join(self.MOVE_SYMBOLS[i] for i in valid_moves)

        while True:
            # Get move
            move = input(f"Move {valid_move_symbols}? ").upper()

            # Check if move is valid
            if move not in valid_move_symbols:
                print("Invalid move.")
                continue

            # Convert move to index
            move = "UDLR".find(move)
            return move

    @staticmethod
    def show_board(board, next_tiles):
        """Print board and next tile(s)."""
        TextUi.pprint_board(board)
        print("next tile:", list(TextUi.to_val(next_tiles)))

    @staticmethod
    def pprint_board(board):
        """Pretty-print board."""
        print("┌────┬────┬────┬────┐")
        for i in range(4):
            print("│", end="")
            for j in range(4):
                print(f"{TextUi.to_val(board[i, j]):4}", end="│")
            print()
            if i < 3:
                print("├────┼────┼────┼────┤")
        print("└────┴────┴────┴────┘")

    @staticmethod
    def to_val(x):
        """Convert tile value to printable value."""
        x = np.asarray(x)
        min0 = np.where(x < 3, 0, x - 3)
        return np.where(x < 3, x, 3 * (2**min0))

    @staticmethod
    def to_score(x):
        x = np.asarray(x)
        min0 = np.where(x < 2, 0, x - 2)
        return np.where(x < 3, 0, 3**min0)
