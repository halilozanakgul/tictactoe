import random
import operator

def where(player, id, board):
    cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    if id == 3:
        for i in range(9):
            if board[i]!=1:
                board[i] = 5 - board[i]
    for i in range(9):
        for j in range(8-i):
            cnt[  ord(player[int( (36- (8-i)*(9-i)/2 + j)*9 + (board[i] - 1)*3 + board[i+j+1]-1 )]) - 48 ] += 1
    mx = 0
    mxi = 0
    for i in range(9):
        if board[i] == 1 and cnt[i] > mx:
            mx = cnt[i]
            mxi = i

    if id == 3:
        for i in range(9):
            if board[i]!=1:
                board[i] = 5 - board[i]
    return mxi

def printBoard(board):
    for i in range(3):
        for j in range(3):
            if board[i*3+j] == 1:
                print(' ', end = '')
            if board[i*3+j] == 2:
                print('X', end = '')
            if board[i*3+j] == 3:
                print('O', end = '')
            if j < 2:
                print('|', end = '')
            else:
                print('')
        if i < 2:
            print("-----")

def play(players):
    board = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    turn = 0
    winner = 1
    for i in range(9):
        place = where(players[turn], turn+2, board)
        board[place] = turn + 2
        if(board[int(place / 3)*3] == board[int(place / 3)*3 + 1] and board[int(place / 3)*3] == board[int(place / 3)*3 + 2]):
            winner = board[int(place / 3)*3]
            break
        if(board[place%3] == board[ 3+ place%3] and board[place%3] == board[6 + place%3]):
            winner = board[place%3]
            break
        if((place == 0 or place==4 or place==8 ) and (board[0] == board[4] and board[0] == board[8])):
            winner = board[0]
            break
        if((place == 2 or place==4 or place==6 ) and (board[2] == board[4] and board[2] == board[6])):
            winner = board[2]
            break
        turn = 1-turn
    return winner

def generatePlayer():
    player = ""
    for i in range(324):
        player += chr(48 + int(random.random()*9))
    return player

def fitness (str):
    result = 0
    for i in range(int(len(population)/4)):
        if play([str, population[int(random.random()*len(population))]]) == 2:
            result += 1
    return result

population = []

for i in range(100):
    population.append(generatePlayer())

def selection():
    fits = {}
    for str in population:
        fits [str] = fitness(str)
    return sorted(fits.items(), key = operator.itemgetter(1), reverse = True)[:20]

def birth(parent1, parent2):
    child = ""
    for i in range(324):
        if(random.random()<0.02):
            child += chr(48+int(random.random()*9))
        elif(random.random()<0.5):
            child += parent1[i]
        else:
            child += parent2[i]
    return child

def breed():
    newGen = []
    random.shuffle(population)
    for i in range(int(len(population)/2)):
        for j in range(5):
            newGen.append(birth(population[i][0], population[-i][0]))
    return newGen
"""
for i in range(1000):
    population = selection()
    print(population)
    population = breed()
"""
board = [1, 1, 1, 1, 1, 1, 1, 1, 1]
turn = 0
ga = "343451362882624116634653735466345851535413021241053274380853126787010185772273447741573160485078754408500020478461454216875715464250555531036345264046470707637683728412021046863737404841405476060774464088172581656824407174672083564605420106862154567774254133348582856564682266745015222201707361806724827812883531861732028668"
"""selection()[0][0]"""
print(ga)
for i in range(9):
    if turn == 0:
        place = where(ga, 2, board)
    else:
        place = ord(input()) - 48
    board[place] = turn + 2
    printBoard(board)
    if(board[int(place / 3)*3] == board[int(place / 3)*3 + 1] and board[int(place / 3)*3] == board[int(place / 3)*3 + 2]):
        winner = board[int(place / 3)*3]
        break
    if(board[place%3] == board[ 3+ place%3] and board[place%3] == board[6 + place%3]):
        winner = board[place%3]
        break
    if((place == 0 or place==4 or place==8 ) and (board[0] == board[4] and board[0] == board[8])):
        winner = board[0]
        break
    if((place == 2 or place==4 or place==6 ) and (board[2] == board[4] and board[2] == board[6])):
        winner = board[2]
        break
    turn = 1-turn
