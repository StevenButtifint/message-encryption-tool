from random import randint

class CaesarCipher(object):

    def __init__(self, shift):
        self.shift = shift
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.alphabet_len = len(self.alphabet)

