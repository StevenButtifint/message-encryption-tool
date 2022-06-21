from constants import *
from interface import *



class messageEncrypter:
    def __init__(self, parent):
        self.window = parent
        self.window.geometry(RESOLUTION)
        self.window.title(TITLE)
        self.window.iconbitmap(ICON_DIR)
        self.window.resizable(width=False, height=False)
        
        makeCanvas(self.window, 500, 500, COLOUR_SECOND)
        titleFrame = makeFrame(self.window, 1, 0.06, 0, 0, COLOUR_PRIME, "nw")
        self.shownOptions = self._makeHomeContent()
        self.operation = makeOptionMenu(titleFrame, OPERATIONS, lambda x=None: self._updateOptions(), 8, 2, 2)
        makeLabel(titleFrame, "message using", 12, 110, 2)
        self.method = makeOptionMenu(titleFrame, CRYPTO_METHODS, lambda x=None: self._updateOptions(), 25, 230, 2)
        makeLabel(titleFrame, "|", 16, 430, 0)
        makeButton(titleFrame, "Help", lambda x=None: self._makeHomeContent(), 5, 450, 2)

    def _makeHomeContent(self):
        try: self.shownOptions.destroy()
        except: pass
        
        self.shownOptions = makeFrame(self.window, 0.9, 0.8, 0.5, 0.5, "green","center")
        return self.shownOptions



        self.method_labels = ["Caesar Cipher", "Vernam Cipher", "AES-128 Symmetric-Key", "AES-256 Custom-Key", "RSA-512 Asymmetric-Key"]
        self.method_classes = [CaesarCipher, VernamCipher, AES_128_symmetric_key, AES_256_custom_key, RSA_512_asymmetric_key]
        self.crypto_types = ["Encrypt", "Decrypt"]
        self.custom_input_frame = None
        canvas = Canvas(self.window, height=500, width=500, bg=COLOUR_SECOND).pack()
        self._makeHomePage()

        
    def _makeHomePage(self):
        title_frm = self._makeFrame(self.window).place(relwidth=1, relheight=0.06, relx=0, rely=0)
        self._makeLabel(title_frm, "Message Encrypter", 14, 170, 2)
        
        input_frm = self._makeFrame(self.window).place(relwidth=1, relheight=0.4, relx=0, rely=0.062)
        self._makeLabel(input_frm, "Enter Message:", 12, 10, 35)
        messg_ent = Text(input_frm, width=60, height=10, bg=COLOUR_THIRD, fg=COLOUR_TEXT)
        messg_ent.place(x=10, y=60)

        opton_frm = self._makeFrame(self.window).place(relwidth=1, relheight=0.15, relx=0, rely=0.464)
        
        self._makeLabel(opton_frm, "Encryption Method:", 12, 10, 243)
        crypto_methods = StringVar(opton_frm)
        crypto_methods.set(self.method_labels[0]) #default value
        dropD_opM = OptionMenu(opton_frm, crypto_methods, *self.method_labels,
                               command= lambda x=None: self._makeCustomInput(messg_ent.get("1.0","end"), operation_type.get(), crypto_methods.get()))
        dropD_opM.config(width=21, bg=COLOUR_THIRD, fg=COLOUR_TEXT)
        dropD_opM.place(x=150, y=240)
        
        self._makeLabel(opton_frm, "Type:", 12, 330, 243)
        operation_type = StringVar(opton_frm)
        operation_type.set("> Select <") #default value
        dropD_opM = OptionMenu(opton_frm, operation_type, *self.crypto_types,
                              command= lambda x=None: self._makeCustomInput(messg_ent.get("1.0","end"), operation_type.get(), crypto_methods.get()))
        dropD_opM.config(width=11, bg=COLOUR_THIRD, fg=COLOUR_TEXT)
        dropD_opM.place(x=380, y=240)
        
        outpt_frm = self._makeFrame(self.window).place(relwidth=1, relheight=0.4, relx=0, rely=0.616)
        self._makeLabel(outpt_frm, "OUTPUT", 12, 230, 310)
        self.output_box = Text(outpt_frm, width=60, height=10, bg=COLOUR_THIRD, fg=COLOUR_TEXT)
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
            self._makeLabel(self.custom_input_frame, enc_content[method_idx][0], enc_content[method_idx][1], enc_content[method_idx][2], enc_content[method_idx][3])
            key_ent = Entry(self.custom_input_frame, width=enc_content[method_idx][4], bg=COLOUR_THIRD, fg=COLOUR_TEXT)
            key_ent.place(x=enc_content[method_idx][5], y=enc_content[method_idx][6])
            
        else:
            #decrypt
            self._makeLabel(self.custom_input_frame, dec_content[method_idx][0], dec_content[method_idx][1], dec_content[method_idx][2], dec_content[method_idx][3])
            key_ent = Entry(self.custom_input_frame, width=dec_content[method_idx][4], bg=COLOUR_THIRD, fg=COLOUR_TEXT)
            key_ent.place(x=dec_content[method_idx][5], y=dec_content[method_idx][6])

        process_button = Button(self.custom_input_frame, text="PROCESS", width=14, bg=COLOUR_THIRD, fg=COLOUR_TEXT,
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




    
if __name__ == "__main__":
    root = tk.Tk()
    messageEncrypter(root)

