from cryptography.fernet import Fernet


class AES_128_symmetric_key(object):

    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        if str(self.key) == "b''":
            self.key = Fernet.generate_key()
        f = Fernet(self.key)
        msg_encoded = plaintext.encode()
        ciphertext = f.encrypt(msg_encoded)
        return ciphertext, self.key

    def decrypt(self, ciphertext):
        f = Fernet(self.key)
        msg_encoded = f.decrypt(ciphertext)
        plaintext = msg_encoded.decode()
        return plaintext
