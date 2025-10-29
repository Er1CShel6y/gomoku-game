"""
Gomoku Game GUI
Tkinter-based graphical user interface for Gomoku game
"""

import tkinter as tk
from tkinter import messagebox
from gomoku_game import GomokuGame, Player


class GomokuGUI:
    """
    Gomoku Game with Tkinter GUI - Modern Design
    - Beautiful graphical 15x15 board
    - Mouse click to place pieces
    - Real-time win detection
    - Modern UI with better visuals
    """

    # Color scheme
    BG_COLOR = "#1a1a2e"           # Deep blue-black background
    HEADER_COLOR = "#16213e"       # Darker header
    ACCENT_COLOR = "#0f3460"       # Accent color
    TEXT_COLOR = "#eaeaea"         # Light text
    BOARD_COLOR = "#d4a574"        # Warm board color
    GRID_COLOR = "#8b7355"         # Grid lines
    BUTTON_COLOR = "#e94560"       # Modern red accent
    BUTTON_HOVER = "#ff6b7a"       # Lighter red on hover

    def __init__(self, root):
        """Initialize the GUI"""
        self.root = root
        self.root.title("Gomoku Game")

        # Game engine
        self.game = GomokuGame(board_size=15)
        self.cell_size = 50

        # 计算合适的窗口大小：棋盘大小 + UI 边距
        canvas_size = self.cell_size * self.game.board_size + 30  # 棋盘大小
        window_height = 80 + 20 + canvas_size + 60 + 30  # header + margin + canvas + status + padding
        self.root.geometry(f"{canvas_size + 30}x{window_height}")
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
        """Create header section with title"""
        self.header_frame = tk.Frame(self.main_frame, bg=self.HEADER_COLOR, height=80)
        self.header_frame.pack(fill=tk.X, pady=(0, 20))
        self.header_frame.pack_propagate(False)

        self.title_label = tk.Label(
            self.header_frame,
            text=" Gomoku ",
            font=("Arial", 28, "bold"),
            bg=self.HEADER_COLOR,
            fg=self.BUTTON_COLOR
        )
        self.title_label.pack(pady=15)

    def _create_info_frame(self):
        """Create info frame with player info and buttons"""
        self.info_frame = tk.Frame(self.main_frame, bg=self.ACCENT_COLOR)
        self.info_frame.pack(fill=tk.X, pady=(0, 20), padx=5)

        # Left info section
        left_info = tk.Frame(self.info_frame, bg=self.ACCENT_COLOR)
        left_info.pack(side=tk.LEFT, padx=15, pady=12)

        # Current player indicator
        self.player_label = tk.Label(
            left_info,
            text="Current Player ：Black",
            font=("Arial", 13, "bold"),
            bg=self.ACCENT_COLOR,
            fg="#000000"
        )
        self.player_label.pack(side=tk.LEFT, padx=15)

        # Move counter
        self.move_label = tk.Label(
            left_info,
            text="Move Counting ：0",
            font=("Arial", 13, "bold"),
            bg=self.ACCENT_COLOR,
            fg=self.TEXT_COLOR
        )
        self.move_label.pack(side=tk.LEFT, padx=15)

        # Right buttons section
        right_buttons = tk.Frame(self.info_frame, bg=self.ACCENT_COLOR)
        right_buttons.pack(side=tk.RIGHT, padx=15, pady=12)

        # Reset button
        self.reset_button = tk.Button(
            right_buttons,
            text="Restart",
            font=("Arial", 11, "bold"),
            command=self.reset_game,
            bg=self.BUTTON_COLOR,
            fg="white",
            padx=20,
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
        """Create status frame for messages"""
        self.status_frame = tk.Frame(self.main_frame, bg=self.ACCENT_COLOR, height=60)
        self.status_frame.pack(fill=tk.X, padx=5)
        self.status_frame.pack_propagate(False)

        # Status message
        self.status_label = tk.Label(
            self.status_frame,
            text="Click the board to place a stone",
            font=("Arial", 11),
            bg=self.ACCENT_COLOR,
            fg=self.TEXT_COLOR,
            wraplength=900,
            justify=tk.LEFT
        )
        self.status_label.pack(fill=tk.BOTH, padx=15, pady=8, side=tk.LEFT)

        # Last move indicator
        self.last_move_label = tk.Label(
            self.status_frame,
            text="",
            font=("Arial", 9),
            bg=self.ACCENT_COLOR,
            fg="#aaaaaa"
        )
        self.last_move_label.pack(fill=tk.BOTH, padx=15, pady=8, side=tk.RIGHT)

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
        """Draw a piece on the board with 3D effect"""
        x = 10 + col * self.cell_size
        y = 10 + row * self.cell_size
        radius = self.cell_size // 2 - 3

        if player_value == Player.BLACK.value:
            color = "#1a1a1a"
            outline = "#000000"
            shadow_color = "#333333"
            highlight_color = "#3a3a3a"
        else:  # WHITE
            color = "#f0f0f0"
            outline = "#999999"
            shadow_color = "#dddddd"
            highlight_color = "#ffffff"

        # Draw shadow
        self.canvas.create_oval(x - radius - 1, y - radius + 1, x + radius + 1, y + radius + 3,
                               fill=shadow_color, outline="")

        # Draw main piece
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius,
                               fill=color, outline=outline, width=2)

        # Draw highlight
        highlight_radius = radius // 3
        self.canvas.create_oval(x - highlight_radius // 2, y - highlight_radius // 2,
                               x + highlight_radius // 2, y + highlight_radius // 2,
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
            winner_name = "Black" if self.game.winner == Player.BLACK else "White"
            messagebox.showinfo(
                "Game Over!",
                f"Congratulations! {winner_name} wins!\n\nTotal moves: {len(self.game.move_history)}"
            )

    def on_canvas_motion(self, event):
        """Handle mouse motion on canvas"""
        pass

    def update_ui(self):
        """Update UI elements"""
        # Update current player label
        player_color = "Black" if self.game.current_player == Player.BLACK else "White"
        self.player_label.config(text=f"Current Player ：{player_color}")

        # Update move counter
        self.move_label.config(text=f"Move Counting ：{len(self.game.move_history)}")

        # Update last move
        if self.game.move_history:
            last_row, last_col = self.game.move_history[-1]
            self.last_move_label.config(
                text=f"Last move: Row {last_row + 1}, Col {last_col + 1}"
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

    def reset_game(self):
        """Reset the game"""
        self.game.reset()
        self.draw_board()
        self.update_ui()
        self.status_label.config(text="Game reset! Click to start playing.", fg=self.TEXT_COLOR)


def main():
    """Main function"""
    root = tk.Tk()
    gui = GomokuGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
