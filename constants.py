from cryptographic_methods.AES_128 import AES_128
from cryptographic_methods.RSA_512 import RSA_512
from cryptographic_methods.caesar_cipher import CaesarCipher
from cryptographic_methods.vernam_cipher import VernamCipher
from cryptographic_methods.AES_256_custom_key import AES_256_custom_key


#colours
COLOUR_PRIME = "cyan4"
COLOUR_SECOND = "cyan2"
COLOUR_THIRD = "DarkSlateGray3"
COLOUR_TEXT = "black"


#labels
CRYPTO_METHODS = ["Caesar Cipher", "Vernam Cipher", "AES-128 Symmetric-Key", "AES-256 Custom-Key", "RSA-512 Asymmetric-Key"]
OPERATIONS = ["Encrypt", "Decrypt"]


#window
RESOLUTION = "500x500"
TITLE = "Message Encryption Tool"
ICON_DIR = "res/icons/icon.ico"


METHOD_DICT = {
    "Caesar Cipher": CaesarCipher,
    "Vernam Cipher": VernamCipher}
    
