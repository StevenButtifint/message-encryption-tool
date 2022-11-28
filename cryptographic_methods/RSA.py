
from Crypto.PublicKey import RSA as _RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


class RSA:
    def __init__(self, key_size):
        self.key_size = key_size

    def encrypt(self, plaintext):
        private_key = _RSA.generate(self.key_size)
        public_key = private_key.publickey()
        encryption = PKCS1_OAEP.new(private_key)
        ciphertext = encryption.encrypt(bytes(plaintext.encode('utf-8')))
        encoded_ciphertext = base64.b64encode(ciphertext)
        return encoded_ciphertext, private_key.exportKey("PEM"), public_key.exportKey("PEM")

    @staticmethod
    def decrypt(encoded_ciphertext, key_string):
        private_key = _RSA.importKey(key_string)
        encryption = PKCS1_OAEP.new(private_key)
        ciphertext = base64.b64decode(encoded_ciphertext)
        plaintext = encryption.decrypt(ciphertext)
        return plaintext
