import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Tic Tac Toe')
        self.setGeometry(100, 100, 300, 300)

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.buttons = {}
        self.turn = 'X'

        for i in range(3):
            for j in range(3):
                button = QPushButton('')
                button.setFixedSize(100, 100)
                button.clicked.connect(lambda _, x=i, y=j: self.on_click(x, y))
                self.grid.addWidget(button, i, j)
                self.buttons[(i, j)] = button

        self.show()

    def on_click(self, x, y):
        if self.buttons[(x, y)].text() == '':
            self.buttons[(x, y)].setText(self.turn)
            if self.check_winner():
                QMessageBox.information(self, 'Game Over', f'{self.turn} wins!')
                self.reset_game()
            elif all(button.text() != '' for button in self.buttons.values()):
                QMessageBox.information(self, 'Game Over', 'Draw!')
                self.reset_game()
            else:
                self.turn = 'O' if self.turn == 'X' else 'X'

    def check_winner(self):
        for i in range(3):
            if self.buttons[(i, 0)].text() == self.buttons[(i, 1)].text() == self.buttons[(i, 2)].text() != '':
                return True
            if self.buttons[(0, i)].text() == self.buttons[(1, i)].text() == self.buttons[(2, i)].text() != '':
                return True
        if self.buttons[(0, 0)].text() == self.buttons[(1, 1)].text() == self.buttons[(2, 2)].text() != '':
            return True
        if self.buttons[(0, 2)].text() == self.buttons[(1, 1)].text() == self.buttons[(2, 0)].text() != '':
            return True
        return False

    def reset_game(self):
        for button in self.buttons.values():
            button.setText('')
        self.turn = 'X'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = TicTacToe()
    sys.exit(app.exec_())
