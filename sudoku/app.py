

import pygame
from settings import *


class App:
    def __init__(self):
       pygame.init()
       self.window =pygame.display.set_mode((800, 800))
       self.running = True
       self.grid =board
       self.selected=None
       self.mousePos=None
       self.font =pygame.font.SysFont("arial", cellSize//2)

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
          
        pygame.quit()
        SystemExit()

    def events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.running= False
            if event.type== pygame.MOUSEBUTTONDOWN:
               selected  = self.mouseOnGrid()
               if selected: 
                 print(self.mouseOnGrid())
                 self.selected=selected
               else:
                   print("not on board")
                   self.selected=None
    def update(self):
       self.mousePos=pygame.mouse.get_pos()

    def draw(self):
        self.window.fill(WHITE)
        if self.selected:
            self.drawSelection(self.window,self.selected)
        self.drawNumbers(self.window)

        self.drawGrid(self.window)
        pygame.display.update()
    def drawNumbers(self,window):
        for yidx, row in enumerate(self.grid):
            for xidx,num in enumerate(row):
                if yidx<=8 and xidx<=8:
                  if num != "*":
                    pos =[(xidx*cellSize)+gridPos[0],(yidx*cellSize)+gridPos[1]]
                    self.textToScreen(window,str(num),pos)
                if  xidx>=9  and yidx>=6 and yidx<=8:
                  if num != "*":
                    pos =[(xidx*cellSize)+gridPos[0],(yidx*cellSize)+gridPos[1]]
                    self.textToScreen(window,str(num),pos)
                if  xidx>=9 and xidx<=11 and yidx>=12 and yidx<=14:
                  if num != "*":
                    pos =[(xidx*cellSize)+gridPos[0],(yidx*cellSize)+gridPos[1]]
                    self.textToScreen(window,str(num),pos)
                if yidx>=9 and yidx<=11 and xidx<=8:
                  if num != "*":
                    pos =[(xidx*cellSize)+gridPos[0]+180,(yidx*cellSize)+gridPos[1]]
                    self.textToScreen(window,str(num),pos)
                if yidx<=5 and xidx>8:
                  if num != "*":
                    pos =[(xidx*cellSize)+gridPos[0]+90,(yidx*cellSize)+gridPos[1]]
                    self.textToScreen(window,str(num),pos)
                if yidx>=12 and yidx<=14 and xidx>11:
                  if num != "*":
                    pos =[(xidx*cellSize)+gridPos[0],(yidx*cellSize)+gridPos[1]]
                    self.textToScreen(window,str(num),pos)
                if yidx>14 and xidx>8:
                  if num != "*":
                    pos =[(xidx*cellSize)+gridPos[0]+90,(yidx*cellSize)+gridPos[1]]
                    self.textToScreen(window,str(num),pos)
                if yidx>=12 and xidx<=8:
                  if num != "*":
                    pos =[(xidx*cellSize)+gridPos[0],(yidx*cellSize)+gridPos[1]]
                    self.textToScreen(window,str(num),pos)
    def drawSelection(self,window,pos):
        pygame.draw.rect(window,LightBlue,((pos[0]*cellSize)+gridPos[0], (pos[1]*cellSize)+gridPos[1],cellSize,cellSize))
        
    def drawGrid(self,window):
        pygame.draw.rect(window, Black, (gridPos[0],gridPos[1], 630,630),2)
        for x in range(10):
             pygame.draw.line(window,Black,(gridPos[0]+(x*cellSize),gridPos[1]), (gridPos[0]+(x*cellSize),gridPos[1]+270),2 if x%3==0 else 1) 
             pygame.draw.line(window,Black,(gridPos[0],gridPos[1]+(x*cellSize)), (gridPos[0]+270,gridPos[1]+(x*cellSize)),2 if x%3==0 else 1) 
        for x in range(12,22):
             pygame.draw.line(window,Black,(gridPos[0]+(x*cellSize),gridPos[1]), (gridPos[0]+(x*cellSize),gridPos[1]+270),2 if x%3==0 else 1) 
        for x in range(10):
             pygame.draw.line(window,Black,(gridPos[2],gridPos[1]+(x*cellSize)), (gridPos[2]+270,gridPos[1]+(x*cellSize)),2 if x%3==0 else 1) 
        for x in range(10):
             pygame.draw.line(window,Black,(gridPos[0]+(x*cellSize),gridPos[3]), (gridPos[0]+(x*cellSize),gridPos[3]+270),2 if x%3==0 else 1) 
             pygame.draw.line(window,Black,(gridPos[0],gridPos[3]+(x*cellSize)), (gridPos[0]+270,gridPos[3]+(x*cellSize)),2 if x%3==0 else 1)
        for x in range(12,22):
             pygame.draw.line(window,Black,(gridPos[0]+(x*cellSize),gridPos[3]), (gridPos[0]+(x*cellSize),gridPos[3]+270),2 if x%3==0 else 1) 
        for x in range(10):
             pygame.draw.line(window,Black,(gridPos[2],gridPos[3]+(x*cellSize)), (gridPos[2]+270,gridPos[3]+(x*cellSize)),2 if x%3==0 else 1)
        for x in range(6,16):
             pygame.draw.line(window,Black,(gridPos[0]+(x*cellSize),gridPos[5]), (gridPos[0]+(x*cellSize),gridPos[5]+90),2 if x%3==0 else 1) 
        for x in range(4):
             pygame.draw.line(window,Black,(gridPos[4],gridPos[5]+(x*cellSize)), (gridPos[4]+270,gridPos[5]+(x*cellSize)),2 if x%3==0 else 1)
        for x in range(9,12):
             pygame.draw.line(window,Black,(gridPos[0]+(x*cellSize),gridPos[6]), (gridPos[0]+(x*cellSize),gridPos[6]+90),2 if x%3==0 else 1) 
        for x in range(3):
            pygame.draw.line(window,Black,(gridPos[7],gridPos[6]+(x*cellSize)), (gridPos[7]+90,gridPos[6]+(x*cellSize)),2 if x%3==0 else 1)
        for x in range(9,12):
            pygame.draw.line(window,Black,(gridPos[0]+(x*cellSize),gridPos[3]), (gridPos[0]+(x*cellSize),gridPos[3]+90),2 if x%3==0 else 1) 
        for x in range(4):
            pygame.draw.line(window,Black,(gridPos[7],gridPos[3]+(x*cellSize)), (gridPos[7]+90,gridPos[3]+(x*cellSize)),2 if x%3==0 else 1)

    def mouseOnGrid(self):
        if self.mousePos[0]<gridPos[0] or self.mousePos[1]<gridPos[1]:
          return False
        if self.mousePos[0]>gridPos[0]+gridSize or self.mousePos[1]>gridPos[1]+gridSize:
           return False
        return((self.mousePos[0]-gridPos[0])//cellSize,(self.mousePos[1]-gridPos[1])//cellSize)
    def textToScreen(self,window,text,pos):
        font=self.font.render(text,False,Black)
        fontWidth= font.get_width()
        fontHeight= font.get_height()
        pos[0]+= (cellSize-fontWidth)//2
        pos[1] += (cellSize-fontHeight)//2
        window.blit(font, pos)

    def checkNumber(x, y, n):
        global board
      #up-left sudoku
        if(x<9 and y<9):
          #joint square
          if (x>5 and y>5):
           for i in range(0, 15):
              print(board[y][i])
              if board[y][i] == n:
                return False
     
           for i in range(0, 9):
             print(board[i][x])
             if board[i][x] or board[9][x-6] or board[10][x-6] or board[11][x-6] or board[12][x] or board[13][x] or board[14][x]== n:
                return False
          
           x0 = (x//3)*3
           y0 = (y//3)*3
           for i in range(0, 3):
             for j in range(0, 3):
              #  print(board[y0+i][x0+j])
                if board[y0+i][x0+j] == n:
                    return False
             return True 
          else:
           for i in range(0, 9):
              print(board[y][i])
              if board[y][i] == n:
                return False
     
           for i in range(0, 9):
         
            print(board[i][x])
            if board[i][x] == n:
                return False
          
           x0 = (x//3)*3
           y0 = (y//3)*3
     
           for i in range(0, 3):
            for j in range(0, 3):
              #  print(board[y0+i][x0+j])
                if board[y0+i][x0+j] == n:
                    return False
           return True 
        # up-right sudoku
        if(x>8 and y<9):
          if ( y>5 and x>14):
            for i in range(12, 21):
              if board[y][i] == n:
                return False
            for i in range (0,6):
             if board[i][x-3] or board[6][x]or board[7][x] or board[8][x]     == n:
                  return False
            x0 = (x//3)*3
            y0 = (y//3)*3
     
            for i in range(0, 3):
                 for j in range(0, 3):
              #  print(board[y0+i][x0+j])
                    if board[y0+i][x0+j] == n:
                      return False
                 return True 
          #joint square
          elif (x>11 and x<15 and y>5):
            for i in range(6, 21):
              
              if board[y][i] == n:
                return False
     
            for i in range(0, 6):
             if board[i][x-3] or board[9][x-6] or board[10][x-6] or board[11][x-6] or board[12][x] or board[13][x] or board[14][x]== n:
                 return False
          
            x0 = (x//3)*3
            y0 = (y//3)*3
            for i in range(0, 3):
             for j in range(0, 3):
              #  print(board[y0+i][x0+j])
                if board[y0+i][x0+j] == n:
                    return False
             return True 
          else: 
             for i in range(9, 18):
              if board[y][i] == n:
                return False
             for i in range(0, 6):
                print(board[i][x])
                if board[i][x] or board[6][x+3]or board[7][x+3] or board[8][x+3]   == n:
                  return False
          
             x0 = (x//3)*3
             y0 = (y//3)*3
     
             for i in range(0, 3):
                 for j in range(0, 3):
              #  print(board[y0+i][x0+j])
                    if board[y0+i][x0+j] == n:
                      return False
                 return True 
        #down-right sudoku  
        if(x>8 and y>11):
          if y<15 and x>14:
            for i in range(12, 21):
              print(board[y][i])
              if board[y][i] == n:
                return False
            for i in range(15, 21):
         
               print(board[i][x])
               if board[i][x-3]   == n:
                 return False
          
            x0 = (x//3)*3
            y0 = (y//3)*3
     
            for i in range(0, 3):
              for j in range(0, 3):
              #  print(board[y0+i][x0+j])
                if board[y0+i][x0+j] == n:
                    return False
              return True
           #joint square
          elif (x>11 and x<15 and y<15):
            for i in range(6, 21):
              
              if board[y][i] == n:
                return False
     
            for i in range(15, 21):
             if board[i][x-3] or board[6][x] or board[7][x] or board[8][x]or board[9][x-6] or board[10][x-6] or board[11][x-6] == n:
                 return False
          
            x0 = (x//3)*3
            y0 = (y//3)*3
            for i in range(0, 3):
             for j in range(0, 3):
              #  print(board[y0+i][x0+j])
                if board[y0+i][x0+j] == n:
                    return False
                return True 
          else:
            for i in range(9, 18):
              print(board[y][i])
              if board[y][i] == n:
                return False
          for i in range(15, 21):
         
            print(board[i][x])
            if board[i][x] or board[12][x+3]or board[13][x+3] or board[14][x+3]   == n:
                return False
          
          x0 = (x//3)*3
          y0 = (y//3)*3
     
          for i in range(0, 3):
            for j in range(0, 3):
              #  print(board[y0+i][x0+j])
                if board[y0+i][x0+j] == n:
                    return False
          return True 
        #down-left sudoku
        if(x<9 and y>11):
          #joint square
          if (x>5 and y<15):
            for i in range(0, 15):
              print(board[y][i])
              if board[y][i] == n:
                return False
     
            for i in range(12, 21):
             print(board[i][x])
             if board[i][x] or board[9][x-6] or board[10][x-6] or board[11][x-6] or board[16][x] or board[7][x] or board[8][x]== n:
                return False
          
            x0 = (x//3)*3
            y0 = (y//3)*3
            for i in range(0, 3):
             for j in range(0, 3):
              #  print(board[y0+i][x0+j])
                if board[y0+i][x0+j] == n:
                    return False
            return True 
          else:
           for i in range(0, 9):
              print(board[y][i])
              if board[y][i] == n:
                return False
     
           for i in range(0, 9):
         
            print(board[i][x])
            if board[i][x] == n:
                return False
          
           x0 = (x//3)*3
           y0 = (y//3)*3
     
           for i in range(0, 3):
            for j in range(0, 3):
              #  print(board[y0+i][x0+j])
                if board[y0+i][x0+j] == n:
                    return False
           return True 
     #up-middle 3*3 square
        if(x>8 and x<12) and (y>5 and y<9):
            for i in range(6, 15):
              print(board[y][i])
              if board[y][i] == n:
                return False
     
            for i in range(9, 12):
             print(board[i][x])
             if board[i][x-3] or board[12][x] or board[13][x] or board[14][x] == n:
                return False
          
            x0 = (x//3)*3
            y0 = (y//3)*3
            for i in range(0, 3):
             for j in range(0, 3):
              #  print(board[y0+i][x0+j])
                if board[y0+i][x0+j] == n:
                    return False
            return True 
      #down-middle 3*3 square
        if(x>8 and x<12) and (y>5 and y<9):
            for i in range(6, 15):
              print(board[y][i])
              if board[y][i] == n:
                return False
     
            for i in range(9, 12):
             print(board[i][x])
             if board[i][x-3] or board[12][x] or board[13][x] or board[14][x] == n:
                return False
          
            x0 = (x//3)*3
            y0 = (y//3)*3
            for i in range(0, 3):
             for j in range(0, 3):
                if board[y0+i][x0+j] == n:
                    return False
            return True 
      #middle 6*3 
        if(x<9 and y>8 and y<12):
            for i in range(0, 9):
              print(board[y][i])
              if board[y][i] == n:
                return False
     
            for i in range(6, 9):
             print(board[i][x])
             if board[i][x+6] or board[12][x] or board[13][x] or board[14][x] == n:
                return False
          
            x0 = (x//3)*3
            y0 = (y//3)*3
            for i in range(0, 3):
             for j in range(0, 3):
              #  print(board[y0+i][x0+j])
                if board[y0+i][x0+j] == n:
                    return False
            return True 
    print(checkNumber(8,10,str(8)))
