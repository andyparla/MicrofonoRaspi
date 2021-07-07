from cryptography.fernet import Fernet

class UtilsEncrypt():

    fernet = None
    key = None
    def __init__(self):
        self.fernet = Fernet(Fernet.generate_key())

    def encryptData(self, data):
        return self.fernet.encrypt(data.encode())
    def decryptData(self, data):
        return self.fernet.decrypt(data).decode()
util = UtilsEncrypt()
# print(util.encryptData("1856142691:AAFvGIIKkvPsrivlAnL9CRr272xJl-yKi80"))
print(util.decryptData("gAAAAABg5bTDpaFN2f4kC971kEw3RYewlfYrxhAPBwAQTo7JbLPsm1m1C5UEdQZ8Kwc4sy2NIUh-TV6KdCLo6rpy17TaJHzKc0TJaJATjlGcru4aRINEafSLKXKu8sSxfcGahAIYErHQ"))