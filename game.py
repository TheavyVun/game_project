
import tkinter as tk

root = tk.Tk()
root.geometry('1440x700')
frame = tk.Frame()
frame.master.title('Game_Project')
canvas = tk.Canvas(frame)
canvas['bg'] = 'white'
winImage = tk.PhotoImage(file='200w.gif')
myimage = tk.PhotoImage(file='pp.gif')
wimage = tk.PhotoImage(file='w.gif')

#  ---------------------------------------------------------------------------------
#  CONSTANTS
#  ---------------------------------------------------------------------------------

EMPTY_CELL  =  0
PLAYER_CELL = 1
WALL_CELL = 2
DOOR_CELL = 8
ENEMY_CELL = 3


#  ---------------------------------------------------------------------------------
#  GLOBAL VARIABLES
#  ---------------------------------------------------------------------------------
grid = [
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,0,0,0,2,0,0,0,0,2,2,2,2,0,0,2,0,2],
    [2,0,0,2,2,2,2,0,2,0,0,2,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,2],
    [2,0,0,0,2,0,0,0,2,2,2,2,2,2,0,0,2,0,2],
    [2,0,2,2,2,2,0,0,2,0,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,2,0,2,0,0,0,0,2,2,2,2],
    [2,0,0,2,0,0,2,0,0,0,2,0,0,0,0,0,0,0,2],
    [2,0,2,2,2,0,0,0,0,0,2,2,2,2,0,0,2,0,2],
    [2,0,0,2,0,0,0,2,0,0,2,0,0,0,0,2,2,0,2],
    [2,2,0,0,0,2,2,2,2,0,0,0,2,0,0,0,2,8,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

enemy = [
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,0,0,0,0,2,0,0,0,0,2,2,2,2,3,0,2,0,2],
    [2,0,0,2,2,2,2,0,2,0,0,2,0,0,0,0,0,0,2],
    [2,3,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,2],
    [2,0,0,0,2,0,0,0,2,2,2,2,2,2,0,0,2,0,2],
    [2,0,2,2,2,2,0,0,2,0,0,0,0,0,0,0,0,3,2],
    [2,0,0,0,0,0,0,0,2,0,2,0,0,0,0,2,2,2,2],
    [2,0,0,2,0,0,2,0,0,0,2,3,0,0,0,0,0,0,2],
    [2,0,2,2,2,0,0,3,0,0,2,2,2,2,0,0,2,0,2],
    [2,0,0,2,0,0,0,2,0,0,2,0,0,0,0,2,2,0,2],
    [2,2,0,0,0,2,2,2,2,0,0,0,2,0,0,0,2,8,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]


# draw graphic of game
def arrayToDrawing():
    canvas.delete('all')
    global grid
    global enemy
    y = 60
    for i in range(len(grid)):
        a = grid[i]
        x = 150
        for j in range(len(a)):
            if grid[i][j] == 0:
                canvas.create_rectangle(x, y, x+50, y+50, fill='white')
            elif grid[i][j] == 2:
                canvas.create_rectangle(x, y, x+50, y+50, fill='black')
            elif grid[i][j] == 1:
                # canvas.create_rectangle(x, y, x+60, y+60, fill='red')
                canvas.create_image(x,y, image=myimage, anchor='nw')
            elif grid[i][j] == 8:
                # canvas.create_rectangle(x, y, x+60, y+60, fill='green')
                canvas.create_image(x+1,y, image=wimage, anchor='nw')
            if enemy[i][j] == 3:
                canvas.create_rectangle(x, y, x+50, y+50, fill='orange')
            x += 50
        y += 50


# get the player position as an array :   [ row  , column  ]
def getPlayerPosition():
    arr = []
    for i in range(len(grid)):
        value = grid[i]
        for j in range(len(value)):
            if grid[i][j] == PLAYER_CELL:
                arr.append(i)
                arr.append(j)
                return arr


def displayWin():
    canvas.delete('all')
    canvas.create_image(660,340,image=winImage)



def move(deltaX, deltaY):
    global grid
    playerPosition = getPlayerPosition()
    playerRow = playerPosition[0]
    playerColumn = playerPosition[1]
    if deltaX == 1 and deltaY == 0:
        if playerColumn+1 < len(grid[0]) and grid[playerRow][playerColumn+1] == 0:
            grid[playerRow][playerColumn] = EMPTY_CELL
            grid[playerRow][playerColumn+1] = PLAYER_CELL
            arrayToDrawing()

    elif deltaX == -1 and deltaY == 0:    
        if playerColumn-1 >= 0 and grid[playerRow][playerColumn-1] == 0:
            grid[playerRow][playerColumn] = EMPTY_CELL
            grid[playerRow][playerColumn-1] = PLAYER_CELL
            arrayToDrawing()

    elif deltaX == 0 and deltaY == 1:  
        if playerRow+1 < len(grid) and (grid[playerRow+1][playerColumn] == 0 or grid[playerRow+1][playerColumn] == 8):
            grid[playerRow][playerColumn] = EMPTY_CELL
            grid[playerRow+1][playerColumn] = PLAYER_CELL
            arrayToDrawing()

    elif deltaX == 0 and deltaY == -1:  
        if playerRow-1 >= 0 and grid[playerRow-1][playerColumn] == 0 and not(playerRow ==9 and playerColumn == 16):
            grid[playerRow][playerColumn] = EMPTY_CELL
            grid[playerRow-1][playerColumn] = PLAYER_CELL
            arrayToDrawing()
    

    

   


# Move person on grid
def moveRight(event):
    move(1,0)


def moveLeft(event):
    move(-1,0)


def moveDown(event):
    move(0,+1)


def moveUp(event):
    move(0,-1)





arrayToDrawing()

root.bind('<Right>', moveRight)
root.bind('<Left>', moveLeft)
root.bind('<Down>', moveDown)
root.bind('<Up>', moveUp)
























canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()