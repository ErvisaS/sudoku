Width= 800
Height=800
Red=(255,0,0)
WHITE=(255,255,255)
Black =(0,0,0)
LightBlue=(96,216,232)
#board
p=1
while p:

    try:
            f = open(r"C:\Users\Ervisa\Desktop\sudoku\sudoku\sud1.txt", 'r')
            p = 0
    except FileNotFoundError:
            print("File not found. (Example test cases can be found under "
                  "~/tests)\n")
board = f.read().split('\n')

#Positions and sizes

gridPos=(20,40,380,400,200,310,220,290)
cellSize= 30
gridSize=cellSize*21
finished= False