# project team

import tkinter as tk
from tkinter import font
from tkinter.constants import NW

root = tk.Tk()
root.geometry('1440x700')
frame = tk.Frame()
frame.master.title('Game_Project')
canvas = tk.Canvas(frame)
canvas['bg'] = 'white'

bg = tk.PhotoImage(file='bg.gif')

# canvas.create_image(20,40, image=bg, anchor=NW)

# canvas.create_text(700,250, text='Loading...', font=("Helvetica",39), fill='black')
# canvas.create_rectangle(515,325,925,330, fill='black')
# canvas.create_rectangle(515,325,520,375, fill='black')
# canvas.create_rectangle(920,325,925,375, fill='black')
# canvas.create_rectangle(515,370,925,375, fill='black')

# x = 525
# def loading():
#     global x
#     y = 335
#     a = canvas.create_rectangle(x,y,x+25,y+30,fill='black')
#     x +=25


# canvas.after(1000, lambda:loading())
# canvas.after(2000, lambda:loading())
# for i in range(5):
#     canvas.after(3000, lambda:loading())






























canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()