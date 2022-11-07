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
        self.messageOutput.config(state=tk.DISABLED)

    def _processVernam(self):
        key = self.keyEntry.get("1.0",tk.END)
        message = self.messageEntry.get("1.0",tk.END)[:-1]
        vernamCipher = VernamCipher(key)
        
        if self.operation.get() == "Encrypt":
            output = vernamCipher.encrypt(message)
        else:
            output = vernamCipher.decrypt(message)

        self._updateReadOnlyBox(self.messageOutput, output)
        

    def _makeAES128(self):
        self.shownOptions = makeFrame(self.window, 1, 0.95, 0.5, 0.55, COLOUR_SECOND, "center")

        makeLabel(self.shownOptions, "Output:", 12, 0.12, 0.64, "center", COLOUR_SECOND)
        self.messageOutput = makeTextbox(self.shownOptions, 60, 6, COLOUR_THIRD, COLOUR_TEXT, 0.5,0.78)

        if self.operation.get() == OPERATIONS[0]:
            # Encrypt options
            makeLabel(self.shownOptions, "Message:", 12, 0.11, 0.06, "center", COLOUR_SECOND)
            self.messageEntry = makeTextbox(self.shownOptions, 60, 6, COLOUR_THIRD, COLOUR_TEXT, 0.5,0.2)
            makeButton(self.shownOptions, "Encrypt", lambda x=None: self._processCaesar(), 12, 0.5, 0.36)
            makeLabel(self.shownOptions, "Key used:", 12, 0.12, 0.44, "center", COLOUR_SECOND)
            self.key = makeTextbox(self.shownOptions, 60, 3, COLOUR_THIRD, COLOUR_TEXT, 0.5,0.53)
            self.key.insert(tk.END, "The generated key used will be shown here...")
            self.key.config(state=tk.DISABLED)
            self.messageOutput.insert(tk.END, "Your ciphertext will be shown here...")

        else:
            # Decrypt options
            makeLabel(self.shownOptions, "Key used:", 12, 0.12, 0.06, "center", COLOUR_SECOND)
            self.key = makeTextbox(self.shownOptions, 60, 3, COLOUR_THIRD, COLOUR_TEXT, 0.5,0.14)
            makeLabel(self.shownOptions, "Ciphertext:", 12, 0.11, 0.26, "center", COLOUR_SECOND)
            self.messageEntry = makeTextbox(self.shownOptions, 60, 6, COLOUR_THIRD, COLOUR_TEXT, 0.5,0.4)
            makeButton(self.shownOptions, "Decrypt", lambda x=None: self._processCaesar(), 12, 0.5, 0.55)
            self.messageOutput.insert(tk.END, "The message will be shown here...")

        
        self.messageOutput.config(state=tk.DISABLED)
        


                                # label, font size, x, y, entry width, x, y
        
                                # label, font size, x, y, entry width, x, y

        
            #encrypt
            
            #decrypt





        
                




    
if __name__ == "__main__":
    root = tk.Tk()
    messageEncrypter(root)

