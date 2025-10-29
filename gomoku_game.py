"""
Gomoku Game Logic Engine
Core game mechanics: board, rules, win detection
"""

import numpy as np
from enum import Enum


class Player(Enum):
    """Player enumeration"""
    EMPTY = 0
    BLACK = 1
    WHITE = 2


class GomokuGame:
    """
    Core Gomoku Game Logic
    - Manages board state
    - Enforces game rules
    - Detects win conditions
    """

    def __init__(self, board_size=15):
        """Initialize the game"""
        self.board_size = board_size
        self.board = np.zeros((self.board_size, self.board_size), dtype=np.int8)
        self.current_player = Player.BLACK
        self.game_over = False
        self.winner = None
        self.move_history = []

    def make_move(self, row, col):
        """
        Make a move on the board

        Args:
            row: Row index (0-14)
            col: Column index (0-14)

        Returns:
            tuple: (success, result)
                - success: bool - True if move was valid
                - result: str - Message describing the result
        """
        # Validate coordinates
        if not (0 <= row < self.board_size and 0 <= col < self.board_size):
            return False, "Invalid coordinates"

        # Check if position is empty
        if self.board[row, col] != Player.EMPTY.value:
            return False, "Position already occupied"

        # Place the piece
        self.board[row, col] = self.current_player.value
        self.move_history.append((row, col))

        # Check for win
        if self.check_win(row, col, self.current_player):
            self.game_over = True
            self.winner = self.current_player
            return True, "WIN"

        # Switch player
        self.current_player = Player.WHITE if self.current_player == Player.BLACK else Player.BLACK
        return True, "OK"

    def undo_move(self):
        """
        Undo the last move

        Returns:
            tuple: (success, result)
                - success: bool - True if undo was successful
                - result: str - Message describing the result
        """
        if len(self.move_history) < 2:
            return False, "Not enough moves to undo"

        if self.game_over:
            return False, "Cannot undo after game over"

        # Remove last two moves (one from each player)
        last_row, last_col = self.move_history.pop()
        self.board[last_row, last_col] = Player.EMPTY.value

        last_row, last_col = self.move_history.pop()
        self.board[last_row, last_col] = Player.EMPTY.value

        # Reset game over state
        if len(self.move_history) > 0:
            self.current_player = Player.BLACK if len(self.move_history) % 2 == 1 else Player.WHITE
        else:
            self.current_player = Player.BLACK

        return True, "OK"

    def check_win(self, row, col, player):
        """
        Check if the current move resulted in a win

        Args:
            row: Row index of the last move
            col: Column index of the last move
            player: Player enum who made the move

        Returns:
            bool - True if player has 5 or more in a row
        """
        directions = [
            (0, 1),   # Horizontal
            (1, 0),   # Vertical
            (1, 1),   # Diagonal \
            (1, -1)   # Diagonal /
        ]

        for dr, dc in directions:
            count = 1

            # Count in positive direction
            r, c = row + dr, col + dc
            while 0 <= r < self.board_size and 0 <= c < self.board_size:
                if self.board[r, c] == player.value:
                    count += 1
                    r += dr
                    c += dc
                else:
                    break

            # Count in negative direction
            r, c = row - dr, col - dc
            while 0 <= r < self.board_size and 0 <= c < self.board_size:
                if self.board[r, c] == player.value:
                    count += 1
                    r -= dr
                    c -= dc
                else:
                    break

            if count >= 5:
                return True

        return False

    def reset(self):
        """Reset the game to initial state"""
        self.board = np.zeros((self.board_size, self.board_size), dtype=np.int8)
        self.current_player = Player.BLACK
        self.game_over = False
        self.winner = None
        self.move_history = []

    def get_board(self):
        """Get current board state"""
        return self.board.copy()

    def get_move_history(self):
        """Get list of all moves made"""
        return self.move_history.copy()

    def get_game_state(self):
        """Get complete game state"""
        return {
            'board': self.get_board(),
            'current_player': self.current_player,
            'game_over': self.game_over,
            'winner': self.winner,
            'move_count': len(self.move_history),
            'moves': self.get_move_history()
        }
