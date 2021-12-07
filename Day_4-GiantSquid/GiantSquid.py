import sys

def printBoards(boards):
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            print(boards[i][j])
        print()

def checkRow(row):
    for col in range(len(row)):
        if row[col][1] == False:
            return False
    return True

def checkCol(col, board):
    for row in range(len(board)):
        if board[row][col][1] == False:
            return False
    return True

def checkGameWin(boards):
    for n in range(len(boards)):
        if checkBoardWin(boards[n]):
            return True
    return False

def checkBoardWin(board):
    for row in range(len(board)):
        if checkRow(board[row]) == True:
            return True
    for col in range(len(board[0])):
        if board[0][col][1] == True:
            if checkCol(col, board) == True:
                return True
    return False

def sumUnmarked(board):
    sum = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col][1] == False:
                sum += board[row][col][0]
    return sum

lines = sys.stdin.readlines()
for i in range(len(lines)-1):
    lines[i] = lines[i][:-1]

# Part 1
print("Part 1:")

# setup turns
turns = [int(x) for x in lines[0].split(',')]

numBoards = 1
for i in range(2, len(lines)):
    if lines[i] == '':
        numBoards += 1

# 5x5 boards, hard coded size
boards = [[[(0, False) for i in range(5)] for j in range(5)] for n in range(numBoards)]

numBoards = 0
numLines = 0
for i in range(2, len(lines)):
    if lines[i] == '':
        numBoards += 1
        numLines = 0
    else:
        boards[numBoards][numLines] = [(int(x), False) for x in lines[i].split()]
        numLines += 1

win = False
for turn in turns:
    for n in range(len(boards)):
        for row in range(len(boards[n])):
            for col in range(len(boards[n][row])):
                if boards[n][row][col][0] == turn and not win:
                    boards[n][row][col] = (boards[n][row][col][0], True)
                    if checkGameWin(boards):
                        win = True
                        sum = sumUnmarked(boards[n])
                        print(turn*sum)

# printBoards(boards)

# Part 2
print("Part 2:")

for n in range(len(boards)):
    for row in range(len(boards[n])):
        for col in range(len(boards[n][row])):
            boards[n][row][col] = (boards[n][row][col][0], False)

countWins = 0
winningBoards = set()
for turn in turns:
    for n in range(len(boards)):
        for row in range(len(boards[n])):
            for col in range(len(boards[n][row])):
                if boards[n][row][col][0] == turn and n not in winningBoards:
                    boards[n][row][col] = (boards[n][row][col][0], True)
    for n in range(len(boards)):
        if checkBoardWin(boards[n]):
            winningBoards.add(n)
            if len(winningBoards) == len(boards):
                print(sumUnmarked(boards[n])*turn)
                exit(1)