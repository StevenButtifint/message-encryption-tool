from tkinter import Tk, filedialog, Text, Listbox, filedialog, Entry, OptionMenu, StringVar, Frame, Label, Text, Canvas, DISABLED, NORMAL, Button

from res.methods.AES_128_symmetric_key import AES_128_symmetric_key
from res.methods.AES_256_custom_key import AES_256_custom_key
from res.methods.RSA_512_asymmetric_key import RSA_512_asymmetric_key


class messageEncryptionWindow:
    def __init__(self, parent):
        self.window = parent
        self.window.geometry("500x500")
        self.window.title("Message Encryption Tool")
        self.window.iconbitmap("res/icons/icon.ico")
        self.window.resizable(width=False, height=False)

        self.col_prime = "cyan4"
        self.col_second = "cyan2"
        self.col_third = "DarkSlateGray3"
        self.col_text = "black"

        self.method_labels = ["AES-128 Symmetric-Key", "AES-256 Custom-Key", "RSA-512 Asymmetric-Key"]
        self.method_classes = [AES_128_symmetric_key, AES_256_custom_key, RSA_512_asymmetric_key]

        self.crypto_types = ["Encrypt", "Decrypt"]

        self.custom_input_frame = None
        
        canvas = Canvas(self.window, height=500, width=500, bg=self.col_second).pack()
        self._makeHomePage()

        
    def _makeHomePage(self):
        title_frm = self._makeFrame(self.window).place(relwidth=1, relheight=0.06, relx=0, rely=0)
        title_lbl = self._makeLabel(title_frm, "Message Encrypter", 14).place(x=170, y=2)
        
        input_frm = self._makeFrame(self.window).place(relwidth=1, relheight=0.4, relx=0, rely=0.062)
        messg_lbl = self._makeLabel(input_frm, "Enter Message:", 12).place(x=10, y=35)
        messg_ent = Text(input_frm, width=60, height=10, bg=self.col_third, fg=self.col_text)
        messg_ent.place(x=10, y=60)

        opton_frm = self._makeFrame(self.window).place(relwidth=1, relheight=0.15, relx=0, rely=0.464)
        #
        encry_lbl = self._makeLabel(opton_frm, "Encryption Method:", 12).place(x=10, y=243)
        crypto_methods = StringVar(opton_frm)
        crypto_methods.set(self.method_labels[0]) #default value
        dropD_opM = OptionMenu(opton_frm, crypto_methods, *self.method_labels,
                               command= lambda x=None: self._makeCustomInput(messg_ent.get("1.0","end"), operation_type.get(), crypto_methods.get()))
        dropD_opM.config(width=21, bg=self.col_third, fg=self.col_text)
        dropD_opM.place(x=150, y=240)
        #
        type_lbl = self._makeLabel(opton_frm, "Type:", 12).place(x=330, y=243)
        operation_type = StringVar(opton_frm)
        operation_type.set("> Select <") #default value
        dropD_opM = OptionMenu(opton_frm, operation_type, *self.crypto_types,
                              command= lambda x=None: self._makeCustomInput(messg_ent.get("1.0","end"), operation_type.get(), crypto_methods.get()))
        dropD_opM.config(width=11, bg=self.col_third, fg=self.col_text)
        dropD_opM.place(x=380, y=240)
        #
        outpt_frm = self._makeFrame(self.window).place(relwidth=1, relheight=0.4, relx=0, rely=0.616)
        outpt_lbl = self._makeLabel(outpt_frm, "OUTPUT", 12).place(x=230, y=310)
        outpt_txt = Text(outpt_frm, width=60, height=10, bg=self.col_third, fg=self.col_text)
        outpt_txt.configure(state=DISABLED)
        outpt_txt.place(x=10, y=330)





def formatEncOutput(ciphertext, key):
    return "Key:\n" + str(key)[2:-1] +"\n\n" + "Message:\n" + str(ciphertext)[2:-1]
    

def setOutputText(outpt_txt, content):
    outpt_txt.configure(state=NORMAL)
    outpt_txt.delete('1.0', tk.END)
    outpt_txt.insert("1.0", content)
    outpt_txt.configure(state=DISABLED)
    

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
    
if __name__ == "__main__":
    root = Tk()
    messageEncryptionWindow(root)

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

    

