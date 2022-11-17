from interface import *

from cryptographic_methods.caesar_cipher import CaesarCipher
from cryptographic_methods.vernam_cipher import VernamCipher
from cryptographic_methods.AES_128 import AES_128
from cryptographic_methods.AES_256_custom_key import AES_256_custom_key


class MessageEncrypter:
    def __init__(self, parent):
        self.window = parent
        self.window.geometry(RESOLUTION)
        self.window.title(TITLE)
        self.window.iconbitmap(ICON_DIR)
        self.window.resizable(width=False, height=False)

        self.interface_dict = {CRYPTO_METHODS[0]: self._make_caesar_options,
                               CRYPTO_METHODS[1]: self._make_vernam_options,
                               CRYPTO_METHODS[2]: self._make_AES,
                               CRYPTO_METHODS[3]: self._make_AES_custom}
        
        makeCanvas(self.window, 500, 500, COLOUR_SECOND)
        title_frame = makeFrame(self.window, 1, 0.06, 0, 0, COLOUR_PRIME, "nw")
        self.operation = makeOptionMenu(title_frame, OPERATIONS, lambda x=None: self._update_options(), 8, 2, 2)
        makeLabel(title_frame, "message using", 12, 0.32, 0.5, "center", COLOUR_PRIME)
        self.method = makeOptionMenu(title_frame, CRYPTO_METHODS, lambda x=None: self._update_options(), 25, 230, 2)
        makeLabel(title_frame, "|", 16, 0.87, 0.5, "center", COLOUR_PRIME)
        makeButton(title_frame, "Help", lambda x=None: self._make_home_content(), 5, 0.94, 0.5)
        self._make_home_content()

    def _make_home_content(self):
        try:
            self.shownOptions.destroy()
        except:
            pass
        self.shownOptions = makeFrame(self.window, 0.95, 0.95, 0.5, 0.55, COLOUR_SECOND,"center")
        makeLabel(self.shownOptions, WELCOME_TITLE, 16, 0.5, 0.1, "center", COLOUR_SECOND)
        makeLabel(self.shownOptions, WELCOME_INFO, 11, 0.5, 0.7, "center", COLOUR_SECOND)
        canvas, self.imageBG = placeImage(self.shownOptions, "res/icons/icon_large.png", 200, 200, 125, 100)       
        makeLabel(self.shownOptions, "Steven B. 2022", 8, 0.5, 0.95, "center", COLOUR_SECOND)

    def _update_options(self):
        self.shownOptions.destroy()
        self.interface_dict[self.method.get()]()
        print(self.operation.get(), self.method.get())        

    def _make_caesar_options(self):
        self.shownOptions = makeFrame(self.window, 1, 0.95, 0.5, 0.55, COLOUR_SECOND, "center")

        makeLabel(self.shownOptions, "Key:", 12, 0.15, 0.1, "center", COLOUR_SECOND)
        self.keyScale = makeScale(self.shownOptions, 1, 25, 0.5, 0.13, 20, 300, COLOUR_THIRD, COLOUR_TEXT)
        self.messageEntry = makeTextbox(self.shownOptions, 60, 6, COLOUR_THIRD, COLOUR_TEXT, 0.5,0.4) 
        makeLabel(self.shownOptions, "Output:", 12, 0.12, 0.64, "center", COLOUR_SECOND)
        self.messageOutput = makeTextbox(self.shownOptions, 60, 6, COLOUR_THIRD, COLOUR_TEXT, 0.5,0.78)

        if self.operation.get() == OPERATIONS[0]:
            # Encrypt options
            makeLabel(self.shownOptions, "Message:", 12, 0.11, 0.26, "center", COLOUR_SECOND)
            makeButton(self.shownOptions, "Encrypt", lambda x=None: self._process_caesar(), 12, 0.5, 0.56)
            self.messageOutput.insert(tk.END, "Your ciphertext will be shown here...")

        else:
            # Decrypt options
            makeLabel(self.shownOptions, "Ciphertext:", 12, 0.11, 0.26, "center", COLOUR_SECOND)
            makeButton(self.shownOptions, "Decrypt", lambda x=None: self._process_caesar(), 12, 0.5, 0.56)
            self.messageOutput.insert(tk.END, "The message will be shown here...")

        self.messageOutput.config(state=tk.DISABLED)

    def _process_caesar(self):
        key = self.keyScale.get()
        message = self.messageEntry.get("1.0", tk.END)
        caesar_cipher = CaesarCipher(key)
        
        if self.operation.get() == "Encrypt":
            output = caesar_cipher.encrypt(message)
        else:
            output = caesar_cipher.decrypt(message)

        self._update_readonly_box(self.messageOutput, output)

    @staticmethod
    def _update_readonly_box(text_box, content):
        text_box.config(state=tk.NORMAL)
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, content)
        text_box.config(state=tk.DISABLED)

    def _make_vernam_options(self):
        self.shownOptions = makeFrame(self.window, 1, 0.95, 0.5, 0.55, COLOUR_SECOND, "center")

        makeLabel(self.shownOptions, "Key:", 12, 0.15, 0.1, "center", COLOUR_SECOND)
        self.keyEntry = makeTextbox(self.shownOptions, 30, 1, COLOUR_THIRD, COLOUR_TEXT, 0.45,0.1) 
        self.messageEntry = makeTextbox(self.shownOptions, 60, 6, COLOUR_THIRD, COLOUR_TEXT, 0.5,0.4) 
        makeLabel(self.shownOptions, "Output:", 12, 0.12, 0.64, "center", COLOUR_SECOND)
        self.messageOutput = makeTextbox(self.shownOptions, 60, 6, COLOUR_THIRD, COLOUR_TEXT, 0.5,0.78)

        if self.operation.get() == OPERATIONS[0]:
            # encrypt options
            makeLabel(self.shownOptions, "Message:", 12, 0.11, 0.26, "center", COLOUR_SECOND)
            makeButton(self.shownOptions, "Encrypt", lambda x=None: self._process_vernam(), 12, 0.5, 0.56)
            self.messageOutput.insert(tk.END, "Your ciphertext will be shown here...")

        else:
            # decrypt options
            makeLabel(self.shownOptions, "Ciphertext:", 12, 0.11, 0.26, "center", COLOUR_SECOND)
            makeButton(self.shownOptions, "Decrypt", lambda x=None: self._process_vernam(), 12, 0.5, 0.56)
            self.messageOutput.insert(tk.END, "The message will be shown here...")
        self.messageOutput.config(state=tk.DISABLED)

    def _process_vernam(self):
        key = self.keyEntry.get("1.0",tk.END)
        message = self.messageEntry.get("1.0",tk.END)[:-1]
        vernam_cipher = VernamCipher(key)
        
        if self.operation.get() == "Encrypt":
            output = vernam_cipher.encrypt(message)
        else:
            output = vernam_cipher.decrypt(message)

        self._update_readonly_box(self.messageOutput, output)

    def _make_AES(self):
        self.shownOptions = makeFrame(self.window, 1, 0.95, 0.5, 0.55, COLOUR_SECOND, "center")

        makeLabel(self.shownOptions, "Output:", 12, 0.12, 0.64, "center", COLOUR_SECOND)
        self.messageOutput = makeTextbox(self.shownOptions, 60, 6, COLOUR_THIRD, COLOUR_TEXT, 0.5,0.78)

        if self.operation.get() == OPERATIONS[0]:
            # Encrypt options
            makeLabel(self.shownOptions, "Message:", 12, 0.11, 0.06, "center", COLOUR_SECOND)
            self.messageEntry = makeTextbox(self.shownOptions, 60, 6, COLOUR_THIRD, COLOUR_TEXT, 0.5,0.2)
            makeButton(self.shownOptions, "Encrypt", lambda x=None: self._process_AES(), 12, 0.5, 0.36)
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
            makeButton(self.shownOptions, "Decrypt", lambda x=None: self._process_AES(), 12, 0.5, 0.55)
            self.messageOutput.insert(tk.END, "The message will be shown here...")

        self.messageOutput.config(state=tk.DISABLED)

    def _process_AES(self):
        message = self.messageEntry.get("1.0", tk.END)[:-1]
        new_AES = AES_128()
        if self.operation.get() == "Encrypt":
            ciphertext, key = new_AES.encrypt(message)
            self._update_readonly_box(self.key, key)
            self._update_readonly_box(self.messageOutput, ciphertext)

        else:
            key = self.key.get("1.0", tk.END)[:-1]
            plaintext = new_AES.decrypt(message, key)
            self._update_readonly_box(self.messageOutput, plaintext)

    def _make_AES_custom(self):
        self.shownOptions = makeFrame(self.window, 1, 0.95, 0.5, 0.55, COLOUR_SECOND, "center")

        makeLabel(self.shownOptions, "Output:", 12, 0.12, 0.64, "center", COLOUR_SECOND)
        self.messageOutput = makeTextbox(self.shownOptions, 60, 6, COLOUR_THIRD, COLOUR_TEXT, 0.5,0.78)

        if self.operation.get() == OPERATIONS[0]:
            # Encrypt options
            makeLabel(self.shownOptions, "Custom Key:", 12, 0.12, 0.06, "center", COLOUR_SECOND)
            self.key = makeTextbox(self.shownOptions, 60, 3, COLOUR_THIRD, COLOUR_TEXT, 0.5,0.14)
            makeLabel(self.shownOptions, "Message:", 12, 0.11, 0.26, "center", COLOUR_SECOND)
            self.messageEntry = makeTextbox(self.shownOptions, 60, 6, COLOUR_THIRD, COLOUR_TEXT, 0.5,0.4)
            makeButton(self.shownOptions, "Encrypt", lambda x=None: self._process_AES_custom(), 12, 0.5, 0.55)
            self.messageOutput.insert(tk.END, "Your ciphertext will be shown here...")

        else:
            # Decrypt options
            makeLabel(self.shownOptions, "Key used:", 12, 0.12, 0.06, "center", COLOUR_SECOND)
            self.key = makeTextbox(self.shownOptions, 60, 3, COLOUR_THIRD, COLOUR_TEXT, 0.5,0.14)
            makeLabel(self.shownOptions, "Ciphertext:", 12, 0.11, 0.26, "center", COLOUR_SECOND)
            self.messageEntry = makeTextbox(self.shownOptions, 60, 6, COLOUR_THIRD, COLOUR_TEXT, 0.5,0.4)
            makeButton(self.shownOptions, "Decrypt", lambda x=None: self._process_AES_custom(), 12, 0.5, 0.55)
            self.messageOutput.insert(tk.END, "The message will be shown here...")

        self.messageOutput.config(state=tk.DISABLED)

    def _process_AES_custom(self):
        message = self.messageEntry.get("1.0", tk.END)[:-1]
        key = self.key.get("1.0", tk.END)[:-1]
        new_AES_custom = AES_256_custom_key()
        if self.operation.get() == "Encrypt":
            # add different encryption key lengths
            ciphertext = new_AES_custom.encrypt(message, key)
            self._update_readonly_box(self.messageOutput, ciphertext)

        else:
            plaintext = new_AES_custom.decrypt(message, key)
            self._update_readonly_box(self.messageOutput, plaintext)


if __name__ == "__main__":
    root = tk.Tk()
    MessageEncrypter(root)
    root.mainloop()
