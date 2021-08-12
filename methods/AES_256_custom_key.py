import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


class AES_256_custom_key(object):

    def __init__(self, key): 
        self.key = hashlib.sha256(key.encode()).digest()
        self.block_size = AES.block_size
        
    def encrypt(self, plaintext):
        iv = Random.new().read(AES.block_size)
        plaintext = self._pad(plaintext)
        ciphertext = AES.new(self.key, AES.MODE_CBC, iv)
        return self._encodeBase64(iv + ciphertext.encrypt(plaintext.encode()))

    def decrypt(self, ciphertext):
        ciphertext = self._decodeBase64(ciphertext)
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(ciphertext[AES.block_size:])).decode('utf-8')

    #Internal class functions
    def _encodeBase64(self, data):
        return base64.b64encode(data)

    def _decodeBase64(self, data):
        return base64.b64decode(data)

    def _pad(self, p):
        return p + (self.block_size - len(p) % self.block_size) * chr(self.block_size - len(p) % self.block_size)

    #Static Methods not using class instance
    @staticmethod
    def _unpad(p):
        return p[:-ord(p[len(p)-1:])]
