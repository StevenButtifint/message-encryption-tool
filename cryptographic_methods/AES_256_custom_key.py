import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


class AES_256_custom_key(object):
    def __init__(self):
        self.block_size = AES.block_size
        
