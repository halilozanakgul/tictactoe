import time

playerSymbol = ['X', 'O', ' ']

class Game:

    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.board = [2, 2, 2,
                      2, 2, 2,
                      2, 2, 2]
        self.turn = 1
        self.winner = 2
    def printBoard(self):
        for i in range(3):
            for j in range(3):
                print(playerSymbol[self.board[i*3+j]], end = '')
                if j < 2:
                    print('|', end = '')
                else:
                    print('')
            if i < 2:
                print('-----')

    def boardInvert(self):
        for i in range(9):
            if self.board[i] != 2:
                self.board[i] = 1 - self.board[i]

    def play(self):

        print(self.players[0], "X vs.", self.players[1], "O")

        for i in range(9):
            print("Turn of", self.players[self.turn], playerSymbol[self.turn])
            self.printBoard()
            time.sleep(1)
            if self.turn == 1:
                self.boardInvert()
            place = self.players[self.turn].play(self.board)
            if self.turn == 1:
                self.boardInvert()

            if self.board[place] != 2:
                print("Cell is full!")
                continue

            self.board[place] = self.turn

            if (self.board[place%3] == self.board[place%3 + 3] and self.board[place%3] == self.board[place%3 + 6]) or\
               (self.board[int(place/3)*3] == self.board[int(place/3)*3 + 1] and self.board[int(place/3)*3] == self.board[int(place/3)*3 + 2]) or\
               ((place == 0 or place == 4 or place == 8) and self.board[0] == self.board[4] and self.board[0] == self.board[8]) or\
               ((place == 2 or place == 4 or place == 6) and self.board[2] == self.board[4] and self.board[2] == self.board[6]):
               self.winner = self.turn
               break

            self.turn = 1-self.turn

        self.printResult()

    def printResult(self):
        if self.winner == 2:
            print("Tie")
        else:
            self.printBoard()
            print(self.players[self.winner], playerSymbol[self.winner], "won")


class Human:
    def __str__(self):
        return "Human"
    def play(self, board):
        return ord(input()) - 49

class Minimax:
    def __str__(self):
        return "Minimax"
    def play(self, board):
        return 1

game = Game(Human(), Minimax())
game.play()
