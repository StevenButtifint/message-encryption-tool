import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


class AES_256_custom_key(object):
    def __init__(self):
        self.block_size = AES.block_size
        
    def encrypt(self, plaintext, key):
        key = hashlib.sha256(key.encode()).digest()
        iv = Random.new().read(AES.block_size)
        plaintext = self._pad(plaintext)
        ciphertext = AES.new(key, AES.MODE_CBC, iv)
        return self._encode_base_64(iv + ciphertext.encrypt(plaintext.encode()))

