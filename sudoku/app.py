import pygame
from settings import *
import threading
import time
import sys
import numpy as np

sys.setrecursionlimit(1000)

threadLock = threading.RLock()
Matrix = [[-1 for x in range(21)] for y in range(21)]
M = [[-1 for x in range(21)] for y in range(21)]
for yidx, row in enumerate(board):
    for xidx, num in enumerate(row):
        if num == '*':
            Matrix[yidx][xidx] = 0
        else:
            if num == '1':
                Matrix[yidx][xidx] = 1
            if num == '2':
                Matrix[yidx][xidx] = 2
            if num == '3':
                Matrix[yidx][xidx] = 3
            if num == '4':
                Matrix[yidx][xidx] = 4
            if num == '5':
                Matrix[yidx][xidx] = 5
            if num == '6':
                Matrix[yidx][xidx] = 6
            if num == '7':
                Matrix[yidx][xidx] = 7
            if num == '8':
                Matrix[yidx][xidx] = 8
            if num == '9':
                Matrix[yidx][xidx] = 9
# up left sudoku


def findNextEmpty1():
    global Matrix
    
  
    for r in range(9):
     for c in range(9):
        if Matrix[r][c] == 0:
            return r, c
    return None, None
# up right sudoku


def findNextEmpty2():
    global Matrix
    for r in range(6):
        for c in range(9, 18):
            if Matrix[r][c] == 0:
                return r, c
    for r in range(6, 9):
        for c in range(12, 21):
            if Matrix[r][c] == 0:
                return r, c
    return None, None
# center sudoku


def findNextEmpty3():
    global Matrix
    for r in range(9, 12):
        for c in range(0,9):
            if Matrix[r][c] == 0:
                return r, c
    for r in range(6, 9):
        for c in range(6, 15):
            if Matrix[r][c] == 0:
                return r, c
    
    for r in range(12, 15):
        for c in range(6, 15):
            if Matrix[r][c] == 0:
                return r, c
    return None, None
# down left sudoku


def findNextEmpty4():
    global Matrix
    
    for r in range(12, 21):
        for c in range(9):
            if Matrix[r][c] == 0:
                return r, c
    return None, None
# down right sudoku


def findNextEmpty5():
    global Matrix
    for r in range(12, 15):
        for c in range(12, 21):
            if Matrix[r][c] == 0:
                return r, c
    for r in range(15, 21):
        for c in range(9, 18):
            if Matrix[r][c] == 0:
                return r, c
    return None, None


class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 800))
        self.running = True
        self.grid = board
        self.selected = None
        self.mousePos = None
        self.font = pygame.font.SysFont("arial", cellSize//2)

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()

        pygame.quit()
        SystemExit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected = self.mouseOnGrid()
                if selected:
                    print(self.mouseOnGrid())
                    self.selected = selected
                else:
                    print("not on board")
                    self.selected = None

    def update(self):
        self.mousePos = pygame.mouse.get_pos()

    def draw(self):
        self.window.fill(WHITE)
        if self.selected:
            self.drawSelection(self.window, self.selected)
        self.drawNumbers(self.window)
        self.drawNumbersMatrix(self.window)
        self.drawGrid(self.window)
        pygame.display.update()
    def drawNumbersMatrix(self,window):
         for yidx, row in enumerate(M):
            for xidx, num in enumerate(row):
                if yidx <= 8 and xidx <= 8:
                    if num !=( 0 or -1):
                        pos = [(xidx*cellSize)+gridPos[0],
                               (yidx*cellSize)+gridPos[1]]
                        self.textToScreenMatrix( self.window,str(num), pos)
                if xidx >= 9 and yidx >= 6 and yidx <= 8:
                    if num != (0 or -1):
                        pos = [(xidx*cellSize)+gridPos[0],
                               (yidx*cellSize)+gridPos[1]]
                        self.textToScreenMatrix(self.window, str(num), pos)
                if xidx >= 9 and xidx <= 11 and yidx >= 12 and yidx <= 14:
                    if num !=( 0 or -1):
                        pos = [(xidx*cellSize)+gridPos[0],
                               (yidx*cellSize)+gridPos[1]]
                        self.textToScreenMatrix(self.window,str(num), pos)
                if yidx >= 9 and yidx <= 11 and xidx <= 8:
                    if num != (0 or -1):
                        pos = [(xidx*cellSize)+gridPos[0]+180,
                               (yidx*cellSize)+gridPos[1]]
                        self.textToScreenMatrix(self.window, str(num), pos)
                if yidx <= 5 and xidx > 8:
                    if num != (0 or -1):
                        pos = [(xidx*cellSize)+gridPos[0]+90,
                               (yidx*cellSize)+gridPos[1]]
                        self.textToScreenMatrix( self.window,str(num), pos)
                if yidx >= 12 and yidx <= 14 and xidx > 11:
                    if num != (0 or -1):
                        pos = [(xidx*cellSize)+gridPos[0],
                               (yidx*cellSize)+gridPos[1]]
                        self.textToScreenMatrix(self.window,str(num), pos)
                if yidx > 14 and xidx > 8:
                    if num !=( 0 or -1):
                        pos= [(xidx*cellSize)+gridPos[0]+90,
                               (yidx*cellSize)+gridPos[1]]
                        self.textToScreenMatrix(self.window, str(num), pos)
                if yidx >= 12 and xidx <= 8:
                    if num !=( 0 or -1):
                        pos = [(xidx*cellSize)+gridPos[0],
                               (yidx*cellSize)+gridPos[1]]
                        self.textToScreenMatrix(self.window, str(num), pos)
    def drawNumbers(self, window):
        for yidx, row in enumerate(self.grid):
            for xidx, num in enumerate(row):
                if yidx <= 8 and xidx <= 8:
                    if num != "*":
                        pos = [(xidx*cellSize)+gridPos[0],
                               (yidx*cellSize)+gridPos[1]]
                        self.textToScreen(window, str(num), pos)
                if xidx >= 9 and yidx >= 6 and yidx <= 8:
                    if num != "*":
                        pos = [(xidx*cellSize)+gridPos[0],
                               (yidx*cellSize)+gridPos[1]]
                        self.textToScreen(window, str(num), pos)
                if xidx >= 9 and xidx <= 11 and yidx >= 12 and yidx <= 14:
                    if num != "*":
                        pos = [(xidx*cellSize)+gridPos[0],
                               (yidx*cellSize)+gridPos[1]]
                        self.textToScreen(window, str(num), pos)
                if yidx >= 9 and yidx <= 11 and xidx <= 8:
                    if num != "*":
                        pos = [(xidx*cellSize)+gridPos[0]+180,
                               (yidx*cellSize)+gridPos[1]]
                        self.textToScreen(window, str(num), pos)
                if yidx <= 5 and xidx > 8:
                    if num != "*":
                        pos = [(xidx*cellSize)+gridPos[0]+90,
                               (yidx*cellSize)+gridPos[1]]
                        self.textToScreen(window, str(num), pos)
                if yidx >= 12 and yidx <= 14 and xidx > 11:
                    if num != "*":
                        pos = [(xidx*cellSize)+gridPos[0],
                               (yidx*cellSize)+gridPos[1]]
                        self.textToScreen(window, str(num), pos)
                if yidx > 14 and xidx > 8:
                    if num != "*":
                        pos = [(xidx*cellSize)+gridPos[0]+90,
                               (yidx*cellSize)+gridPos[1]]
                        self.textToScreen(window, str(num), pos)
                if yidx >= 12 and xidx <= 8:
                    if num != "*":
                        pos = [(xidx*cellSize)+gridPos[0],
                               (yidx*cellSize)+gridPos[1]]
                        self.textToScreen(window, str(num), pos)

    def drawSelection(self, window, pos):
        pygame.draw.rect(window, LightBlue, ((
            pos[0]*cellSize)+gridPos[0], (pos[1]*cellSize)+gridPos[1], cellSize, cellSize))

    def drawGrid(self, window):
        pygame.draw.rect(window, Black, (gridPos[0], gridPos[1], 630, 630), 2)
        for x in range(10):
            pygame.draw.line(window, Black, (gridPos[0]+(x*cellSize), gridPos[1]), (gridPos[0]+(
                x*cellSize), gridPos[1]+270), 2 if x % 3 == 0 else 1)
            pygame.draw.line(window, Black, (gridPos[0], gridPos[1]+(
                x*cellSize)), (gridPos[0]+270, gridPos[1]+(x*cellSize)), 2 if x % 3 == 0 else 1)
        for x in range(12, 22):
            pygame.draw.line(window, Black, (gridPos[0]+(x*cellSize), gridPos[1]), (gridPos[0]+(
                x*cellSize), gridPos[1]+270), 2 if x % 3 == 0 else 1)
        for x in range(10):
            pygame.draw.line(window, Black, (gridPos[2], gridPos[1]+(
                x*cellSize)), (gridPos[2]+270, gridPos[1]+(x*cellSize)), 2 if x % 3 == 0 else 1)
        for x in range(10):
            pygame.draw.line(window, Black, (gridPos[0]+(x*cellSize), gridPos[3]), (gridPos[0]+(
                x*cellSize), gridPos[3]+270), 2 if x % 3 == 0 else 1)
            pygame.draw.line(window, Black, (gridPos[0], gridPos[3]+(
                x*cellSize)), (gridPos[0]+270, gridPos[3]+(x*cellSize)), 2 if x % 3 == 0 else 1)
        for x in range(12, 22):
            pygame.draw.line(window, Black, (gridPos[0]+(x*cellSize), gridPos[3]), (gridPos[0]+(
                x*cellSize), gridPos[3]+270), 2 if x % 3 == 0 else 1)
        for x in range(10):
            pygame.draw.line(window, Black, (gridPos[2], gridPos[3]+(
                x*cellSize)), (gridPos[2]+270, gridPos[3]+(x*cellSize)), 2 if x % 3 == 0 else 1)
        for x in range(6, 16):
            pygame.draw.line(window, Black, (gridPos[0]+(x*cellSize), gridPos[5]), (gridPos[0]+(
                x*cellSize), gridPos[5]+90), 2 if x % 3 == 0 else 1)
        for x in range(4):
            pygame.draw.line(window, Black, (gridPos[4], gridPos[5]+(
                x*cellSize)), (gridPos[4]+270, gridPos[5]+(x*cellSize)), 2 if x % 3 == 0 else 1)
        for x in range(9, 12):
            pygame.draw.line(window, Black, (gridPos[0]+(x*cellSize), gridPos[6]), (gridPos[0]+(
                x*cellSize), gridPos[6]+90), 2 if x % 3 == 0 else 1)
        for x in range(3):
            pygame.draw.line(window, Black, (gridPos[7], gridPos[6]+(
                x*cellSize)), (gridPos[7]+90, gridPos[6]+(x*cellSize)), 2 if x % 3 == 0 else 1)
        for x in range(9, 12):
            pygame.draw.line(window, Black, (gridPos[0]+(x*cellSize), gridPos[3]), (gridPos[0]+(
                x*cellSize), gridPos[3]+90), 2 if x % 3 == 0 else 1)
        for x in range(4):
            pygame.draw.line(window, Black, (gridPos[7], gridPos[3]+(
                x*cellSize)), (gridPos[7]+90, gridPos[3]+(x*cellSize)), 2 if x % 3 == 0 else 1)

    def mouseOnGrid(self):
        if self.mousePos[0] < gridPos[0] or self.mousePos[1] < gridPos[1]:
            return False
        if self.mousePos[0] > gridPos[0]+gridSize or self.mousePos[1] > gridPos[1]+gridSize:
            return False
        return((self.mousePos[0]-gridPos[0])//cellSize, (self.mousePos[1]-gridPos[1])//cellSize)

    def textToScreen(self, window, text, pos):
        font = self.font.render(text, False, Black)
        fontWidth = font.get_width()
        fontHeight = font.get_height()
        pos[0] += (cellSize-fontWidth)//2
        pos[1] += (cellSize-fontHeight)//2
        window.blit(font, pos)
    def textToScreenMatrix(self,window, text, pos):
        font = self.font.render(text, False, Red)
        fontWidth = font.get_width()
        fontHeight = font.get_height()
        pos[0] += (cellSize-fontWidth)//2
        pos[1] += (cellSize-fontHeight)//2
        window.blit(font, pos)

def checkNumberCenter(x, y, n):
    # upleft
    if(x > 5 and x < 9 and y > 5 and y < 9):
        for i in range(0, 15):
            # print(board[y][i])
            if Matrix[y][i] == n:
                return False

        for i in range(0, 9):
            # print(board[i][x])
            if Matrix[i][x] == n:
                return False
        if Matrix[9][x-6] == n:
            return False
        elif Matrix[10][x-6] == n:
            return False
        elif Matrix[11][x-6] == n:
            return False
        for i in range(12, 15):
            if Matrix[i][x] == n:
                return False
        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(0, 3):
            for j in range(0, 3):
                #  print(board[y0+i][x0+j])
                if Matrix[y0+i][x0+j] == n:
                    return False
        return True
    # upright
    if(x > 11 and x < 15 and y > 5 and y < 9):
        for i in range(6, 21):
            if Matrix[y][i] == n:
                return False

        for i in range(0, 6):
            if Matrix[i][x-3] == n:
                return False
        if Matrix[9][x-6] == n:
            return False
        elif Matrix[10][x-6] == n:
            return False
        elif Matrix[11][x-6] == n:
            return False
        for i in range(12, 15):
            if Matrix[i][x] == n:
                return False
        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(0, 3):
            for j in range(0, 3):
                #  print(board[y0+i][x0+j])
                if Matrix[y0+i][x0+j] == n:
                    return False
        return True
    # downright
    if (x > 11 and x < 15 and y < 15 and y > 11):
        for i in range(6, 21):
            if Matrix[y][i] == n:
                return False
        if Matrix[6][x] == n:
            return False
        elif Matrix[7][x] == n:
            return False
        elif Matrix[8][x] == n:
            return False
        for i in range(15, 21):
            if Matrix[i][x-3] == n:
                return False
        if Matrix[9][x-6] == n:
            return False
        elif Matrix[10][x-6] == n:
            return False
        elif Matrix[11][x-6] == n:
            return False
        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(0, 3):
            for j in range(0, 3):
             #  print(board[y0+i][x0+j])
                if Matrix[y0+i][x0+j] == n:
                    return False
        return True
 # downleft
    if(x < 9 and y > 11 and x > 5 and y < 15):
        for i in range(0, 15):
            # print(Matrix[y][i])
            if Matrix[y][i] == n:
                return False
        if Matrix[6][x] == n:
            return False
        elif Matrix[7][x] == n:
            return False
        elif Matrix[8][x] == n:
            return False
        for i in range(12, 21):
            # print(Matrix[i][x])
            if (Matrix[i][x]) == n:
                return False
        if Matrix[9][x-6] == n:
            return False
        elif Matrix[10][x-6] == n:
            return False
        elif Matrix[11][x-6] == n:
            return False

        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(0, 3):
            for j in range(0, 3):
                #  print(board[y0+i][x0+j])
                if Matrix[y0+i][x0+j] == n:
                    return False
        return True
    if(x > 8 and x < 12) and (y > 5 and y < 9):
        for i in range(6, 15):
            # print(Matrix[y][i])
            if Matrix[y][i] == n:
                return False

        for i in range(6, 9):
            # print(Matrix[i][x])
            if Matrix[i][x] == n:
                return False
        for i in range(9, 12):
            # print(Matrix[i][x])
            if Matrix[i][x-6] == n:
                return False
        for i in range(12, 15):
            # print(Matrix[i][x])
            if Matrix[i][x] == n:
                return False

        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(0, 3):
            for j in range(0, 3):
                #  print(board[y0+i][x0+j])
                if Matrix[y0+i][x0+j] == n:
                    return False
        return True
  # down-middle 3*3 square
    if(x > 8 and x < 12) and (y > 11 and y < 15):
        for i in range(6, 15):
            # print(Matrix[y][i])
            if Matrix[y][i] == n:
                return False

        for i in range(6, 9):
            # print(Matrix[i][x])
            if Matrix[i][x] == n:
                return False
        for i in range(9, 12):
            # print(Matrix[i][x])
            if Matrix[i][x-6] == n:
                return False
        for i in range(12, 15):
            # print(Matrix[i][x])
            if Matrix[i][x] == n:
                return False

        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(0, 3):
            for j in range(0, 3):
                if Matrix[y0+i][x0+j] == n:
                    return False
        return True
  # middle 6*3
    if(x < 9 and y > 8 and y < 12):
        for i in range(0, 9):
            # print(Matrix[y][i])
            if Matrix[y][i] == n:
                return False

        for i in range(6, 9):
            # print(Matrix[i][x])
            if Matrix[i][x+6] == n:
                return False
        for i in range(9, 12):
            # print(Matrix[i][x])
            if Matrix[i][x] == n:
                return False
        for i in range(12, 15):
            # print(Matrix[i][x])
            if Matrix[i][x+6] == n:
                return False

        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(0, 3):
            for j in range(0, 3):
                #  print(board[y0+i][x0+j])
                if Matrix[y0+i][x0+j] == n:
                    return False
        return True


def checkNumber(x, y, n):
    global Matrix
  # up-left sudoku
    if(x < 9 and y < 9):
        # joint square
        if (x > 5 and y > 5):
            for i in range(0, 15):
                # print(board[y][i])
                if Matrix[y][i] == n:
                    return False

            for i in range(0, 9):
                # print(board[i][x])
                if (Matrix[i][x] or Matrix[9][x-6] or Matrix[10][x-6] or Matrix[11][x-6] or Matrix[12][x] or Matrix[13][x] or Matrix[14][x]) == n:
                    return False

            x0 = (x//3)*3
            y0 = (y//3)*3
            for i in range(0, 3):
                for j in range(0, 3):
                    #  print(board[y0+i][x0+j])
                    if Matrix[y0+i][x0+j] == n:
                        return False
            return True
        else:
            for i in range(0, 9):
                # print(board[y][i])
                if Matrix[y][i] == n:
                    return False

            for i in range(0, 9):

                # print(board[i][x])
                if Matrix[i][x] == n:
                    return False

            x0 = (x//3)*3
            y0 = (y//3)*3

            for i in range(0, 3):
                for j in range(0, 3):
                    #  print(board[y0+i][x0+j])
                    if Matrix[y0+i][x0+j] == n:
                        return False
            return True
    # up-right sudoku
    if(x > 8 and y < 9):
        if (x > 11 and x < 15 and y > 5):
            for i in range(6, 21):

                if Matrix[y][i] == n:
                    return False

            for i in range(0, 6):
                if (Matrix[i][x-3] or Matrix[9][x-6] or Matrix[10][x-6] or Matrix[11][x-6] or Matrix[12][x] or Matrix[13][x] or Matrix[14][x]) == n:
                    return False

            x0 = (x//3)*3
            y0 = (y//3)*3
            for i in range(0, 3):
                for j in range(0, 3):
                    #  print(board[y0+i][x0+j])
                    if Matrix[y0+i][x0+j] == n:
                        return False
            return True
        # joint square
        elif (y > 5 and x > 14):
            for i in range(12, 21):
                if Matrix[y][i] == n:
                    return False
            for i in range(0, 6):
                if (Matrix[i][x-3] or Matrix[6][x] or Matrix[7][x] or Matrix[8][x]) == n:
                    return False

            x0 = (x//3)*3
            y0 = (y//3)*3

            for i in range(0, 3):
                for j in range(0, 3):
                    #  print(board[y0+i][x0+j])
                    if Matrix[y0+i][x0+j] == n:
                        return False
            return True
        else:

            for i in range(9, 18):
                if Matrix[y][i] == n:
                    return False
            for i in range(0, 6):
                if (Matrix[i][x] or Matrix[6][x+3] or Matrix[7][x+3] or Matrix[8][x+3]) == n:
                    return False
            x0 = (x//3)*3
            y0 = (y//3)*3
            for i in range(0, 3):
                for j in range(0, 3):
                    #  print(board[y0+i][x0+j])
                    if Matrix[y0+i][x0+j] == n:
                        return False
            return True
 # down-right sudoku

    if (x > 8 and y > 11):

        # joint square
        if (x > 11 and x < 15 and y < 15):
            for i in range(6, 21):
                if Matrix[y][i] == n:
                    return False

            for i in range(6, 21):
                if Matrix[i][x-3] == n:
                    return False

            x0 = (x//3)*3
            y0 = (y//3)*3
            for i in range(0, 3):
                for j in range(0, 3):
                 #  print(board[y0+i][x0+j])
                    if Matrix[y0+i][x0+j] == n:
                        return False
            return True
        elif x >= 15 and y < 15:
            for i in range(12, 21):
                if Matrix[y][i] == n:
                    return False

            for i in range(15, 21):
                if Matrix[i][x-3] == n:
                    return False

            x0 = (x//3)*3
            y0 = (y//3)*3
            for i in range(0, 3):
                for j in range(0, 3):
                    #  print(board[y0+i][x0+j])
                    if Matrix[y0+i][x0+j] == n:
                        return False
            return True
        else:
            for i in range(9, 18):
                # print(Matrix[y][i])
                if Matrix[y][i] == n:
                    return False

            for i in range(15, 21):
                if Matrix[i][x] == n:
                    return False
            if Matrix[12][x+3] == n:
                return False
            elif Matrix[13][x+3] == n:
                return False
            elif Matrix[14][x+3] == n:
                return False
            x0 = (x//3)*3
            y0 = (y//3)*3
            for i in range(0, 3):
                for j in range(0, 3):
                    #  print(board[y0+i][x0+j])
                    if Matrix[y0+i][x0+j] == n:
                        return False
            return True

 # down-left sudoku
    if(x < 9 and y > 11):
        # joint square
        if (x > 5 and y < 15):
            for i in range(0, 15):
                # print(Matrix[y][i])
                if Matrix[y][i] == n:
                    return False

            for i in range(12, 21):
                # print(Matrix[i][x])
                if (Matrix[i][x]) == n:
                    return False
            if (Matrix[9][x-6] or Matrix[10][x-6] or Matrix[11][x-6] or Matrix[6][x] or Matrix[7][x] or Matrix[8][x]) == n:
                return False

            x0 = (x//3)*3
            y0 = (y//3)*3
            for i in range(0, 3):
                for j in range(0, 3):
                    #  print(board[y0+i][x0+j])
                    if Matrix[y0+i][x0+j] == n:
                        return False
            return True
        else:
            for i in range(0, 9):
                # print(Matrix[y][i])
                if Matrix[y][i] == n:
                    return False

            for i in range(12, 21):
                # print(Matrix[i][x])
                if Matrix[i][x] == n:
                    return False

            x0 = (x//3)*3
            y0 = (y//3)*3

            for i in range(0, 3):
                for j in range(0, 3):
                    #  print(board[y0+i][x0+j])
                    if Matrix[y0+i][x0+j] == n:
                        return False
            return True
    #print(checkNumber(8, 10, str(8)))

# up left sudoku
def write(result):
 res=np.matrix(result)
 with open("C:/Users/Ervisa/Desktop/sudoku/sudoku/solve.txt", "a") as f:

     for line in res:
       np.savetxt(f,line,fmt='%s')
mat=['t','row','col','value']
write(mat)
def solve1():
    global Matrix,M
    row, col = findNextEmpty1()
    if row is None:
        return True
    if (row and col) > 5 and (row and col) < 9:
  
         for n in range(1, 10):
            if checkNumber(col, row, n):
             
                    Matrix[row][col] = n
                    if solve1():
                        res=['t1',row,col,n]
                        write(res)
                        M[row][col] = n
                        return True
                    Matrix[row][col] = 0
         return False
    else:
        for n in range(1, 10):
            if checkNumber(col, row, n):
                Matrix[row][col] = n
                if solve1():
                    res=['t1',row,col,n]
                    write(res)
                    M[row][col] = n
                    return True
                Matrix[row][col] = 0
        return False

# up right sudoku


def solve2():
    global Matrix,M
    row, col = findNextEmpty2()
    if row is None:
        return True
    if row > 5 and row < 9 and col > 11 and col < 15:
   
        for n in range(1, 10):
            if checkNumber(col, row, n):
               
                    Matrix[row][col] = n
                    if solve2():
                        res=['t2',row,col,n]
                        write(res)
                        print( Matrix[row][col])
                        M[row][col] = n
                        return True
                    Matrix[row][col] = 0
        return False
    else:
        for n in range(1, 10):
            if checkNumber(col, row, n):
                Matrix[row][col] = n
                if solve2():
                    res=['t2',row,col,n]
                    write(res)
                    M[row][col] = n
                    print( Matrix[row][col])
                    return True
                Matrix[row][col] = 0
        return False
# center sudoku


def solve3():
    global Matrix,M
    row, col = findNextEmpty3()
    if row is None:
        print("LLLLLLLLLLLLLLLLLLLL")
        return True
    if 5<row<9   and 5< col < 9:
      
        for n in range(1, 10):
            if checkNumberCenter(col, row, n):
                
                
                    Matrix[row][col] = n
                    if solve3():
                        res=['t3',row,col,n]
                        write(res)
                        print("AAAAAAAAAA")
                        M[row][col] = n
                        print( Matrix[row][col])
                        return True
                    Matrix[row][col] = 0
        return False
    elif row > 5 and row < 9 and col > 11 and col < 15:
      
        for n in range(1, 10):
            if checkNumberCenter(col, row, n):
               
                
                    Matrix[row][col] = n
                    if solve3():
                        res=['t3',row,col,n]
                        write(res)
                        M[row][col] = n
                        print("BBBBBBBBBB")
                        print( Matrix[row][col])
                        return True
                    Matrix[row][col] = 0
        return False
    elif row > 11 and row < 15 and col > 5 and col < 9:
    
        for n in range(1, 10):
            if checkNumberCenter(col, row, n):
                
               
                    Matrix[row][col] = n
                    if solve3():
                        res=['t3',row,col,n]
                        write(res)
                        M[row][col] = n
                        print("CCCCCCCCCC")
                        print( Matrix[row][col])
                        return True
                    Matrix[row][col] = 0
        return False
    elif row > 11 and row < 15 and col > 11 and col < 15:
     
        for n in range(1, 10):
            if checkNumberCenter(col, row, n):
                
               
                    Matrix[row][col] = n
                    if solve3():
                        res=['t3',row,col,n]
                        write(res)
                        M[row][col] = n
                        print("DDDDDDDD")
                        print( Matrix[row][col])
                        return True
                    Matrix[row][col] = 0
        return False
    else:
        for n in range(1, 10):
            if checkNumberCenter(col, row, n):
                
                Matrix[row][col] = n
                if solve3():
                    res=['t3',row,col,n]
                    write(res)
                    M[row][col] = n
                    print("XXXXXXXXXXXX")
                    print( Matrix[row][col])
                    return True
                Matrix[row][col] = 0
        return False


# down left sudoku
def solve4():
    global Matrix,M
    row, col = findNextEmpty4()
    if row is None:
        return True
    if row > 11 and row < 15 and col > 5 and col < 9:
        
         for n in range(1, 10):
            if checkNumber(col, row, n):
               
                    Matrix[row][col] = n
                    if solve4():
                        res=['t4',row,col,n]
                        write(res)
                        M[row][col] = n
                        print( Matrix[row][col])
                        return True
                    Matrix[row][col] = 0
         return False
    else:
        for n in range(1, 10):
            if checkNumber(col, row, n):
                Matrix[row][col] = n
                if solve4():
                    res=['t4',row,col,n]
                    write(res)
                    M[row][col] = n
                    print( Matrix[row][col])
                    return True
                Matrix[row][col] = 0
        return False
# down right sudoku


def solve5():
    global Matrix,M,k
    row, col = findNextEmpty5()
    if row is None:
        return True
    if row > 11 and row < 15 and col > 11 and col < 15:
      
        for n in range(1, 10):
            if checkNumber(col, row, n):
            
                    Matrix[row][col] = n
                    if solve5():
                   
                        res=['t5',row,col,n]
                        write(res)
                        M[row][col] = n
                        print( Matrix[row][col])
                        return True
                    Matrix[row][col] = 0
        return False
    else:
        for n in range(1, 10):
            if checkNumber(col, row, n):
                Matrix[row][col] = n
                if solve5():
                
                    res=['t5',row,col,n]
                    write(res)
                    M[row][col] = n
                    print( Matrix[row][col])
                    return True
                Matrix[row][col] = 0
        return False


t1 = threading.Thread(target=solve1)
t2 = threading.Thread(target=solve2)
t3 = threading.Thread(target=solve3)
t4 = threading.Thread(target=solve4)
t5 = threading.Thread(target=solve5)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
"""solve1()
solve2()
solve3()
solve4()
solve5()"""

# print(Matrix[8][6])
# print(sys.getrecursionlimit())
# time.sleep(3)
print(Matrix)
print("AAAAAAAAA")
