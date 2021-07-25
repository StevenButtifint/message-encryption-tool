import tkinter as tk
from tkinter import filedialog, Text, Listbox, filedialog, Entry, OptionMenu, StringVar

from cryptography.fernet import Fernet

APP_TITLE   = "Message Encryption Tool"
APP_ICON    = "icon.ico"

WINDOW_H    = 500
WINDOW_W    = 500

COL_PRIME   = "cyan4"
COL_SECND   = "cyan2"
COL_THIRD   = "DarkSlateGray3"
COL_TEXT    = "white"

ENC_TYPES   = ["option1", "option2", "option3"]


def encryptMessage(message, title, enc_type):
    print("message:", message)
    print("title:", title)
    print("enc_type:", enc_type)


def makeFrame(root):
    frame = tk.Frame(root, bg=COL_PRIME)
    return frame


def makeLabel(frame, text, font_size):
    return tk.Label(frame, text=text, bg=COL_PRIME, fg=COL_SECND, font=(COL_SECND,font_size))
    

def createInterface():
    title_frm = makeFrame(root).place(relwidth=1, relheight=0.06, relx=0, rely=0)
    title_lbl = makeLabel(title_frm, "Message Encrypter", 14).place(x=170, y=2)
    
    input_frm = makeFrame(root).place(relwidth=1, relheight=0.4, relx=0, rely=0.062)
    messg_lbl = makeLabel(input_frm, "Enter Message:", 12).place(x=10, y=35)
    messg_ent = tk.Text(input_frm, width=60, height=10, bg=COL_THIRD, fg=COL_TEXT)
    messg_ent.place(x=10, y=60)

    opton_frm = makeFrame(root).place(relwidth=1, relheight=0.15, relx=0, rely=0.464)
    #
    encry_lbl = makeLabel(opton_frm, "Encryption Method:", 12).place(x=10, y=243)
    options = StringVar(opton_frm)
    options.set(ENC_TYPES[0]) #default value
    dropD_opM = OptionMenu(opton_frm, options, *ENC_TYPES)
    dropD_opM.config(width=18, bg=COL_THIRD, fg=COL_TEXT)
    dropD_opM.place(x=150, y=240)
    #
    title_lbl = makeLabel(opton_frm, "Output Title Name:", 12).place(x=10, y=278)
    title_ent = tk.Entry(opton_frm, width=25, bg=COL_THIRD, fg=COL_TEXT)
    title_ent.place(x=150, y=280)

    proce_frm = makeFrame(root).place(relwidth=1, relheight=0.15, relx=0, rely=0.616)
    proce_btn = tk.Button(proce_frm, text="PROCESS", width=10, bg=COL_THIRD, fg=COL_TEXT,
                          command= lambda: encryptMessage(messg_ent.get("1.0","end"), title_ent.get(), options.get()))
    proce_btn.place(x=200, y=350)

    
if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(width=False, height=False)
    root.title(APP_TITLE)
    root.iconbitmap(APP_ICON)
    canvas = tk.Canvas(root, height=WINDOW_H, width=WINDOW_W, bg=COL_SECND).pack()
    createInterface()
