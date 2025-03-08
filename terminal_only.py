import numpy as np

def create_board():
    board = np.zeros([6, 7])
    return board

def next_row(column: int):
    for i in range(7):
        if board[5-i][column] == 0:
            return 5-i

running = True

print("Player 1, please enter your name:")
player1 = input()
print("Hello {}!".format(player1))

print("Player 2, please enter your name:")
player2 = input()
print("Hello {}!".format(player2))

board = create_board()

turn = 0


while running:
    
    if not np.isin(0 , board):
        print("Game over! Try again!")
        break

    if turn == 0:

        move = int(input("{}, choose your next move (0-6)!".format(player1)))

        while move not in range(7):
            move = int(input("Your move needs to be a number between 0 and 6."))
        
        while board[0, move] != 0:
            move = int(input("This column is full! Choose a different column."))
        
        board[next_row(move), move] = 1

        print(board)

        game_checker = False

        for column in range(0, 4):
            for row in range(6):
                if board[row][column] == 1 and board[row][column+1] == 1 and board[row][column+2] == 1 and board[row][column+3] == 1:
                    game_checker = True

        for row in range(0, 3):
            for column in range(7):
                if board[row][column] == 1 and board[row+1][column] == 1 and board[row+2][column] == 1 and board[row+3][column] == 1:
                    game_checker = True

        for column in range(4):
            for row in range(3, 6):
                if board[row][column] == 1 and board[row-1][column+1] == 1 and board[row-2][column+2] == 1 and board[row-3][column+3] == 1:
                    game_checker = True

        for column in range(3, 7):
            for row in range(3, 6):
                if board[row][column] == 1 and board[row-1][column-1] == 1 and board[row-2][column-2] == 1 and board[row-3][column-3] == 1:
                    game_checker = True

        if game_checker == True:
            print("Congratulations {}!".format(player1))
            break

        turn = 1
    
    if turn == 1:

        move = int(input("{}, choose your next move (0-6)!".format(player2)))

        while move not in range(7):
            move = int(input("Your move needs to be a number between 0 and 6."))

        while board[0, move] != 0:
            move = int(input("This column is full! Choose a different column."))
        
        board[next_row(move), move] = 2

        print(board)

        game_checker = False

        for column in range(0, 4):
            for row in range(6):
                if board[row][column] == 2 and board[row][column+1] == 2 and board[row][column+2] == 2 and board[row][column+3] == 2:
                    game_checker = True


        for row in range(0, 3):
            for column in range(7):
                if board[row][column] == 2 and board[row+1][column] == 2 and board[row+2][column] == 2 and board[row+3][column] == 2:
                    game_checker = True

        for column in range(4):
            for row in range(3, 6):
                if board[row][column] == 2 and board[row-1][column+1] == 2 and board[row-2][column+2] == 2 and board[row-3][column+3] == 2:
                    game_checker = True

        for column in range(3, 7):
            for row in range(3, 6):
                if board[row][column] == 2 and board[row-1][column-1] == 2 and board[row-2][column-2] == 2 and board[row-3][column-3] == 2:
                    game_checker = True    

        if game_checker == True:
            print("Congratulations {}!".format(player2))
            break

        turn = 0