from cryptography.fernet import Fernet
from Utils.leerProperties import LeerPropertyClass

class UtilsEncrypt():

    fernet = None
    def __init__(self, key):
        if key != None:
            self.key = key
        else:
            self.key = Fernet.generate_key()

        self.fernet = Fernet(self.key)

    def encryptData(self, data):
        return self.fernet.encrypt(data.encode())
    def decryptData(self, data):
        return self.fernet.decrypt(data).decode()