from tkinter import Tk, filedialog, Text, Listbox, filedialog, Entry, OptionMenu, StringVar, Frame, Label, Text, Canvas, DISABLED, NORMAL, Button, END

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
        
        encry_lbl = self._makeLabel(opton_frm, "Encryption Method:", 12).place(x=10, y=243)
        crypto_methods = StringVar(opton_frm)
        crypto_methods.set(self.method_labels[0]) #default value
        dropD_opM = OptionMenu(opton_frm, crypto_methods, *self.method_labels,
                               command= lambda x=None: self._makeCustomInput(messg_ent.get("1.0","end"), operation_type.get(), crypto_methods.get()))
        dropD_opM.config(width=21, bg=self.col_third, fg=self.col_text)
        dropD_opM.place(x=150, y=240)
        
        type_lbl = self._makeLabel(opton_frm, "Type:", 12).place(x=330, y=243)
        operation_type = StringVar(opton_frm)
        operation_type.set("> Select <") #default value
        dropD_opM = OptionMenu(opton_frm, operation_type, *self.crypto_types,
                              command= lambda x=None: self._makeCustomInput(messg_ent.get("1.0","end"), operation_type.get(), crypto_methods.get()))
        dropD_opM.config(width=11, bg=self.col_third, fg=self.col_text)
        dropD_opM.place(x=380, y=240)
        
        outpt_frm = self._makeFrame(self.window).place(relwidth=1, relheight=0.4, relx=0, rely=0.616)
        outpt_lbl = self._makeLabel(outpt_frm, "OUTPUT", 12).place(x=230, y=310)
        self.output_box = Text(outpt_frm, width=60, height=10, bg=self.col_third, fg=self.col_text)
        self.output_box.configure(state=DISABLED)
        self.output_box.place(x=10, y=330)


    def _makeCustomInput(self, input_string, operation_type, crypto_method):

        try:
            self.custom_input_frame.destroy()
        except:
            pass
        self.custom_input_frame = self._makeFrame(self.window).place(relwidth=1, relheight=0.075, relx=0, rely=0.539)

                                # label, font size, x, y, entry width, x, y
        enc_content = [["Shift Amount:", 12, 10, 278, 35, 110, 280],
                       ["Key (word):", 12, 10, 278, 35, 110, 280],
                       ["Input Key:", 12, 10, 278, 37, 90, 280],
                       ["Enter Custom Key String:", 12, 10, 278, 21, 190, 280],
                       ["Input Key:", 12, 10, 278, 37, 90, 280]]
        
                                # label, font size, x, y, entry width, x, y
        dec_content = [["Shift Amount:", 12, 10, 278, 35, 110, 280],
                       ["Key (word):", 12, 10, 278, 35, 110, 280],
                       ["Reuse previous key:", 12, 10, 278, 26, 160, 280],
                       ["Enter Custom Key String:", 12, 10, 278, 21, 190, 280],
                       ["Reuse previous key:", 12, 10, 278, 26, 160, 280]]

        method_idx = self.method_labels.index(crypto_method)
        
        if operation_type == self.crypto_types[0]:
            #encrypt
            self._makeLabel(self.custom_input_frame, enc_content[method_idx][0], enc_content[method_idx][1]).place(x=enc_content[method_idx][2], y=enc_content[method_idx][3])
            key_ent = Entry(self.custom_input_frame, width=enc_content[method_idx][4], bg=self.col_third, fg=self.col_text)
            key_ent.place(x=enc_content[method_idx][5], y=enc_content[method_idx][6])
            
        else:
            #decrypt
            self._makeLabel(self.custom_input_frame, dec_content[method_idx][0], dec_content[method_idx][1]).place(x=dec_content[method_idx][2], y=dec_content[method_idx][3])
            key_ent = Entry(self.custom_input_frame, width=dec_content[method_idx][4], bg=self.col_third, fg=self.col_text)
            key_ent.place(x=dec_content[method_idx][5], y=dec_content[method_idx][6])

        process_button = Button(self.custom_input_frame, text="PROCESS", width=14, bg=self.col_third, fg=self.col_text,
                              command= lambda: self.processMessage(input_string, key_ent.get(), method_idx, operation_type))
        process_button.place(x=380, y=280)


    def processMessage(self, input_string, key, operation_index, crypto_type):

        output = ""
        operation_method = self.method_classes[operation_index]
        
        print(crypto_type + "ing with " + operation_method.__name__)

        method = operation_method(key)
        
        if crypto_type == self.crypto_types[0]:
            output = method.sanitizeEncrypt(input_string)
        else:
            output = method.sanitizeDecrypt(input_string)
                
        self.setOutputText(self.output_box, output)

    @staticmethod
    def setOutputText(text_box, content):
        text_box.configure(state=NORMAL)
        text_box.delete('1.0', END)
        text_box.insert("1.0", content)
        text_box.configure(state=DISABLED)


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
        
    def _makeLabel(self, frame, text, font_size):
        return Label(frame, text=text, bg=self.col_prime, fg=self.col_second, font=(self.col_second,font_size))


    proce_btn = tk.Button(temp_frm, text="PROCESS", width=14, bg=COL_THIRD, fg=COL_TEXT,
                          command= lambda: processMessage(messg_ent.get("1.0","end"), key_ent.get(), operation.get(), enc_option.get(), outpt_txt))
    proce_btn.place(x=380, y=280)

    
if __name__ == "__main__":
    root = Tk()
    messageEncryptionWindow(root)

