class User:
    userNum = 1000
    def __init__(self, email, phone, password):
        self.email = email
        self.phone = phone
        self.password = password
        self.houseCode = None
git commi
    def getEmail(self):
        return self.email

    def getPhone(self):
        return self.phone

    def getPassword(self):
        return self.password

    def getCode(self):
        return self.houseCode

    def setCode(self, newCode):
        self.houseCode = newCode