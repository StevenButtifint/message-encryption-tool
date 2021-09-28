import rsa


class RSA_512_asymmetric_key(object):

    def __init__(self, key):
        self.publicKey = key

    def encrypt(self, plaintext):
        if str(self.publicKey) == "":
            self.publicKey, privateKey = rsa.newkeys(512)
        ciphertext = rsa.encrypt(plaintext.encode(), self.publicKey)
        #print(type(publicKey))
        #print(self.publicKey.exportKey("PEM"))
        return ciphertext, self.publicKey, privateKey

    #methods not using self, @staticmethod removes the assumption of self param
    @staticmethod
    def decrypt(ciphertext, privateKey):
        print("current types")
        print(type(privateKey), type(rsa.importKey(privateKey)))
        print(type(ciphertext), type(bytes(ciphertext, encoding='utf-8')))
        return rsa.decrypt(bytes(ciphertext, encoding='utf-8'), rsa.importKey(privateKey)).decode()
