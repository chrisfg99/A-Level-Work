import random

def inputPlayerLetter():
    letter = ''
    while not (letter == 'A' or letter == 'B'):
        print('Do you want to be A Or B?')
        letter = input().upper()
    if letter == 'A':
        return ['A', 'A']
    else:
        return ['B', 'A']

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def drawBoard(board):
    linebreak = 0
    while linebreak <50:
        print('\n')
        linebreak = linebreak+1
    print('\t''   |   |')
    print('\t'' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('\t''   |   |')
    print('\t''-----------')
    print('\t''   |   |')
    print('\t'' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('\t''   |   |')
    print('\t''-----------')
    print('\t''   |   |')
    print('\t'' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('\t''   |   |')
    print('\n')
    print('\n')
   

def makeMove(board, letter, move):
    board[move] = str(letter)

def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[8] == le and bo[5] == le and bo[2] == le) or 
    (bo[9] == le and bo[6] == le and bo[3] == le) or 
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le)) 

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = int(input())
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    if isSpaceFree(board, 5):
        return 5
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True
print('Welcome to Noughts and Crosses - its time to play...')

while True:
    theBoard=[' ']*10
    playerLetter, computeLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The '+turn+' will go first.')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn=='player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard,playerLetter, move)
            if isWinner(theBoard,playerLetter):
                drawBoard(theBoard)
                print('Hooray!You have won the game!')
                gameISPlaying=False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn='computer'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You Lose.')
                gameIsPlaying=False
            else:
                if ifIsBoardfull(theBoard):
                    drawBoard(theBoard)
                    print('The gameis a tie!')
                    break
                else:
                    turn='player'
    if not playAgain():
        break
