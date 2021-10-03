

class VernamCipher(object):

    def __init__(self, key):
        self.key = key
        self.key_len = len(key)
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.alphabet_len = len(self.alphabet)

    def encrypt(self, plaintext):
        ciphertext = ""
        plaintext = ''.join(filter(str.isalpha, plaintext))
        for idx, letter in enumerate(plaintext):
            p_idx = self.alphabet.find(letter)
            k_idx = self.alphabet.find(self.key[idx % self.key_len])
            ciphertext += (self.alphabet[(p_idx + k_idx) % self.alphabet_len])
        return ciphertext

