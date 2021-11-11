

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
                if num != "0":
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

