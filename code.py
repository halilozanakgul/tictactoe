import time

playerSymbol = [' ', 'X', 'O']

def printBoard(board):
    for i in range(3):
        for j in range(3):
            print(playerSymbol[board[i*3+j]], end = '')
            if j < 2:
                print('|', end = '')
            else:
                print('')
        if i < 2:
            print('-----')

board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]


def human():
    return ord(input()) - 49

turn = 1

players = ["", "human", "human"]

print(players[1], "X vs.", players[2], "O")

winner = 0

for i in range(9):
    print("Turn of", players[turn], playerSymbol[turn])
    printBoard(board)
    time.sleep(1)
    if players[turn] == "human":
        place = human()

    if board[place]:
        print("Cell is full!")
        continue

    board[place] = turn

    if (board[place%3] == board[place%3 + 3] and board[place%3] == board[place%3 + 6]) or\
       (board[int(place/3)*3] == board[int(place/3)*3 + 1] and board[int(place/3)*3] == board[int(place/3)*3 + 2]) or\
       ((place == 0 or place == 4 or place == 8) and board[0] == board[4] and board[0] == board[8]) or\
       ((place == 2 or place == 4 or place == 6) and board[2] == board[4] and board[2] == board[6]):
       winner = turn
       break

    turn = 3-turn

if winner == 0:
    print("Tie")
else:
    printBoard(board)
    print(players[winner], playerSymbol[turn], "won")
