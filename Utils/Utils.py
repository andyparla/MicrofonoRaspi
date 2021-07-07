from cryptography.fernet import Fernet

class UtilsEncrypt():

    fernet = None
    key = None
    def __init__(self, key):
        if key != None:
            self.key = key
        else:
            self.key = Fernet.generate_key()
            print(self.key)

        self.fernet = Fernet(self.key)

    def encryptData(self, data):
        return self.fernet.encrypt(data.encode())
    def decryptData(self, data):
        return self.fernet.decrypt(data).decode()
util = UtilsEncrypt(b'DPYVeSnMa_rcAwrtBcn2dJpfuzz4R4f3Ax1HIv5Gi8c=')
# print(util.encryptData("1856142691:AAFvGIIKkvPsrivlAnL9CRr272xJl-yKi80"))
print(util.decryptData(b'gAAAAABg5baxxikQjdQixPTSrhOGCN9CjsBo_NJvTbAmMEVT8EL1TjZAN0aM0VWSFU4A7EgwM6jKqZBVt27dz5O1O2_73JA0MtxiUEM6RVKUbPZZ5MseQE29pBnX0mvSQ0TDvE-ydlVE'))