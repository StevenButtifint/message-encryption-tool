import tkinter as tk
from PIL import Image, ImageTk
from constants import *



def makeCanvas(frame, h, w, bg):
    canvas = tk.Canvas(frame, height=h, width=w, bg=bg)
    canvas.config(highlightthickness=0)
    canvas.pack()
    return canvas


def setOutputText(text_box, content):
    text_box.configure(state=tk.NORMAL)
    text_box.delete('1.0', tk.END)
    text_box.insert("1.0", content)
    text_box.configure(state=tk.DISABLED)
  

def makeFrame(parentFrame, rw, rh, rx, ry, bg,anchor):
    frame = tk.Frame(parentFrame, bg=bg)
    frame.place(relwidth=rw, relheight=rh, relx=rx, rely=ry, anchor=anchor)
    return frame


def makeLabel(frame, text, font_size, x, y, anchor, bg):
    label = tk.Label(frame, text=text, bg=bg, fg=COLOUR_TEXT, font=(COLOUR_SECOND,font_size))
    label.place(x=x, y=y, anchor=anchor)
    return label


def makeEntry(frame, width, bg, fg, rx, ry):
    entry = tk.Entry(frame, width=width, bg=bg, fg=fg)
    entry.place(relx=rx, rely=ry)
    return entry


def makeTextbox(frame, width, height, bg, fg, rx, ry):
    textbox = tk.Text(frame, width=width, height=height, bg=bg, fg=fg)
    textbox.place(relx=rx, rely=ry, anchor="center")
    return textbox


def makeOptionMenu(frame, options, func, w, x, y):
    stringVar = tk.StringVar(frame)
    stringVar.set(options[0])
    optionMenu = tk.OptionMenu(frame, stringVar, *options, command=func)
    optionMenu.config(width=w, bg=COLOUR_THIRD, fg=COLOUR_TEXT)
    optionMenu["highlightthickness"]=0
    optionMenu["menu"].config(bg=COLOUR_THIRD, borderwidth=0)
    optionMenu.place(x=x, y=y)
    return stringVar


def makeButton(frame, text, func, w, x ,y):
    button = tk.Button(frame, text=text, command= func)
    button.config(width=w, bg=COLOUR_THIRD)
    button.place(x=x, y=y)
    return button
    

def placeImage(parent, file, w, h, x, y):
    canvas = tk.Canvas(parent, bg=COLOUR_SECOND, width=w, height=h)
    canvas.place(x=x, y=y)
    canvas["highlightthickness"]=0
    img = Image.open(file)
    img = img.resize((w,h), Image.ANTIALIAS)
    photoimage = ImageTk.PhotoImage(img)
    canvas.create_image(w//2, h//2, image=photoimage)
    return canvas, photoimage


def makeScale(frame, minVal, maxVal, rx, ry, height, width, bg, fg):
    scale = tk.Scale(frame, orient='horizontal', from_=minVal, to=maxVal, width=height, length=width, bg=bg, fg=fg)
    scale.place(relx=rx, rely=ry, anchor="center")
    return scale

