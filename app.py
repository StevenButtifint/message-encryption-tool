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

ENC_TYPES   = ["AES", "option2", "option3"]
ENC_OPTNS   = ["Encrypt", "Decrypt"]

def encryptAES(message):
    key = Fernet.generate_key()
    f = Fernet(key)
    msg_encoded = message.encode()
    msg_encrypt = f.encrypt(msg_encoded)
    return msg_encrypt, key


def decryptAES(msg_encrypted, key):
    f = Fernet(key)
    msg_encoded = f.decrypt(msg_encrypted)
    msg_origin = msg_encoded.decode()
    return msg_origin
    
def encryptMessage(message, title, enc_type):
    print("message:", message)
    print("title:", title)
    print("enc_type:", enc_type)

    enc_functions = [encryptAES, "", ""]

    
    enc_func = enc_functions[ENC_TYPES.index(enc_type)]

    enc_message, key = enc_func(message)

    print(enc_message)
    print(key)

    print(decryptAES(enc_message, key))


def makeFrame(root):
    frame = tk.Frame(root, bg=COL_PRIME)
    return frame


def makeLabel(frame, text, font_size):
    return tk.Label(frame, text=text, bg=COL_PRIME, fg=COL_SECND, font=(COL_SECND,font_size))
    

def makeCustomInput(operation):
    global title_lbl, title_ent, temp_frm

    try:
        temp_frm.destroy()
    except:
        pass
    
    temp_frm = makeFrame(root).place(relwidth=1, relheight=0.075, relx=0, rely=0.539)

    if (operation == "Encrypt"):
        title_lbl = makeLabel(temp_frm, "Output Title Name:", 12).place(x=10, y=278)
        title_ent = tk.Entry(temp_frm, width=25, bg=COL_THIRD, fg=COL_TEXT)
        title_ent.place(x=150, y=280)
        print("Encrypt")
    else:
        title_lbl = makeLabel(temp_frm, "Input Key:", 12).place(x=10, y=278)
        title_ent = tk.Entry(temp_frm, width=35, bg=COL_THIRD, fg=COL_TEXT)
        title_ent.place(x=90, y=280)
        print("Decrypt")

    
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
    type_lbl = makeLabel(opton_frm, "Type:", 12).place(x=320, y=243)
    options = StringVar(opton_frm)
    options.set("> Select <") #default value
    dropD_opM = OptionMenu(opton_frm, options, *ENC_OPTNS,
                          command= lambda x=None: makeCustomInput(options.get()))
    dropD_opM.config(width=11, bg=COL_THIRD, fg=COL_TEXT)
    dropD_opM.place(x=380, y=240)
    #



    proce_frm = makeFrame(root).place(relwidth=1, relheight=0.15, relx=0, rely=0.616)
    proce_btn = tk.Button(proce_frm, text="PROCESS", width=10, bg=COL_THIRD, fg=COL_TEXT,
                          command= lambda: encryptMessage(messg_ent.get("1.0","end"), title_ent.get(), options.get()))
    proce_btn.place(x=200, y=350)
    #need unwritable textbox for key output

    
if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(width=False, height=False)
    root.title(APP_TITLE)
    root.iconbitmap(APP_ICON)
    canvas = tk.Canvas(root, height=WINDOW_H, width=WINDOW_W, bg=COL_SECND).pack()
    createInterface()
