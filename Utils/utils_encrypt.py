from cryptography.fernet import Fernet
from utils.leer_properties import LeerProperty


class UtilsEncrypt():
    fernet = None

    def __init__(self, key):
        if key != None:
            self.key = key
        else:
            self.key = Fernet.generate_key()

        self.fernet = Fernet(self.key)

    def encrypt_data(self, data):
        return self.fernet.encrypt(data.encode())

    def decrypt_data(self, data):
        return self.fernet.decrypt(data).decode()
