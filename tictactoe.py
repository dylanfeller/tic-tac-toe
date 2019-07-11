import pygame, sys, os
from array import *
pygame.init()

X = 1680
Y = 1050

s1 = (400, 100)
s2 = (720, 100)
s3 = (1040, 100)
s4 = (400, 420)
s5 = (720, 420)
s6 = (1040, 420)
s7 = (400, 740)
s8 = (720, 740)
s9 = (1040, 740)

screen = pygame.display.set_mode((X,Y), pygame.FULLSCREEN)
pygame.display.set_caption('Tic-Tac-Toe')
board = pygame.image.load('board.jpg')
x = pygame.image.load('x.png')
o = pygame.image.load('o.png')
xwin = pygame.image.load('xwin.jpg')
owin = pygame.image.load('owin.jpg')
draw = pygame.image.load('draw.jpg')

gameBoard = [[0,0,0],[0,0,0],[0,0,0]]

def checkWin():
    isDraw = 1
    if gameBoard[0][0] == 1 and gameBoard[0][1] == 1 and gameBoard[0][2] == 1:
        return 'x'
    if gameBoard[1][0] == 1 and gameBoard[1][1] == 1 and gameBoard[1][2] == 1:
        return 'x'
    if gameBoard[2][0] == 1 and gameBoard[2][1] == 1 and gameBoard[2][2] == 1:
        return 'x'
    if gameBoard[0][0] == 1 and gameBoard[1][0] == 1 and gameBoard[2][0] == 1:
        return 'x'
    if gameBoard[0][1] == 1 and gameBoard[1][1] == 1 and gameBoard[2][1] == 1:
        return 'x'
    if gameBoard[0][2] == 1 and gameBoard[1][2] == 1 and gameBoard[2][2] == 1:
        return 'x'
    if gameBoard[0][0] == 1 and gameBoard[1][1] == 1 and gameBoard[2][2] == 1:
        return 'x'
    if gameBoard[0][2] == 1 and gameBoard[1][1] == 1 and gameBoard[2][0] == 1:
        return 'x'

    if gameBoard[0][0] == 2 and gameBoard[0][1] == 2 and gameBoard[0][2] == 2:
        return 'o'
    if gameBoard[1][0] == 2 and gameBoard[1][1] == 2 and gameBoard[1][2] == 2:
        return 'o'
    if gameBoard[2][0] == 2 and gameBoard[2][1] == 2 and gameBoard[2][2] == 2:
        return 'o'
    if gameBoard[0][0] == 2 and gameBoard[1][0] == 2 and gameBoard[2][0] == 2:
        return 'o'
    if gameBoard[0][1] == 2 and gameBoard[1][1] == 2 and gameBoard[2][1] == 2:
        return 'o'
    if gameBoard[0][2] == 2 and gameBoard[1][2] == 2 and gameBoard[2][2] == 2:
        return 'o'
    if gameBoard[0][0] == 2 and gameBoard[1][1] == 2 and gameBoard[2][2] == 2:
        return 'o'
    if gameBoard[0][2] == 2 and gameBoard[1][1] == 2 and gameBoard[2][0] == 2:
        return 'o'
    
    a = 0
    while a<3:
        b = 0
        while b<3:
            if gameBoard[a][b] == 0:
                isDraw = 0
            b+=1    
        a+=1
                
    if isDraw == 1:
        return 'd'
    return 'n'

def drawBoard():
    screen.fill((255,255,255))
    screen.blit(board, (0,0))
    if gameBoard[0][0] == 1:
        screen.blit(x, s1)
    if gameBoard[0][0] == 2:
        screen.blit(o, s1)
    if gameBoard[0][1] == 1:
        screen.blit(x, s2)
    if gameBoard[0][1] == 2:
        screen.blit(o, s2)
    if gameBoard[0][2] == 1:
        screen.blit(x, s3)
    if gameBoard[0][2] == 2:
        screen.blit(o, s3)
    if gameBoard[1][0] == 1:
        screen.blit(x, s4)
    if gameBoard[1][0] == 2:
        screen.blit(o, s4)
    if gameBoard[1][1] == 1:
        screen.blit(x, s5)
    if gameBoard[1][1] == 2:
        screen.blit(o, s5)
    if gameBoard[1][2] == 1:
        screen.blit(x, s6)
    if gameBoard[1][2] == 2:
        screen.blit(o, s6)
    if gameBoard[2][0] == 1:
        screen.blit(x, s7)
    if gameBoard[2][0] == 2:
        screen.blit(o, s7)
    if gameBoard[2][1] == 1:
        screen.blit(x, s8)
    if gameBoard[2][1] == 2:
        screen.blit(o, s8)
    if gameBoard[2][2] == 1:
        screen.blit(x, s9)
    if gameBoard[2][2] == 2:
        screen.blit(o, s9)  

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

while True:
    player1turn = True
    drawBoard()
    while player1turn:
        drawBoard()
        for event in pygame.event.get():
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_ESCAPE:                
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    restart_program()
            if event.type == pygame.MOUSEBUTTONUP :
                pos = pygame.mouse.get_pos()
                if pos[0]>350 and pos[0]<666 and pos[1]>50 and pos[1]<365:
                    if gameBoard[0][0] == 0:
                        gameBoard[0][0] = 1
                        player1turn=False
                if pos[0]>666 and pos[0]<985 and pos[1]>50 and pos[1]<365:
                    if gameBoard[0][1] == 0:
                        gameBoard[0][1] = 1
                        player1turn=False
                if pos[0]>985 and pos[0]<1300 and pos[1]>50 and pos[1]<365:
                    if gameBoard[0][2] == 0:
                        gameBoard[0][2] = 1
                        player1turn=False
                if pos[0]>350 and pos[0]<666 and pos[1]>365 and pos[1]<690:
                    if gameBoard[1][0] == 0:
                        gameBoard[1][0] = 1
                        player1turn=False
                if pos[0]>666 and pos[0]<985 and pos[1]>365 and pos[1]<690:
                    if gameBoard[1][1] == 0:
                        gameBoard[1][1] = 1
                        player1turn=False
                if pos[0]>985 and pos[0]<1300 and pos[1]>365 and pos[1]<690:
                    if gameBoard[1][2] == 0:
                        gameBoard[1][2] = 1
                        player1turn=False
                if pos[0]>350 and pos[0]<666 and pos[1]>690 and pos[1]<1010:
                    if gameBoard[2][0] == 0:
                        gameBoard[2][0] = 1
                        player1turn=False
                if pos[0]>666 and pos[0]<985 and pos[1]>690 and pos[1]<1010:
                    if gameBoard[2][1] == 0:
                        gameBoard[2][1] = 1
                        player1turn=False
                if pos[0]>985 and pos[0]<1300 and pos[1]>690 and pos[1]<1010:
                    if gameBoard[2][2] == 0:
                        gameBoard[2][2] = 1
                        player1turn=False
        if checkWin() == 'x':
            screen.blit(xwin, (0,0))
        if checkWin() == 'o':
            screen.blit(owin, (0,0))
        if checkWin() == 'd':
            screen.blit(draw, (0,0))
        pygame.display.update()

    while not player1turn:
        drawBoard()
        for event in pygame.event.get():
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_ESCAPE:                
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    restart_program()
            if event.type == pygame.MOUSEBUTTONUP :
                pos = pygame.mouse.get_pos()
                if pos[0]>350 and pos[0]<666 and pos[1]>50 and pos[1]<365:
                    if gameBoard[0][0] == 0:
                        gameBoard[0][0] = 2
                        player1turn=True
                if pos[0]>666 and pos[0]<985 and pos[1]>50 and pos[1]<365:
                    if gameBoard[0][1] == 0:
                        gameBoard[0][1] = 2
                        player1turn=True
                if pos[0]>985 and pos[0]<1300 and pos[1]>50 and pos[1]<365:
                    if gameBoard[0][2] == 0:
                        gameBoard[0][2] = 2
                        player1turn=True
                if pos[0]>350 and pos[0]<666 and pos[1]>365 and pos[1]<690:
                    if gameBoard[1][0] == 0:
                        gameBoard[1][0] = 2
                        player1turn=True
                if pos[0]>666 and pos[0]<985 and pos[1]>365 and pos[1]<690:
                    if gameBoard[1][1] == 0:
                        gameBoard[1][1] = 2
                        player1turn=True
                if pos[0]>985 and pos[0]<1300 and pos[1]>365 and pos[1]<690:
                    if gameBoard[1][2] == 0:
                        gameBoard[1][2] = 2
                        player1turn=True
                if pos[0]>350 and pos[0]<666 and pos[1]>690 and pos[1]<1010:
                    if gameBoard[2][0] == 0:
                        gameBoard[2][0] = 2
                        player1turn=True
                if pos[0]>666 and pos[0]<985 and pos[1]>690 and pos[1]<1010:
                    if gameBoard[2][1] == 0:
                        gameBoard[2][1] = 2
                        player1turn=True
                if pos[0]>985 and pos[0]<1300 and pos[1]>690 and pos[1]<1010:
                    if gameBoard[2][2] == 0:
                        gameBoard[2][2] = 2
                        player1turn=True
        if checkWin() == 'o':
            screen.blit(owin, (0,0))
        if checkWin() == 'x':
            screen.blit(xwin, (0,0))
        if checkWin() == 'd':
            screen.blit(draw, (0,0))
        pygame.display.update()