import tkinter as tk
from tkinter import filedialog, Text, Listbox, filedialog, Entry


APP_TITLE   = "Message Encryption Tool"
APP_ICON    = "icon.ico"

WINDOW_H    = 500
WINDOW_W    = 500

COL_PRIME   = "cyan4"
COL_SECND   = "cyan2"
COL_THIRD   = "DarkSlateGray3"
COL_TEXT    = "white"


def makeFrame(root):
    return tk.Frame(root, bg=COL_PRIME)


def makeLabel(frame, text, font_size):
    return tk.Label(frame, text=text, bg=COL_PRIME, fg=COL_SECND, font=(COL_SECND,font_size))


def createTitleInterface():
    title_frame = makeFrame(root).place(relwidth=1, relheight=0.06, relx=0, rely=0)
    title_label = makeLabel(title_frame, "Message Encrypter", 14).place(x=170, y=2)


def createInputInterface():
    input_frame = makeFrame(root).place(relwidth=1, relheight=0.4, relx=0, rely=0.062)
    messg_label = makeLabel(input_frame, "Enter Message:", 12).place(x=10, y=35)
    messg_entry = tk.Text(input_frame, width=60, height=10, bg=COL_THIRD, fg=COL_TEXT).place(x=10, y=60)


def createInterface():
    createTitleInterface()
    createInputInterface()




if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(width=False, height=False)
    root.title(APP_TITLE)
    root.iconbitmap(APP_ICON)
    canvas = tk.Canvas(root, height=WINDOW_H, width=WINDOW_W, bg=COL_THIRD).pack()
    createInterface()
