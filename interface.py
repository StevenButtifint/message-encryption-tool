import tkinter as tk
from constants import *


def setOutputText(text_box, content):
    text_box.configure(state=tk.NORMAL)
    text_box.delete('1.0', tk.END)
    text_box.insert("1.0", content)
    text_box.configure(state=tk.DISABLED)
  

def makeFrame(parentFrame, rw, rh, rx, ry, bg,anchor):
    frame = tk.Frame(parentFrame, bg=bg)
    frame.place(relwidth=rw, relheight=rh, relx=rx, rely=ry, anchor=anchor)
    return frame


def makeLabel(frame, text, font_size, x, y):
    label = tk.Label(frame, text=text, bg=COLOUR_PRIME, fg=COLOUR_TEXT, font=(COLOUR_SECOND,font_size))
    label.place(x=x, y=y)
    return label


