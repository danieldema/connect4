import numpy as np
import pygame
import sys
import math
import pyautogui


def create_board():
    board = np.zeros([6, 7])
    return board

def next_row(column: int):
    for i in range(6):
        if board[5-i][column] == 0:
            return int(5-i)
    return -1

running = True

player1 = pyautogui.prompt(text = 'Player 1, please enter your name:')

player2 = pyautogui.prompt(text = 'Player 2, please enter your name:')

board = create_board()

turn = 0

pygame.init()

screen = pygame.display.set_mode((700, 800))
pygame.display.set_caption('Connect Four')
icon = pygame.image.load('connect_4_pic.jpg')
pygame.display.set_icon(icon)
myfont = pygame.font.SysFont("monospace", 75)

for column in range(7):
    for row in range(6):
        pygame.draw.rect(screen, (24, 66, 180), (column*100, (row+1)*100, 100, 100))
        pygame.draw.circle(screen, (0,0,0), (column*100 + 50, (row+1)*100 + 50), 45, 0)

pygame.display.update()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if not np.isin(0, board):
            pyautogui.alert(text = "Game over! Try again!")
            running = False

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

                if board[0, move] == 0:
                    board[next_row(move), move] = 1
                    pygame.draw.circle(screen, (255,0,0), (move*100 + 50, (int(next_row(move)+2)*100) + 50), 45, 0)
                    pygame.display.update()

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
                        pyautogui.alert(text = "Congratulations {}!".format(player1), title = "{} wins!".format(player1))
                        running = False
                    
                    turn = 1
                    print(board)

                if board[0, move] != 0 and turn == 0:
                    pyautogui.alert("This column is full! Choose a different column!")
    
            else:

                move = int(math.floor(event.pos[0]/100))


                if board[0, move] == 0:
                    board[next_row(move), move] = 2
                    pygame.draw.circle(screen, (255,255,0), (move*100 + 50, (int(next_row(move)+2)*100) + 50), 45, 0)
                    pygame.display.update()

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
                        pyautogui.alert(text = "Congratulations {}!".format(player2), title = "{} wins!".format(player2))
                        running = False

                    turn = 0
                    print(board)

                if board[0, move] != 0 and turn == 1:
                    pyautogui.alert("This column is full! Choose a different column!")