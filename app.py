import tkinter as tk
from tkinter import filedialog, Text, Listbox, filedialog, Entry, OptionMenu, StringVar


from res.methods.AES_128_symmetric_key import AES_128_symmetric_key
from res.methods.AES_256_custom_key import AES_256_custom_key
from res.methods.RSA_512_asymmetric_key import RSA_512_asymmetric_key


APP_TITLE   = "Message Encryption Tool"
APP_ICON    = "res/icons/icon.ico"

WINDOW_H    = 500
WINDOW_W    = 500

COL_PRIME   = "cyan4"
COL_SECND   = "cyan2"
COL_THIRD   = "DarkSlateGray3"
COL_TEXT    = "black"

ENC_TYPES   = ["AES-128 Symmetric-Key", "AES-256 Custom-Key", "RSA-512 Asymmetric-Key"]
CRYPTO_TYPE = ["Encrypt", "Decrypt"]



def formatEncOutput(ciphertext, key):
    return "Key:\n" + str(key)[2:-1] +"\n\n" + "Message:\n" + str(ciphertext)[2:-1]
    

def setOutputText(outpt_txt, content):
    outpt_txt.configure(state=tk.NORMAL)
    outpt_txt.delete('1.0', tk.END)
    outpt_txt.insert("1.0", content)
    outpt_txt.configure(state=tk.DISABLED)
    

def processMessage(message, key, crypto_type, enc_option, outpt_txt):

    output = ""
    print(crypto_type + "ing with " + enc_option)

    if enc_option == ENC_TYPES[0]:
        method = AES_128_symmetric_key(key)
        if crypto_type == CRYPTO_TYPE[0]:
            ciphertext, key = method.encrypt(message)
            output = formatEncOutput(ciphertext, key)
        else:
            plaintext = method.decrypt(message)
            output = "Message:\n" + str(plaintext)
            
    elif enc_option == ENC_TYPES[1]:
        method = AES_256_custom_key(key)
        if crypto_type == CRYPTO_TYPE[0]:
            ciphertext = method.encrypt(message)
            output = ciphertext
        else:
            plaintext = method.decrypt(message)
            output = plaintext

    elif enc_option == ENC_TYPES[2]:
        method = RSA_512_asymmetric_key(key)
        if crypto_type == CRYPTO_TYPE[0]:
            ciphertext, publicKey, privateKey = method.encrypt(message)
            print("working types")
            print(type(privateKey))
            print(type(ciphertext))
            #plaintext = method.decrypt(ciphertext, privateKey)
            output = "PublicKey:\n" + str(publicKey) +"\n\n" + "PrivateKey:\n" + str(privateKey) +"\n\n" + "Message:\n" + str(ciphertext)[2:-1]# + "\ndectypted again:\n" + plaintext


        else:
            
            plaintext = method.decrypt(message, key)#SK
            output = "Message:\n" + str(plaintext)

            
    setOutputText(outpt_txt, output)
    

def makeFrame(root):
    frame = tk.Frame(root, bg=COL_PRIME)
    return frame


def makeLabel(frame, text, font_size):
    return tk.Label(frame, text=text, bg=COL_PRIME, fg=COL_SECND, font=(COL_SECND,font_size))
    

def makeCustomInput(operation, messg_ent, enc_option, outpt_txt):
    global key_lbl, key_ent, temp_frm

    try:
        temp_frm.destroy()
    except:
        pass
    
    temp_frm = makeFrame(root).place(relwidth=1, relheight=0.075, relx=0, rely=0.539)

    if enc_option.get() == ENC_TYPES[0]:#aes
        if (operation.get() == CRYPTO_TYPE[1]):
            key_lbl = makeLabel(temp_frm, "Input Key:", 12).place(x=10, y=278)
            key_ent = tk.Entry(temp_frm, width=37, bg=COL_THIRD, fg=COL_TEXT)
            key_ent.place(x=90, y=280)
        else:
            key_lbl = makeLabel(temp_frm, "Reuse previous key:", 12).place(x=10, y=278)
            key_ent = tk.Entry(temp_frm, width=26, bg=COL_THIRD, fg=COL_TEXT)
            key_ent.place(x=160, y=280)

    if enc_option.get() == ENC_TYPES[1]:#aes custom key
        if (operation.get() == CRYPTO_TYPE[1]):
            key_lbl = makeLabel(temp_frm, "Enter Custom Key String:", 12).place(x=10, y=278)
            key_ent = tk.Entry(temp_frm, width=21, bg=COL_THIRD, fg=COL_TEXT)
            key_ent.place(x=190, y=280)
        else:
            key_lbl = makeLabel(temp_frm, "Enter Custom Key String:", 12).place(x=10, y=278)
            key_ent = tk.Entry(temp_frm, width=21, bg=COL_THIRD, fg=COL_TEXT)
            key_ent.place(x=190, y=280)
            
    if enc_option.get() == ENC_TYPES[2]:#rsa
        if (operation.get() == CRYPTO_TYPE[1]):
            key_lbl = makeLabel(temp_frm, "Input Key:", 12).place(x=10, y=278)
            key_ent = tk.Entry(temp_frm, width=37, bg=COL_THIRD, fg=COL_TEXT)
            key_ent.place(x=90, y=280)
        else:
            key_lbl = makeLabel(temp_frm, "Reuse previous key:", 12).place(x=10, y=278)
            key_ent = tk.Entry(temp_frm, width=26, bg=COL_THIRD, fg=COL_TEXT)
            key_ent.place(x=160, y=280)
        


    proce_btn = tk.Button(temp_frm, text="PROCESS", width=14, bg=COL_THIRD, fg=COL_TEXT,
                          command= lambda: processMessage(messg_ent.get("1.0","end"), key_ent.get(), operation.get(), enc_option.get(), outpt_txt))
    proce_btn.place(x=380, y=280)

    
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
    enc_methods = StringVar(opton_frm)
    enc_methods.set(ENC_TYPES[0]) #default value
    dropD_opM = OptionMenu(opton_frm, enc_methods, *ENC_TYPES)
    dropD_opM.config(width=21, bg=COL_THIRD, fg=COL_TEXT)
    dropD_opM.place(x=150, y=240)
    #
    type_lbl = makeLabel(opton_frm, "Type:", 12).place(x=330, y=243)
    operation_type = StringVar(opton_frm)
    operation_type.set("> Select <") #default value
    dropD_opM = OptionMenu(opton_frm, operation_type, *CRYPTO_TYPE,
                          command= lambda x=None: makeCustomInput(operation_type, messg_ent, enc_methods, outpt_txt))
    dropD_opM.config(width=11, bg=COL_THIRD, fg=COL_TEXT)
    dropD_opM.place(x=380, y=240)
    #
    outpt_frm = makeFrame(root).place(relwidth=1, relheight=0.4, relx=0, rely=0.616)
    outpt_lbl = makeLabel(outpt_frm, "OUTPUT", 12).place(x=230, y=310)
    outpt_txt = tk.Text(outpt_frm, width=60, height=10, bg=COL_THIRD, fg=COL_TEXT)
    outpt_txt.configure(state=tk.DISABLED)
    outpt_txt.place(x=10, y=330)

    
if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(width=False, height=False)
    root.title(APP_TITLE)
    root.iconbitmap(APP_ICON)
    canvas = tk.Canvas(root, height=WINDOW_H, width=WINDOW_W, bg=COL_SECND).pack()
    createInterface()
