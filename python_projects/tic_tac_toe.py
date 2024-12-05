import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.turn = 'X'
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font=('Arial', 20), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def on_click(self, row, col):
        if not self.buttons[row][col]['text']:
            self.buttons[row][col]['text'] = self.turn
            if self.check_winner():
                messagebox.showinfo("Game Over", f"{self.turn} wins!")
                self.reset_game()
            elif all(self.buttons[i][j]['text'] for i in range(3) for j in range(3)):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.turn = 'O' if self.turn == 'X' else 'X'
                if self.turn == 'O':
                    self.ai_move()

    def ai_move(self):
        empty_buttons = [(i, j) for i in range(3) for j in range(3) if not self.buttons[i][j]['text']]
        if empty_buttons:
            row, col = random.choice(empty_buttons)
            self.buttons[row][col]['text'] = self.turn
            if self.check_winner():
                messagebox.showinfo("Game Over", f"{self.turn} wins!")
                self.reset_game()
            elif all(self.buttons[i][j]['text'] for i in range(3) for j in range(3)):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.turn = 'X'

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != "":
                return True
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != "":
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        return False

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ""
        self.turn = 'X'

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
