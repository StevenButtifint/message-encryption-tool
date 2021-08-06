import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


class AES256custom(object):

    def __init__(self, key): 
        self.key = hashlib.sha256(key.encode()).digest()
        self.block_size = AES.block_size
        
    def encrypt(self, plaintext):
        iv = Random.new().read(AES.block_size)
        plaintext = self._pad(plaintext)
        ciphertext = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + ciphertext.encrypt(plaintext.encode()))



