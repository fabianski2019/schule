from tkinter import *
from math import *
from time import *
import time

# ---------------------------------------------------------------------------

root = Tk()
root.title('7 Segment-Anzeige')
root.minsize(width=540, height=150)
canvas = Canvas(root, width=540, height=150)
canvas.pack()  # geometry manager

# ---------------------------------------------------------------------------

def draw_digit(x_offset):
    Segments = [(2, 1, 7, 2), (7, 2, 8, 7), (7, 8, 8, 13), (2, 13, 7, 14), (1, 8, 2, 13), (1, 2, 2, 7), (2, 7, 7, 8)]
    dx = 10
    dy = 54  # grubinger

    for i in range(len(Segments)):
        canvas.create_rectangle((Segments[i][0] + x_offset) * dx, Segments[i][1] * dx,
                                (Segments[i][2] + x_offset) * dx, Segments[i][3] * dx, fill= 'blue')

def draw():
    canvas.delete("all")
    for i in range(6):
        draw_digit(i * 9)

def TimeString():
    fro i in range(3):
        if len(str(localtime()[i+3]))< 2:
            jetzt = jetzt + '0' + str(localtime()[i+3])
        else 

# ---------------------------------------------------------------------------

draw()  # Funktionsaufruf
root.mainloop()
