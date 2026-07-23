import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.resizable(False, False)

        self.current_player = "X"
        self.board = ["" for _ in range(9)]
        self.buttons = []

        self.status_var = tk.StringVar(value=f"Turn: {self.current_player}")

        title_label = tk.Label(
            root,
            text="Tic-Tac-Toe",
            font=("Arial", 20, "bold"),
            pady=10,
        )
        title_label.pack()

        status_label = tk.Label(
            root,
            textvariable=self.status_var,
            font=("Arial", 12),
            pady=5,
        )
        status_label.pack()

        board_frame = tk.Frame(root)
        board_frame.pack(pady=10)

        for row in range(3):
            for col in range(3):
                index = row * 3 + col
                button = tk.Button(
                    board_frame,
                    text="",
                    width=8,
                    height=3,
                    font=("Arial", 18, "bold"),
                    command=lambda i=index: self.on_click(i),
                )
                button.grid(row=row, column=col, padx=5, pady=5)
                self.buttons.append(button)

        reset_button = tk.Button(
            root,
            text="Reset Game",
            font=("Arial", 12),
            command=self.reset_game,
        )
        reset_button.pack(pady=10)

    def on_click(self, index):
        if self.board[index] != "":
            return

        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player)
        self.buttons[index].config(state="disabled")

        if self.check_winner(self.current_player):
            self.status_var.set(f"Player {self.current_player} wins!")
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            self.disable_all_buttons()
            return

        if self.is_board_full():
            self.status_var.set("It's a draw!")
            messagebox.showinfo("Game Over", "It's a draw!")
            self.disable_all_buttons()
            return

        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_var.set(f"Turn: {self.current_player}")

    def check_winner(self, player):
        winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == player and self.board[combo[1]] == player and self.board[combo[2]] == player:
                return True
        return False

    def is_board_full(self):
        return "" not in self.board

    def disable_all_buttons(self):
        for button in self.buttons:
            button.config(state="disabled")

    def reset_game(self):
        self.current_player = "X"
        self.board = ["" for _ in range(9)]
        self.status_var.set(f"Turn: {self.current_player}")
        for button in self.buttons:
            button.config(text="", state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()
