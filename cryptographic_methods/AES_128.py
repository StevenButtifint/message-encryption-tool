from cryptography.fernet import Fernet


class AES_128:
    def __init__(self):
        self.key = bytes("", encoding='utf-8')

    def encrypt(self, plaintext):
        if str(self.key) == "b''":
            self.key = Fernet.generate_key()
        f = Fernet(self.key)
        msg_encoded = plaintext.encode()
        ciphertext = f.encrypt(msg_encoded)
        return ciphertext, self.key

    @staticmethod
    def decrypt(ciphertext, key):
        f = Fernet(bytes(key, encoding='utf-8'))
        msg_encoded = f.decrypt(bytes(ciphertext, encoding='utf-8'))
        plaintext = msg_encoded.decode()
        return plaintext
