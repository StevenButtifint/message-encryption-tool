from random import randint

class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.alphabet_len = len(self.alphabet)


    def encrypt(self, plaintext):
        ciphertext = ""
        self._setShift()
        for letter in plaintext:
            index = self.alphabet.find(letter)
            if index != -1:
                ciphertext += self.alphabet[(index + self.shift) % self.alphabet_len]
        return ciphertext


    def decrypt(self, ciphertext):
        plaintext = ""
        self.shift = int(self.shift)
        for letter in ciphertext:
            try:
                index = self.alphabet.find(letter)
                if index != -1:
                    plaintext += self.alphabet[(index - self.shift) % self.alphabet_len]
            except:
                pass
        return plaintext

        
    def _setShift(self):
        if self.shift == "":
            self.shift = randint(2, self.alphabet_len)
        else:
            self.shift = int(self.shift)


    def sanitizeEncrypt(self, plaintext):
        ciphertext = self.encrypt(plaintext)
        return ("Shift:\n" + str(self.shift) +"\n\n" + "Ciphertext:\n" + str(ciphertext))


    def sanitizeDecrypt(self, ciphertext):
        plaintext = self.decrypt(ciphertext)
        return ("Shift:\n" + str(self.shift) +"\n\n" + "Plaintext:\n" + str(plaintext))
