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

