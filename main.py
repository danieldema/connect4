import numpy as np
import pygame
import sys
import math

def create_board():
    board = np.zeros([6, 7])
    return board

def next_row(column: int):
    for i in range(6):
        if board[5-i][column] == 0:
            return int(5-i)
    return -1

running = True

print("Player 1, please enter your name:")
player1 = input()
print("Hello {}!".format(player1))

print("Player 2, please enter your name:")
player2 = input()
print("Hello {}!".format(player2))

board = create_board()

turn = 0

pygame.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption('Connect Four')
icon = pygame.image.load('connect_4_pic.jpg')
pygame.display.set_icon(icon)

for column in range(7):
    for row in range(6):
        pygame.draw.rect(screen, (24, 66, 180), (column*100, (row+1)*100, 100, 100))
        pygame.draw.circle(screen, (0,0,0), (column*100 + 50, (row+1)*100 + 50), 45, 0)

pygame.display.update()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if not np.isin(0 , board):
            print("Game over! Try again!")
            break

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, (0,0,0), (0,0, 700, 100))
            if turn == 0:
                pygame.draw.circle(screen, (255,0,0), (event.pos[0], 50), 45, 0)
            else:
                pygame.draw.circle(screen, (255,255,0), (event.pos[0], 50), 45, 0)
        pygame.display.update()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
        
            if turn == 0:

                move = int(math.floor(event.pos[0])/100)

                while board[0, move] != 0:
                    move = int(input("This column is full! Choose a different column."))
                
                board[next_row(move), move] = 1
                pygame.draw.circle(screen, (255,0,0), (move*100 + 50, (int(next_row(move)+2)*100) + 50), 45, 0)
                pygame.display.update()

                print(move)
                print(next_row(move))
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
    
            else:

                move = int(math.floor(event.pos[0]/100))

                while move not in range(7):
                    move = int(input("Your move needs to be a number between 0 and 6."))

                while board[0, move] != 0:
                    move = int(input("This column is full! Choose a different column."))
        
                board[next_row(move), move] = 2
                pygame.draw.circle(screen, (255,255,0), (move*100 + 50, int((next_row(move)+2)*100) + 50), 45, 0)
                pygame.display.update()


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