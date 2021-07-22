import tkinter as tk
from tkinter import filedialog, Text, Listbox, filedialog, Entry


APP_TITLE   = "Message Encryption Tool"

WINDOW_H    = 500
WINDOW_W    = 500

FIRST_COL   = "cyan4"
SECOND_COL  = "cyan2"


def createInterface():
    pass




if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(width=False, height=False)
    root.title(APP_TITLE)
    canvas = tk.Canvas(root, height=WINDOW_H, width=WINDOW_W, bg=FIRST_COL).pack()
    createInterface()
