import time
from timeit import default_timer as timer
import random

playerSymbol = ['X', 'O', ' ']

class Game:

    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.board = [2, 2, 2,
                      2, 2, 2,
                      2, 2, 2]
        self.turn = 0
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
            startTime = timer()
            place = self.players[self.turn].play(self.board)
            print("Time =", timer()-startTime)
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
        self.printBoard()
        if self.winner == 2:
            print("Tie")
        else:
            print(self.players[self.winner], playerSymbol[self.winner], "won")

class Human:
    def __str__(self):
        return "Human"
    def play(self, board):
        return ord(input()) - 49
class Minimax:
    def __str__(self):
        return "Minimax"
    def printBoard(self, board):
        for i in range(3):
            for j in range(3):
                print(playerSymbol[board[i*3+j]], end = '')
                if j < 2:
                    print('|', end = '')
                else:
                    print('')
            if i < 2:
                print('-----')
    def isEnd(self, board):
        for i in range(3):
            if board[i*3] == board[i*3+1] and board[i*3] == board[i*3+2] and board[i*3] != 2:
                return board[i*3]
            if board[i] == board[i+3] and board[i] == board[i+6] and board[i] != 2:
                return board[i]
            if ((board[4] == board[0] and board[4] == board[8]) or (board[4] == board[2] and board[4] == board[6])) and board[4] != 2:
                return board[4]
        for i in range(9):
            if board[i] == 2:
                return -1
        return 2
    def minimize(self, board):
        end = self.isEnd(board)
        if end == 1:
            return -1
        if end == 0:
            return 1
        if end == 2:
            return 0
        mn = 2
        for i in range(9):
            if board[i] == 2:
                board[i] = 1
                mn = min(self.maximize(board), mn)
                board[i] = 2
                if mn == -1:
                    return -1
        return mn

    def maximize(self, board):
        end = self.isEnd(board)
        if end == 0:
            return 1
        if end == 1:
            return -1
        if end == 2:
            return 0
        mx = -2
        for i in range(9):
            if board[i] == 2:
                board[i] = 0
                mx = max(self.minimize(board), mx)
                board[i] = 2
                if mx == 1:
                    return 1
        return mx
    def play(self, board):
        mx = -2
        for i in range(9):
            if board[i] == 2:
                board[i] = 0
                t=self.minimize(board)
                if t == mx and random.random()>0.5:
                    mxi = i
                if t > mx:
                    mx = t
                    mxi = i
                board[i] = 2
        return mxi

Game(Minimax(), Minimax()).play()
