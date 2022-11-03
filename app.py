from constants import *
from interface import *
import tkinter as tk

from cryptographic_methods.caesar_cipher import CaesarCipher
from cryptographic_methods.vernam_cipher import VernamCipher


class messageEncrypter:
    def __init__(self, parent):
        self.window = parent
        self.window.geometry(RESOLUTION)
        self.window.title(TITLE)
        self.window.iconbitmap(ICON_DIR)
        self.window.resizable(width=False, height=False)
        
        makeCanvas(self.window, 500, 500, COLOUR_SECOND)
        titleFrame = makeFrame(self.window, 1, 0.06, 0, 0, COLOUR_PRIME, "nw")
        self.operation = makeOptionMenu(titleFrame, OPERATIONS, lambda x=None: self._updateOptions(), 8, 2, 2)
        makeLabel(titleFrame, "message using", 12, 0.32, 0.5, "center", COLOUR_PRIME)
        self.method = makeOptionMenu(titleFrame, CRYPTO_METHODS, lambda x=None: self._updateOptions(), 25, 230, 2)
        makeLabel(titleFrame, "|", 16, 0.87, 0.5, "center", COLOUR_PRIME)
        makeButton(titleFrame, "Help", lambda x=None: self._makeHomeContent(), 5, 0.94, 0.5)
        self._makeHomeContent()


    def _makeHomeContent(self):
        try: self.shownOptions.destroy()
        except: pass
        self.shownOptions = makeFrame(self.window, 0.95, 0.95, 0.5, 0.55, COLOUR_SECOND,"center")
        makeLabel(self.shownOptions, WELCOME_TITLE, 16, 0.5, 0.1, "center", COLOUR_SECOND)
        makeLabel(self.shownOptions, WELCOME_INFO, 11, 0.5, 0.7, "center", COLOUR_SECOND)
        canvas, self.imageBG = placeImage(self.shownOptions, "res/icons/icon_large.png", 200, 200, 125, 100)       
        makeLabel(self.shownOptions, "Steven B. 2022", 8, 0.5, 0.95, "center", COLOUR_SECOND)


    def _updateOptions(self):
        self.shownOptions.destroy()

        interfaceDict = {CRYPTO_METHODS[0]: self._makeCaesarOptions,
                         CRYPTO_METHODS[1]: self._makeVernamOptions}

        interfaceDict[self.method.get()]()
        
        print(self.operation.get(), self.method.get())        
        print(METHOD_DICT[self.method.get()])

        
    def _makeCaesarOptions(self):
        self.shownOptions = makeFrame(self.window, 1, 0.95, 0.5, 0.55, COLOUR_SECOND, "center")

        makeLabel(self.shownOptions, "Key:", 12, 0.15, 0.1, "center", COLOUR_SECOND)
        self.keyScale = makeScale(self.shownOptions, 1, 25, 0.5, 0.13, 20, 300, COLOUR_THIRD, COLOUR_TEXT)
        self.messageEntry = makeTextbox(self.shownOptions, 60, 6, COLOUR_THIRD, COLOUR_TEXT, 0.5,0.4) 
        makeLabel(self.shownOptions, "Output:", 12, 0.12, 0.64, "center", COLOUR_SECOND)
        self.messageOutput = makeTextbox(self.shownOptions, 60, 6, COLOUR_THIRD, COLOUR_TEXT, 0.5,0.78)

        if self.operation.get() == OPERATIONS[0]:
            # Encrypt options
            makeLabel(self.shownOptions, "Message:", 12, 0.11, 0.26, "center", COLOUR_SECOND)
            makeButton(self.shownOptions, "Encrypt", lambda x=None: self._processCaesar(), 12, 0.5, 0.56)
            self.messageOutput.insert(tk.END, "Your ciphertext will be shown here...")

        else:
            # Decrypt options
            makeLabel(self.shownOptions, "Ciphertext:", 12, 0.11, 0.26, "center", COLOUR_SECOND)
            makeButton(self.shownOptions, "Decrypt", lambda x=None: self._processCaesar(), 12, 0.5, 0.56)
            self.messageOutput.insert(tk.END, "The message will be shown here...")

        self.messageOutput.config(state=tk.DISABLED)
            

    def _processCaesar(self):
        key = self.keyScale.get()
        message = self.messageEntry.get("1.0",tk.END)
        caesarCipher = CaesarCipher(key)
        
        if self.operation.get() == "Encrypt":
            output = caesarCipher.encrypt(message)
        else:
            output = caesarCipher.decrypt(message)

        self._updateReadOnlyBox(self.messageOutput, output)
        

    @staticmethod
    def _updateReadOnlyBox(textBox, content):
        textBox.config(state=tk.NORMAL)
        textBox.delete("1.0", tk.END)
        textBox.insert(tk.END, content)
        textBox.config(state=tk.DISABLED)
        

    def _makeVernamOptions(self):
        self.shownOptions = makeFrame(self.window, 1, 0.95, 0.5, 0.55, COLOUR_SECOND, "center")

        makeLabel(self.shownOptions, "Key:", 12, 0.15, 0.1, "center", COLOUR_SECOND)
        self.keyEntry = makeTextbox(self.shownOptions, 30, 1, COLOUR_THIRD, COLOUR_TEXT, 0.45,0.1) 
        self.messageEntry = makeTextbox(self.shownOptions, 60, 6, COLOUR_THIRD, COLOUR_TEXT, 0.5,0.4) 
        makeLabel(self.shownOptions, "Output:", 12, 0.12, 0.64, "center", COLOUR_SECOND)
        self.messageOutput = makeTextbox(self.shownOptions, 60, 6, COLOUR_THIRD, COLOUR_TEXT, 0.5,0.78)

        if self.operation.get() == OPERATIONS[0]:
            #encrypt options
            makeLabel(self.shownOptions, "Message:", 12, 0.11, 0.26, "center", COLOUR_SECOND)
            makeButton(self.shownOptions, "Encrypt", lambda x=None: self._processVernam(), 12, 0.5, 0.56)
            self.messageOutput.insert(tk.END, "Your ciphertext will be shown here...")

        else:
            #decrypt options
            makeLabel(self.shownOptions, "Ciphertext:", 12, 0.11, 0.26, "center", COLOUR_SECOND)
            makeButton(self.shownOptions, "Decrypt", lambda x=None: self._processVernam(), 12, 0.5, 0.56)
            self.messageOutput.insert(tk.END, "The message will be shown here...")


        


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

