import random

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

# printing the game board


def printBoard(board):
    print(board[0] + "|"+board[1] + "|" + board[2])
    print("------")
    print(board[3] + "|"+board[4] + "|" + board[5])
    print("------")
    print(board[6] + "|"+board[7] + "|" + board[8])



# take player input


def playerInput(board):
    inp = int(input("Entrez un nombre 1-9:"))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Le joueur se trouve déjà à cet endroit")


# check for win or tie
def check_Horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
    return True


def check_verticale(board):
    if board[0] == board[3] == board[6] and [0] != "-":
        winner = board = [0]
        return True
    elif board[1] == board[4] == board[7] and [1] != "-":
        winner = board = [1]
        return True
    elif board[2] == board[5] == board[8] and [2] != "-":
        winner = board = [2]
    return True


def check_diagonal(board):
    if board[0] == board[4] == board[8] and [0] != "-":
        winner = board = [0]
        return True
    elif board[2] == board[4] == board[6] and [2] != "-":
        winner = board = [2]
        return True


def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("C'est une egalité")
        gameRunning = False


def checkWin():
    if check_diagonal(board) or check_Horizontal(board) or check_verticale(board):
        print(f"-{winner}")
# switch the player


def switcPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# IA


def IA(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switcPlayer()


# check for win or tie again
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switcPlayer()
    IA(board)
    checkWin()
    checkTie(board)
