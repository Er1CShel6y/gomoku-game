"""
Gomoku Game GUI
Tkinter-based graphical user interface for Gomoku game
"""

import tkinter as tk
from tkinter import messagebox
from gomoku_game import GomokuGame, Player


class GomokuGUI:
    """
    Gomoku Game with Tkinter GUI - Premium Modern Design
    - Beautiful graphical 15x15 board with enhanced visuals
    - Mouse click to place pieces with smooth animations
    - Real-time win detection with visual effects
    - Modern premium UI with gradient-like effects
    - Dark theme with elegant color scheme
    """

    # Premium color scheme - Dark theme with gradient
    BG_COLOR = "#0f0f23"           # Deep dark background
    HEADER_COLOR = "#1a1a3e"       # Premium dark header
    ACCENT_COLOR = "#2a2d5a"       # Premium accent (blue-purple)
    TEXT_COLOR = "#f0f0f0"         # Bright light text
    BOARD_COLOR = "#c9a561"        # Premium warm board color
    GRID_COLOR = "#8b7355"         # Grid lines
    BUTTON_COLOR = "#ff6b9d"       # Modern pink accent
    BUTTON_HOVER = "#ff85ad"       # Lighter pink on hover
    SUCCESS_COLOR = "#4ecca3"      # Green for success
    INFO_COLOR = "#6fa8dc"         # Blue for info

    def __init__(self, root):
        """Initialize the GUI"""
        self.root = root
        self.root.title("⚫ Gomoku Game - Five in a Row Strategy Game")
        self.root.resizable(False, False)

        # Game engine
        self.game = GomokuGame(board_size=15)
        self.cell_size = 50

        # 计算合适的窗口大小：棋盘大小 + UI 边距
        canvas_size = self.cell_size * self.game.board_size + 30  # 棋盘大小
        window_height = 100 + 20 + canvas_size + 80 + 30  # header + margin + canvas + status + padding
        window_width = canvas_size + 30
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.configure(bg=self.BG_COLOR)

        # Setup UI
        self._create_ui()

    def _create_ui(self):
        """Create all UI components"""
        # Create main frame
        self.main_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Create header frame
        self._create_header()

        # Create info frame
        self._create_info_frame()

        # Create canvas for board
        self._create_canvas()

        # Create status frame
        self._create_status_frame()

        # Draw initial board
        self.draw_board()

    def _create_header(self):
        """Create header section with premium title design"""
        self.header_frame = tk.Frame(self.main_frame, bg=self.HEADER_COLOR, height=90)
        self.header_frame.pack(fill=tk.X, pady=(0, 20))
        self.header_frame.pack_propagate(False)

        # Title with emoji and enhanced styling
        self.title_label = tk.Label(
            self.header_frame,
            text="⚫ Gomoku ⚪",
            font=("Arial", 32, "bold"),
            bg=self.HEADER_COLOR,
            fg=self.BUTTON_COLOR
        )
        self.title_label.pack(pady=10)

        # Subtitle
        self.subtitle_label = tk.Label(
            self.header_frame,
            text="Five in a Row • Strategy Game",
            font=("Arial", 11),
            bg=self.HEADER_COLOR,
            fg=self.INFO_COLOR
        )
        self.subtitle_label.pack(pady=(0, 5))

    def _create_info_frame(self):
        """Create premium info frame with player info and buttons"""
        self.info_frame = tk.Frame(self.main_frame, bg=self.ACCENT_COLOR)
        self.info_frame.pack(fill=tk.X, pady=(0, 20), padx=5)

        # Left info section with enhanced layout
        left_info = tk.Frame(self.info_frame, bg=self.ACCENT_COLOR)
        left_info.pack(side=tk.LEFT, padx=20, pady=15)

        # Current player indicator with icon
        self.player_label = tk.Label(
            left_info,
            text="🎮 Current Player: Black",
            font=("Arial", 12, "bold"),
            bg=self.ACCENT_COLOR,
            fg=self.TEXT_COLOR
        )
        self.player_label.pack(side=tk.LEFT, padx=10)

        # Separator
        separator = tk.Label(
            left_info,
            text="│",
            font=("Arial", 12),
            bg=self.ACCENT_COLOR,
            fg=self.INFO_COLOR
        )
        separator.pack(side=tk.LEFT, padx=5)

        # Move counter with icon
        self.move_label = tk.Label(
            left_info,
            text="📊 Moves: 0",
            font=("Arial", 12, "bold"),
            bg=self.ACCENT_COLOR,
            fg=self.TEXT_COLOR
        )
        self.move_label.pack(side=tk.LEFT, padx=10)

        # Right buttons section
        right_buttons = tk.Frame(self.info_frame, bg=self.ACCENT_COLOR)
        right_buttons.pack(side=tk.RIGHT, padx=20, pady=15)

        # Undo button
        self.undo_button = tk.Button(
            right_buttons,
            text="↶ Undo",
            font=("Arial", 10, "bold"),
            command=self.undo_move,
            bg="#6fa8dc",
            fg="white",
            padx=15,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2",
            activebackground="#85b9e8",
            activeforeground="white"
        )
        self.undo_button.pack(side=tk.LEFT, padx=5)

        # Reset button with enhanced style
        self.reset_button = tk.Button(
            right_buttons,
            text="🔄 Restart",
            font=("Arial", 10, "bold"),
            command=self.reset_game,
            bg=self.BUTTON_COLOR,
            fg="white",
            padx=15,
            pady=8,
            relief=tk.FLAT,
            cursor="hand2",
            activebackground=self.BUTTON_HOVER,
            activeforeground="white"
        )
        self.reset_button.pack(side=tk.LEFT, padx=5)

    def _create_canvas(self):
        """Create canvas for the game board"""
        canvas_width = self.game.board_size * self.cell_size + 20
        canvas_height = self.game.board_size * self.cell_size + 20

        self.canvas = tk.Canvas(
            self.main_frame,
            width=canvas_width,
            height=canvas_height,
            bg=self.BOARD_COLOR,
            highlightthickness=3,
            highlightbackground=self.GRID_COLOR,
            cursor="cross"
        )
        self.canvas.pack(pady=20)
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<Motion>", self.on_canvas_motion)

    def _create_status_frame(self):
        """Create premium status frame for messages"""
        self.status_frame = tk.Frame(self.main_frame, bg=self.ACCENT_COLOR, height=70)
        self.status_frame.pack(fill=tk.X, padx=5)
        self.status_frame.pack_propagate(False)

        # Status message with enhanced styling
        self.status_label = tk.Label(
            self.status_frame,
            text="💡 Click the board to place a stone",
            font=("Arial", 11),
            bg=self.ACCENT_COLOR,
            fg=self.TEXT_COLOR,
            wraplength=600,
            justify=tk.LEFT
        )
        self.status_label.pack(fill=tk.BOTH, padx=15, pady=10, side=tk.LEFT)

        # Last move indicator
        self.last_move_label = tk.Label(
            self.status_frame,
            text="",
            font=("Arial", 9),
            bg=self.ACCENT_COLOR,
            fg=self.INFO_COLOR
        )
        self.last_move_label.pack(fill=tk.BOTH, padx=15, pady=10, side=tk.RIGHT)

    def draw_board(self):
        """Draw the game board with enhanced visuals"""
        self.canvas.delete("all")

        # Draw board background with shadow
        board_x1 = 5
        board_y1 = 5
        board_x2 = 10 + (self.game.board_size - 1) * self.cell_size + 5
        board_y2 = 10 + (self.game.board_size - 1) * self.cell_size + 5

        self.canvas.create_rectangle(board_x1 + 2, board_y1 + 2, board_x2, board_y2,
                                     fill="#c9956f", outline="")
        self.canvas.create_rectangle(board_x1, board_y1, board_x2 - 2, board_y2 - 2,
                                     fill="#d4a574", outline="")

        # Draw grid lines
        for i in range(self.game.board_size):
            x = 10 + i * self.cell_size
            y = 10 + i * self.cell_size
            line_width = 2 if i == 0 or i == self.game.board_size - 1 else 1

            # Vertical lines
            self.canvas.create_line(x, 10, x, 10 + (self.game.board_size - 1) * self.cell_size,
                                   fill="#7a6048", width=line_width)

            # Horizontal lines
            self.canvas.create_line(10, y, 10 + (self.game.board_size - 1) * self.cell_size, y,
                                   fill="#7a6048", width=line_width)

        # Draw star points
        star_positions = [(3, 3), (3, 11), (7, 7), (11, 3), (11, 11)]
        for row, col in star_positions:
            x = 10 + col * self.cell_size
            y = 10 + row * self.cell_size
            self.canvas.create_oval(x - 4, y - 4, x + 4, y + 4,
                                   fill="#8B7355", outline="#6a5644", width=1)

        # Draw pieces
        board = self.game.get_board()
        for row in range(self.game.board_size):
            for col in range(self.game.board_size):
                if board[row, col] != Player.EMPTY.value:
                    self.draw_piece(row, col, board[row, col])

        # Draw last move indicator
        if self.game.move_history:
            last_row, last_col = self.game.move_history[-1]
            x = 10 + last_col * self.cell_size
            y = 10 + last_row * self.cell_size

            self.canvas.create_rectangle(x - 6, y - 6, x + 6, y + 6,
                                        outline="#ff9800", width=2)

            # Draw corner marks
            offset = 6
            for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
                self.canvas.create_line(x + dx * offset, y + dy * (offset - 2),
                                       x + dx * offset, y + dy * offset,
                                       fill="#ff9800", width=2)
                self.canvas.create_line(x + dx * (offset - 2), y + dy * offset,
                                       x + dx * offset, y + dy * offset,
                                       fill="#ff9800", width=2)

    def draw_piece(self, row, col, player_value):
        """Draw a piece on the board with premium 3D effect"""
        x = 10 + col * self.cell_size
        y = 10 + row * self.cell_size
        radius = self.cell_size // 2 - 3

        if player_value == Player.BLACK.value:
            color = "#0d0d0d"
            outline = "#000000"
            shadow_color = "#2a2a2a"
            highlight_color = "#4a4a4a"
            glow_color = "#1a1a1a"
        else:  # WHITE
            color = "#f5f5f5"
            outline = "#b0b0b0"
            shadow_color = "#e0e0e0"
            highlight_color = "#ffffff"
            glow_color = "#f0f0f0"

        # Draw glow effect (outer shadow)
        self.canvas.create_oval(x - radius - 3, y - radius - 3, x + radius + 3, y + radius + 3,
                               fill=glow_color, outline="")

        # Draw shadow for depth
        self.canvas.create_oval(x - radius - 1, y - radius + 1, x + radius + 1, y + radius + 3,
                               fill=shadow_color, outline="")

        # Draw main piece with border
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius,
                               fill=color, outline=outline, width=3)

        # Draw highlight (glossy effect)
        highlight_radius = radius // 2
        self.canvas.create_oval(x - highlight_radius // 2, y - highlight_radius // 2 - 2,
                               x + highlight_radius // 2, y + highlight_radius // 2 - 2,
                               fill=highlight_color, outline="")

    def on_canvas_click(self, event):
        """Handle mouse click on canvas"""
        if self.game.game_over:
            messagebox.showinfo("Game Over", f"Congratulations! {self.game.winner.name} wins!")
            return

        # Convert pixel coordinates to board coordinates
        col = round((event.x - 10) / self.cell_size)
        row = round((event.y - 10) / self.cell_size)

        # Try to make move
        success, result = self.game.make_move(row, col)

        if not success:
            self.status_label.config(text=f"❌ Invalid move: {result}")
            self.root.after(2000, self._update_status)
            return

        # Update display
        self.draw_board()
        self.update_ui()

        # Check for win
        if self.game.game_over:
            winner_emoji = "⚫" if self.game.winner == Player.BLACK else "⚪"
            winner_name = "Black" if self.game.winner == Player.BLACK else "White"
            messagebox.showinfo(
                "🎉 Game Over!",
                f"🎊 Congratulations! {winner_emoji} {winner_name} wins!\n\n"
                f"Total moves: {len(self.game.move_history)}\n\n"
                f"Click 'Restart' to play again!"
            )

    def on_canvas_motion(self, event):
        """Handle mouse motion on canvas"""
        pass

    def update_ui(self):
        """Update UI elements with enhanced styling"""
        # Update current player label with emoji
        if self.game.current_player == Player.BLACK:
            player_color = "Black"
            player_emoji = "⚫"
        else:
            player_color = "White"
            player_emoji = "⚪"

        self.player_label.config(text=f"🎮 Current Player: {player_emoji} {player_color}")

        # Update move counter
        self.move_label.config(text=f"📊 Moves: {len(self.game.move_history)}")

        # Update last move with enhanced display
        if self.game.move_history:
            last_row, last_col = self.game.move_history[-1]
            # Convert to letter-number notation (common in board games)
            col_letter = chr(65 + last_col)  # A, B, C, ...
            self.last_move_label.config(
                text=f"Last: {col_letter}{last_row + 1}"
            )
        else:
            self.last_move_label.config(text="")

        # Update status
        self._update_status()

    def _update_status(self):
        """Update status message"""
        if self.game.game_over:
            winner_name = "Black" if self.game.winner == Player.BLACK else "White"
            self.status_label.config(
                text=f"Game Over! {winner_name} wins!",
                fg="#FFD700"
            )
        else:
            player_color = "Black" if self.game.current_player == Player.BLACK else "White"
            self.status_label.config(
                text=f"Waiting for {player_color}'s move... Click board to place piece",
                fg=self.TEXT_COLOR
            )

    def undo_move(self):
        """Undo the last move"""
        if not self.game.move_history:
            self.status_label.config(text="❌ No moves to undo!", fg="#ff6b6b")
            self.root.after(2000, self._update_status)
            return

        # Remove last two moves (current player and opponent)
        if len(self.game.move_history) >= 1:
            self.game.move_history.pop()
            # Reset game_over status if it was set
            if self.game.game_over:
                self.game.game_over = False
                self.game.winner = None

        self.draw_board()
        self.update_ui()
        self.status_label.config(text="↶ Move undone!", fg=self.SUCCESS_COLOR)
        self.root.after(1500, self._update_status)

    def reset_game(self):
        """Reset the game"""
        self.game.reset()
        self.draw_board()
        self.update_ui()
        self.status_label.config(text="🔄 Game reset! Click to start playing.", fg=self.TEXT_COLOR)


def main():
    """Main function"""
    root = tk.Tk()
    gui = GomokuGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
