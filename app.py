import tkinter as tk
from tkinter import filedialog, Text, Listbox, filedialog, Entry, OptionMenu, StringVar


APP_TITLE   = "Message Encryption Tool"
APP_ICON    = "icon.ico"

WINDOW_H    = 500
WINDOW_W    = 500

COL_PRIME   = "cyan4"
COL_SECND   = "cyan2"
COL_THIRD   = "DarkSlateGray3"
COL_TEXT    = "white"

ENC_TYPES   = ["option1", "option2", "option3"]


def makeFrame(root):
    frame = tk.Frame(root, bg=COL_PRIME)
    return frame


def makeLabel(frame, text, font_size):
    return tk.Label(frame, text=text, bg=COL_PRIME, fg=COL_SECND, font=(COL_SECND,font_size))
    

def createInterface():
    title_frame = makeFrame(root).place(relwidth=1, relheight=0.06, relx=0, rely=0)
    title_label = makeLabel(title_frame, "Message Encrypter", 14).place(x=170, y=2)
    
    input_frame = makeFrame(root).place(relwidth=1, relheight=0.4, relx=0, rely=0.062)
    messg_label = makeLabel(input_frame, "Enter Message:", 12).place(x=10, y=35)
    messg_entry = tk.Text(input_frame, width=60, height=10, bg=COL_THIRD, fg=COL_TEXT).place(x=10, y=60)

    opton_frame = makeFrame(root).place(relwidth=1, relheight=0.15, relx=0, rely=0.464)
    #
    encry_label = makeLabel(opton_frame, "Encryption Method:", 12).place(x=10, y=243)
    options = StringVar(opton_frame)
    options.set(ENC_TYPES[0]) #default value
    dropD_opMen = OptionMenu(opton_frame, options, *ENC_TYPES)
    dropD_opMen.config(width=18, bg=COL_THIRD, fg=COL_TEXT)
    dropD_opMen.place(x=150, y=240)
    #
    title_label = makeLabel(opton_frame, "Output Title Name:", 12).place(x=10, y=278)
    title_entry = tk.Entry(opton_frame, width=25, bg=COL_THIRD, fg=COL_TEXT).place(x=150, y=280)



    
if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(width=False, height=False)
    root.title(APP_TITLE)
    root.iconbitmap(APP_ICON)
    canvas = tk.Canvas(root, height=WINDOW_H, width=WINDOW_W, bg=COL_SECND).pack()
    createInterface()
