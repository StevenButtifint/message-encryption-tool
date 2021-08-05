import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


class AES256custom(object):

    def __init__(self, key): 
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()




