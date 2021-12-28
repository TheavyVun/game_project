
import tkinter as tk
import winsound

root = tk.Tk()
root.geometry('1440x700')
frame = tk.Frame()
frame.master.title('Game_Project')
canvas = tk.Canvas(frame)
canvas['bg'] = 'white'
# winImage = tk.PhotoImage(file='200w.gif')
bg = tk.PhotoImage(file='images\\ice.gif')
bg1 = tk.PhotoImage(file='images\\bg3.gif')
bg2 = tk.PhotoImage(file='images\\bg2.gif')
bg3 = tk.PhotoImage(file='images\\bg1.gif')
bg4 = tk.PhotoImage(file='images\\bg.gif')
helpImage = tk.PhotoImage(file='images\\help.png')
emty = tk.PhotoImage(file='images\\empty.gif')
myimage = tk.PhotoImage(file='images\\player.gif')
wimage = tk.PhotoImage(file='images\\door1.gif')
stoneImage = tk.PhotoImage(file='images\\wall.gif')
liveImage = tk.PhotoImage(file='images\\heart5.gif')
fruitImage = tk.PhotoImage(file='images\\fruit.gif')
enemy1 = tk.PhotoImage(file='images\\m2.gif')
enemy2 = tk.PhotoImage(file='images\\m8.gif')
enemy3 = tk.PhotoImage(file='images\\m7.gif')
enemy4 = tk.PhotoImage(file='images\\m6.gif')
text = ('Kolker Brush',80,'bold')


#  ---------------------------------------------------------------------------------
#  CONSTANTS
#  ---------------------------------------------------------------------------------

EMPTY_CELL  =  0
PLAYER_CELL = 1
WALL_CELL = 2
DOOR_CELL = 8
ENEMY_1_CELL = 3
ENEMY_2_CELL = 4
ENEMY_3_CELL = 5
ENEMY_4_CELL = 6
FRUIT_CELL = 9
LEVEL = 1
Exit = 0

# -------------Level Of Game------------------------------------------
# LEVEL01
LEVEL_1_GRID = [
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
        [2,2,0,0,0,2,2,2,2,0,0,0,2,0,0,0,2,0,0],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

enemy_Level_1 = [
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,0,0,0,0,2,9,5,0,0,2,2,2,2,6,0,2,9,2],
        [2,0,0,2,2,2,2,0,2,0,0,2,0,0,0,0,0,0,2],
        [2,3,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,2],
        [2,0,0,0,2,0,0,0,2,2,2,2,2,2,0,0,2,0,2],
        [2,0,2,2,2,2,0,0,2,0,0,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2,0,2,0,0,0,0,2,2,2,2],
        [2,0,0,2,0,0,2,0,0,0,2,4,0,0,0,0,0,0,2],
        [2,0,2,2,2,0,0,0,0,0,2,2,2,2,0,0,2,0,2],
        [2,0,0,2,9,0,0,2,0,0,2,0,0,0,0,2,2,0,2],
        [2,2,0,0,0,2,2,2,2,0,0,0,2,0,0,0,2,0,8],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]
# -------------------------------------------------------------
# LEVEL02
LEVEL_2_GRID = [
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,1,0,0,0,0,0,0,0,0,2,2,2,0,0,2,0,0,0],
        [2,0,0,2,2,2,2,2,0,0,0,0,2,0,0,0,0,0,2],
        [2,2,0,0,0,0,0,2,0,0,0,2,2,0,2,2,2,0,2],
        [2,2,0,0,0,0,0,2,0,2,0,0,2,0,0,0,2,0,2],
        [2,2,0,0,0,2,0,0,0,2,2,0,2,0,0,0,2,0,2],
        [2,2,0,2,2,2,2,2,0,2,0,0,0,0,0,2,2,2,2],
        [2,2,0,0,2,0,0,0,0,2,0,2,2,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,0,2,0,0,2,0,2,0,2,0,2],
        [2,0,2,2,2,2,2,2,2,2,2,2,2,0,2,2,2,0,2],
        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]
enemy_Level_2 = [
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,0,0,0,0,0,0,0,5,0,2,2,2,0,0,2,0,0,8],
        [2,0,0,2,2,2,2,2,0,0,0,0,2,0,0,0,0,0,2],
        [2,2,0,0,0,0,9,2,0,0,0,2,2,0,2,2,2,0,2],
        [2,2,0,0,0,0,0,2,0,2,0,0,2,0,0,9,2,0,2],
        [2,2,0,0,0,2,0,0,0,2,2,0,2,0,0,0,2,0,2],
        [2,2,0,2,2,2,2,2,0,2,4,0,0,0,0,2,2,2,2],
        [2,2,0,0,2,0,0,0,0,2,0,2,2,0,0,0,0,0,2],
        [2,3,0,0,0,0,0,0,0,2,0,9,2,0,2,0,2,0,2],
        [2,0,2,2,2,2,2,2,2,2,2,2,2,0,2,2,2,0,2],
        [2,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]
# ----------------------------------------------------------------------
# LEVEL03
LEVEL_3_GRID = [
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,1,2,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,2],
        [2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,2],
        [2,2,0,2,2,2,0,2,2,2,2,2,2,0,2,2,2,0,2],
        [2,0,0,0,2,0,0,2,0,0,0,0,2,0,0,0,2,0,2],
        [2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,2],
        [2,0,0,0,2,0,0,2,2,2,2,2,2,0,2,2,2,2,2],
        [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        [2,0,0,0,2,0,0,2,2,0,0,2,0,0,2,2,2,0,2],
        [2,0,2,2,2,2,2,2,2,2,2,2,2,0,2,0,2,0,2],
        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,0,2,2,2,2,2,2]]

enemy_Level_3 = [
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,0,2,0,0,0,5,0,0,0,0,0,0,0,2,2,0,0,2],
        [2,0,0,0,0,0,0,2,0,0,0,0,0,6,0,0,2,9,2],
        [2,2,0,2,2,2,0,2,2,2,2,2,2,0,2,2,2,0,2],
        [2,0,0,0,2,0,0,2,0,0,0,0,2,0,0,0,2,0,2],
        [2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,2],
        [2,9,0,0,2,0,0,2,2,2,2,2,2,0,2,2,2,2,2],
        [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,2],
        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,2],
        [2,0,2,2,2,2,2,2,2,2,2,2,2,0,2,9,2,0,2],
        [2,0,0,0,0,0,0,0,0,0,0,0,4,0,2,0,0,0,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,8,2,2,2,2,2,2]]

# ----------------------------------------------------------------------


# ---COPY ARRAY----------------------------------------------
def copyArray(array2d) :
    return  list(map(list, array2d))


# ---------Array of dictionary to store all Level----------------------------------
ALL_LEVEL = [
            {'grid':LEVEL_1_GRID, 'enemy':enemy_Level_1},
            {'grid':LEVEL_2_GRID, 'enemy':enemy_Level_2}, 
            {'grid':LEVEL_3_GRID, 'enemy':enemy_Level_3}]

#  ---------------------------------------------------------------------------------
#  GLOBAL VARIABLES
#  ---------------------------------------------------------------------------------
grid = copyArray(LEVEL_1_GRID)
enemy = copyArray(enemy_Level_1)


PLAYER_LIFE = 3
isLose = False
isWin = False
numOfFruit = 0

# --------------------------------------------------------------------------------------------
# -------To Copy grid of any Level----------------
def get_Array_Level():
    global ALL_LEVEL,grid,enemy,LEVEL
    grid = copyArray(ALL_LEVEL[LEVEL-1]['grid'])
    enemy = copyArray(ALL_LEVEL[LEVEL-1]['enemy'])
# ------------------------------------------------

def draw():
    arrayToDrawing()
    canvas.after(500,move_Enemy_1)
    canvas.after(1000,move_Enemy_2)
    canvas.after(1000,move_Enemy_3)
    canvas.after(100,move_Enemy_4)

def defult_Value():
    global isWin,isLose,numOfFruit,PLAYER_LIFE
    isWin = False
    isLose = False
    numOfFruit = 0
    PLAYER_LIFE = 3
   
# ---------manage Level game for player to play----------------
def play_Level_1(event):
    global LEVEL,door_Position
    defult_Value()
    LEVEL = 1
    get_Array_Level()
    door_Position = getWinPosition()
    draw()

    
def play_Level_2(event):
    global LEVEL,door_Position
    defult_Value()
    LEVEL = 2
    get_Array_Level()
    door_Position = getWinPosition()
    draw()


def play_Level_3(event):
    global LEVEL,door_Position
    defult_Value()
    LEVEL = 3
    get_Array_Level()
    door_Position = getWinPosition()
    draw()
# -----------------------------------

# ---------List of Level game----------------
def menu(event):
    global isLose,isWin
    isWin = True
    isLose = True
    canvas.create_image(0,0, image=bg4, anchor='nw')
    canvas.create_oval(100,100,200,200,fill='white',outline='')
    canvas.create_text(150,150,text='1', font=('serif',40,'bold'),tags='level_1')
    canvas.create_oval(250,100,350,200,fill='white',outline='')
    canvas.create_text(300,150,text='2', font=('serif',40,'bold'),tags='level_2')
    canvas.create_oval(400,100,500,200,fill='white',outline='')
    canvas.create_text(450,150,text='3', font=('serif',40,'bold'),tags='level_3')
    canvas.create_rectangle(0,0,150,50,fill='orange',outline='')
    canvas.create_text(75,25,text='Back',font=('serif',20,'bold'), tags='home')
    canvas.tag_bind('home','<Button-1>',homePage)
    canvas.tag_bind('level_1','<Button-1>',play_Level_1)
    canvas.tag_bind('level_2','<Button-1>',play_Level_2)
    canvas.tag_bind('level_3','<Button-1>',play_Level_3)

# --------To display tip for player to understand about the game------------
def help(event):
    canvas.create_image(0,0,image=bg3, anchor='nw')
    canvas.create_image(225,30,image=helpImage, anchor='nw')
    canvas.create_rectangle(0,0,150,50,fill='orange',outline='')
    canvas.create_text(75,25,text='Back',font=('serif',20,'bold'), tags='home')
    canvas.tag_bind('home','<Button-1>',homePage)


# ----------START graphic (homepage)----------------------
def home():
    canvas.create_image(0,0, image=bg3, anchor='nw')
    canvas.create_rectangle(560,200,860,260,fill='green', outline='')
    canvas.create_text(710,230, text='Start Game', font=('serif',25,'bold'),tags='start')
    canvas.create_rectangle(560,290,860,350,fill='red', outline='')
    canvas.create_text(710,320, text='Exit', font=('serif',25,'bold'),tags='exit')
    canvas.create_rectangle(560,380,860,440,fill='orange', outline='')
    canvas.create_text(710,410, text='Help', font=('serif',25,'bold'),tags='help')
    canvas.tag_bind('start','<Button-1>',menu)
    canvas.tag_bind('help','<Button-1>',help)
    canvas.tag_bind('exit','<Button-1>',quit)

# ---------To stop the game----------------
def quit(event):
    root.destroy()

# --------Turn to homepage---------------
def homePage(event):
    home()

# --------------draw graphic of game---------------------------
def arrayToDrawing():
    canvas.delete('all')
    global grid,enemy,numOfFruit
    canvas.create_image(0,0,image=bg, anchor='nw')
    y = 60
    for i in range(len(grid)):
        value = grid[i]
        x = 180
        for j in range(len(value)):
            if grid[i][j] == EMPTY_CELL:
                canvas.create_rectangle(x, y, x+50, y+50, fill='white')
                canvas.create_image(x,y, image=emty, anchor='nw')

            elif grid[i][j] == WALL_CELL:
                canvas.create_image(x,y, image=stoneImage, anchor='nw')

            elif grid[i][j] == PLAYER_CELL:
                canvas.create_image(x,y, image=emty, anchor='nw')
                canvas.create_image(x,y, image=myimage, anchor='nw')

            if enemy[i][j] == DOOR_CELL:
                canvas.create_image(x+1,y, image=wimage, anchor='nw')

            if enemy[i][j] == ENEMY_1_CELL:
                canvas.create_image(x+1,y, image=enemy1, anchor='nw')
            if enemy[i][j] == ENEMY_2_CELL:
                canvas.create_image(x+1,y, image=enemy2, anchor='nw')
            if enemy[i][j] == ENEMY_3_CELL:
                canvas.create_image(x+1,y, image=enemy3, anchor='nw')
            if enemy[i][j] == ENEMY_4_CELL:
                canvas.create_image(x+1,y, image=enemy4, anchor='nw')

            if enemy[i][j] == FRUIT_CELL:
                canvas.create_image(x,y, image=emty, anchor='nw')
                canvas.create_image(x,y, image=fruitImage, anchor='nw')
            x += 50
        y += 50
    canvas.create_text(210,30,text='Lives:', font=('serif',20), fill='white')
    pY = 15
    pX = 250
    for i in range(PLAYER_LIFE):
        canvas.create_image(pX,pY,image=liveImage, anchor='nw')
        pX += 41
    fruit = 'Fruits: '
    canvas.create_text(1024,30,text=fruit+str(numOfFruit)+'/3', font=('serif',20), fill='white')
    canvas.create_rectangle(0,0,150,50,fill='orange',outline='')
    canvas.create_text(75,25,text='Back',font=('serif',20,'bold'), tags='home')
    canvas.tag_bind('home','<Button-1>',menu)
    

# ------get the player position as an array :   [ row  , column  ]--------------
def getPlayerPosition():
    for i in range(len(grid)):
        value = grid[i]
        for j in range(len(value)):
            if grid[i][j] == PLAYER_CELL:
                arr = [i,j]
                return arr

# -----------Get the Win position as an array: [x,y]-------------------------------
def getWinPosition():
    for i in range(len(enemy)):
        value = enemy[i]
        for j in range(len(value)):
            if enemy[i][j] == DOOR_CELL:
                arr = [i,j]
                return arr
                
door_Position = getWinPosition()

# 
def newlive():
    global grid,LEVEL
    grid = copyArray(ALL_LEVEL[LEVEL-1]['grid'])
    arrayToDrawing()

# ----------------Display Lost-----------------
def lose():
    global isLose
    canvas.delete('all')
    isLose = True
    canvas.create_image(0,0,image=bg1, anchor='nw')
    canvas.create_text(680,340,text='Game Over', font=text)
    canvas.create_rectangle(750,420,910,470,fill='black')
    canvas.create_text(830,445,text='Try Again', font=('serif',22,'bold'),fill='white', tags='play_again')
    canvas.create_rectangle(470,420,630,470,fill='black')
    canvas.create_text(550,445,text='MENU', font=('serif',22,'bold'),fill='white', tags='menu')
    winsound.PlaySound('sound\\lose.wav', winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas.tag_bind('play_again', '<Button-1>',try_Again)
    canvas.tag_bind('menu', '<Button-1>',menu)

# -------------To Play Again---------------------
def try_Again(event):
    global isLose,isWin,grid,enemy,PLAYER_LIFE,numOfFruit,LEVEL
    isLose = False
    isWin = False
    PLAYER_LIFE = 3
    numOfFruit = 0
    get_Array_Level()
    draw()

# ---------------Display Win----------------------
def win():
    global isWin,LEVEL
    LEVEL += 1
    canvas.delete('all')
    isWin = True
    canvas.create_image(0,0,image=bg2, anchor='nw')
    canvas.create_text(680,340,text='YOU WIN', font=text, fill='orange')
    canvas.create_rectangle(520,460,660,510,fill='orange', outline='')
    canvas.create_text(590,485,text='MENU', font=('serif',22,'bold'), fill='white', tags='menu')
    canvas.create_rectangle(720,460,860,510,fill='orange', outline='')
    canvas.create_text(790,485,text='Next', font=('serif',22,'bold'), fill='white', tags='next')
    winsound.PlaySound('sound\\win.wav', winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas.tag_bind('next', '<Button-1>',next_level)
    canvas.tag_bind('menu', '<Button-1>',menu)


#  -----------------Go Next Level---------------------
def next_level(event):
    global isWin,grid,enemy,PLAYER_LIFE,numOfFruit,door_Position,LEVEL
    isWin = False
    PLAYER_LIFE = 3
    numOfFruit = 0
    get_Array_Level()
    door_Position = getWinPosition()
    draw()


# ----------Lost Lives-----------------------------
def lose_lives():
    global PLAYER_LIFE
    winsound.PlaySound('sound\\hit.wav',winsound.SND_ASYNC | winsound.SND_ASYNC)
    PLAYER_LIFE -= 1
    if PLAYER_LIFE > 0:
        newlive()
    else:
        lose()

#  --------Count Fruit-----------------------------
def count_Fruit():
    global numOfFruit
    numOfFruit += 1  

# ------------Move person on grid-------------------------
def move(deltaX, deltaY):
    global grid,PLAYER_LIFE,enemy,isLose,door_Position,isWin,numOfFruit
    playerPosition = getPlayerPosition()
    playerRow = playerPosition[0]
    playerColumn = playerPosition[1]
    door_Position_X = door_Position[0]
    door_Position_Y = door_Position[1]
    if not isLose and not isWin:
        if deltaX == 1 and deltaY == 0:
            if playerColumn+1 < len(grid[0]) and grid[playerRow][playerColumn+1] != WALL_CELL :
                winsound.PlaySound('sound\\scrat.wav',winsound.SND_ASYNC | winsound.SND_ASYNC)
                grid[playerRow][playerColumn] = EMPTY_CELL
                grid[playerRow][playerColumn+1] = PLAYER_CELL
                
                if enemy[playerRow][playerColumn+1] == FRUIT_CELL:
                    count_Fruit()
                    enemy[playerRow][playerColumn+1] = 0
                    winsound.PlaySound('sound\\acon.wav',winsound.SND_ASYNC | winsound.SND_ASYNC)

                arrayToDrawing()
            if enemy[playerRow][playerColumn+1] == ENEMY_1_CELL or enemy[playerRow][playerColumn+1] == ENEMY_2_CELL or enemy[playerRow][playerColumn+1] == ENEMY_3_CELL or enemy[playerRow][playerColumn+1] == ENEMY_4_CELL:
                lose_lives()
  
            if door_Position_X == playerRow  and door_Position_Y == playerColumn + 1 and numOfFruit == 3:
                win()  
                   
        elif deltaX == -1 and deltaY == 0:    
            if playerColumn-1 >= 0 and grid[playerRow][playerColumn-1] != WALL_CELL:
                winsound.PlaySound('sound\\scrat.wav',winsound.SND_ASYNC | winsound.SND_ASYNC)
                grid[playerRow][playerColumn] = EMPTY_CELL
                grid[playerRow][playerColumn-1] = PLAYER_CELL

                if enemy[playerRow][playerColumn-1] == FRUIT_CELL:
                    count_Fruit()
                    enemy[playerRow][playerColumn-1] = EMPTY_CELL
                    winsound.PlaySound('sound\\acon.wav',winsound.SND_ASYNC | winsound.SND_ASYNC)

                arrayToDrawing()
            if enemy[playerRow][playerColumn-1] == ENEMY_1_CELL or enemy[playerRow][playerColumn-1] == ENEMY_2_CELL or enemy[playerRow][playerColumn-1] == ENEMY_3_CELL  or enemy[playerRow][playerColumn-1] == ENEMY_4_CELL :
                lose_lives()

            if door_Position_X == playerRow  and door_Position_Y  == playerColumn - 1 and numOfFruit == 3:
                win()  
                            
        elif deltaX == 0 and deltaY == 1:  
            if playerRow+1 < len(grid) and grid[playerRow+1][playerColumn] != WALL_CELL :
                winsound.PlaySound('sound\\scrat.wav',winsound.SND_ASYNC | winsound.SND_ASYNC)
                grid[playerRow][playerColumn] = EMPTY_CELL
                grid[playerRow+1][playerColumn] = PLAYER_CELL
                if enemy[playerRow+1][playerColumn] == FRUIT_CELL:
                    count_Fruit()
                    enemy[playerRow+1][playerColumn] = EMPTY_CELL
                    winsound.PlaySound('sound\\acon.wav',winsound.SND_ASYNC | winsound.SND_ASYNC)

                arrayToDrawing()
            if enemy[playerRow+1][playerColumn] == ENEMY_1_CELL or enemy[playerRow+1][playerColumn] == ENEMY_2_CELL or enemy[playerRow+1][playerColumn] == ENEMY_3_CELL or enemy[playerRow+1][playerColumn] == ENEMY_4_CELL:
                lose_lives()

            if door_Position_X == playerRow + 1  and door_Position_Y == playerColumn and numOfFruit == 3:
                win()  
                   
        elif deltaX == 0 and deltaY == -1:  
            if playerRow-1 >= 0 and grid[playerRow-1][playerColumn] != WALL_CELL :
                winsound.PlaySound('sound\\scrat.wav',winsound.SND_ASYNC | winsound.SND_ASYNC)
                grid[playerRow][playerColumn] = EMPTY_CELL
                grid[playerRow-1][playerColumn] = PLAYER_CELL
                if enemy[playerRow-1][playerColumn] == FRUIT_CELL:
                    count_Fruit()
                    enemy[playerRow-1][playerColumn] = EMPTY_CELL
                    winsound.PlaySound('sound\\acon.wav',winsound.SND_ASYNC | winsound.SND_ASYNC)
                arrayToDrawing()
            if enemy[playerRow-1][playerColumn] == ENEMY_1_CELL or enemy[playerRow-1][playerColumn] == ENEMY_2_CELL or enemy[playerRow-1][playerColumn] == ENEMY_3_CELL or enemy[playerRow-1][playerColumn] == ENEMY_4_CELL:
                lose_lives()

            if door_Position_X == playerRow - 1  and door_Position_Y == playerColumn and numOfFruit == 3:
                win()  
                   
def moveRight(event):
    move(1,0)

def moveLeft(event):
    move(-1,0)

def moveDown(event):
    move(0,1)

def moveUp(event):
    move(0,-1)

# --------------ENEMYMOVE--------------
move_rignt = True
move_up = True
move_down = True
move_left = True

def enemyPositions(enemy_P):
    global enemy
    for i in range(len(enemy)):
        for j in range(len(enemy[i])):
            if enemy[i][j] == enemy_P:
                allPosition = [i,j]
                return allPosition

def move_Enemy_1():
    global enemy,move_rignt,PLAYER_LIFE,move_left,isWin,isLose
    if not isWin and not isLose:
        canvas.delete('all')
        enemy_Positions = enemyPositions(ENEMY_1_CELL)
        p_X = enemy_Positions[0]
        p_Y = enemy_Positions[1]

        if enemy[p_X][p_Y+1] == WALL_CELL:
            move_rignt = False

        elif enemy[p_X][p_Y-1] == WALL_CELL:
            move_rignt = True       
        if p_Y + 1 < len(enemy[0]) and enemy[p_X][p_Y+1] == EMPTY_CELL and move_rignt:
            enemy[p_X][p_Y] = EMPTY_CELL
            enemy[p_X][p_Y + 1] = ENEMY_1_CELL
            if grid[p_X][p_Y + 1] == PLAYER_CELL:
                lose_lives()

            
        if p_Y > 0 and enemy[p_X][p_Y-1] == EMPTY_CELL and not move_rignt:
            enemy[p_X][p_Y] = EMPTY_CELL
            enemy[p_X][p_Y - 1] = ENEMY_1_CELL  
            if grid[p_X][p_Y - 1] == PLAYER_CELL:
                lose_lives()

        if PLAYER_LIFE >0:
            arrayToDrawing()
            canvas.after(500,move_Enemy_1)

def move_Enemy_2():
    global enemy,move_rignt,PLAYER_LIFE,move_left,isWin,isLose

    if not isLose and not isWin:      
        canvas.delete('all')
        enemy_Positions = enemyPositions(ENEMY_2_CELL)
        p_X = enemy_Positions[0]
        p_Y = enemy_Positions[1]

        if enemy[p_X][p_Y+1] == WALL_CELL:
            move_left = True
        elif enemy[p_X][p_Y-1] == WALL_CELL:
            move_left = False  
        if p_Y + 1 < len(enemy[0]) and enemy[p_X][p_Y+1] == EMPTY_CELL and not move_left:
            enemy[p_X][p_Y] = EMPTY_CELL
            enemy[p_X][p_Y + 1] = ENEMY_2_CELL
            if grid[p_X][p_Y + 1] == PLAYER_CELL:
                lose_lives()
 
            
        if p_Y > 0 and enemy[p_X][p_Y-1] == EMPTY_CELL and move_left:
            enemy[p_X][p_Y] = EMPTY_CELL
            enemy[p_X][p_Y - 1] = ENEMY_2_CELL  
            if grid[p_X][p_Y - 1] == PLAYER_CELL:
                lose_lives()

        if PLAYER_LIFE>0:
            arrayToDrawing()
            canvas.after(1000,move_Enemy_2)

def move_Enemy_3():
    global enemy,move_up,PLAYER_LIFE,move_down,isWin,isLose

    if not isWin and not isLose:     
        canvas.delete('all')
        enemy_Positions = enemyPositions(ENEMY_3_CELL)
        p_X = enemy_Positions[0]
        p_Y = enemy_Positions[1]

        if enemy[p_X+1][p_Y] == WALL_CELL:
            move_down = False
        elif enemy[p_X-1][p_Y] == WALL_CELL:
            move_down = True   

        if p_X + 1 < len(enemy) and enemy[p_X+1][p_Y] == EMPTY_CELL and move_down :
            enemy[p_X][p_Y] = EMPTY_CELL
            enemy[p_X + 1][p_Y ] = ENEMY_3_CELL
            if grid[p_X+ 1][p_Y ] == PLAYER_CELL:
                lose_lives()

            
        if p_Y > 0 and enemy[p_X-1][p_Y] == EMPTY_CELL and not move_down :
            enemy[p_X][p_Y] = EMPTY_CELL
            enemy[p_X - 1][p_Y] = ENEMY_3_CELL  
            if grid[p_X - 1][p_Y] == PLAYER_CELL:
                lose_lives()
 
        if PLAYER_LIFE>0:
            arrayToDrawing()
            canvas.after(1000,move_Enemy_3)

def move_Enemy_4():
    global enemy,move_up,PLAYER_LIFE,isWin,isLose
    if not isLose and not isWin:      
        canvas.delete('all')
        enemy_Positions = enemyPositions(ENEMY_4_CELL)
        p_X = enemy_Positions[0]
        p_Y = enemy_Positions[1]

        if enemy[p_X+1][p_Y] == WALL_CELL:
            move_up = True
        elif enemy[p_X-1][p_Y] == WALL_CELL:
            move_up = False 


        if p_X + 1 < len(enemy) and enemy[p_X+1][p_Y] == EMPTY_CELL and not move_up:
            enemy[p_X][p_Y] = EMPTY_CELL
            enemy[p_X+ 1][p_Y ] = ENEMY_4_CELL
            if grid[p_X+ 1][p_Y ] == PLAYER_CELL:
                lose_lives()
 
            
        if p_X > 0 and enemy[p_X-1][p_Y] == EMPTY_CELL and move_up:
            enemy[p_X][p_Y] = EMPTY_CELL
            enemy[p_X- 1][p_Y ] = ENEMY_4_CELL  
            if grid[p_X- 1][p_Y ] == PLAYER_CELL:
                lose_lives()
  
        if PLAYER_LIFE>0:
            arrayToDrawing()
            canvas.after(100,move_Enemy_4)


home()


root.bind('<Right>', moveRight)
root.bind('<Left>', moveLeft)
root.bind('<Down>', moveDown)
root.bind('<Up>', moveUp)

winsound.PlaySound('sound\\sound.wav', winsound.SND_LOOP | winsound.SND_ASYNC)

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()