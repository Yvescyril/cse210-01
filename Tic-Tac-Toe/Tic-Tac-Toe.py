#Tic-Tac-Toe: Assignment Solution
# Author:Yves Cyril
from random import random
from tabnanny import check
from turtle import position
from unicodedata import name



board = [ "-","-","-",
        "-","-","-",
        "-","-","-", ]
def main():
    pass
    
currentPlayer = "x"
winner = None
gameRunning = True
# printing the board for the players to see
def printBoard(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
# take the player input
def playerInput(board):
    inp = int(input("Enter a number 1-9:"))
    if inp>=1 and inp<=9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("This square has already chosen")
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner= board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner == board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
def checkDiag(board):
    global winner 
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
def checkTie(board):
    if "-" not in board:
        printBoard(board)
        print("It is a tie")
        gameRunning = False

def checkWin():
    if checkDiag(board) or checkHorizontle(board) or checkRow(board):
        print(f"The winner is {winner}")
        print("Good game. Thanks for playing!")
    
# switch the players
def switchPlayer():
    global currentPlayer
    if currentPlayer == "x":
        currentPlayer = "o"
    else:
        currentPlayer = "x"
        
# compute
def compute(board):
    while currentPlayer == "o":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "o"
            switchPlayer()
#check for the win or tie
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer
    compute(board)
    checkTie(board)
if __name__=="__main__":
    main()
    