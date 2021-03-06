from repository.userrepository import UserRepository


class AuthService:
    dl = None

    def __init__(self) -> None:
        self.dl = UserRepository()

    def validateLogin(self, email, password):
        result = self.dl.getUserByEmail(email)

        if (result is None or len(result) <= 0):
            return "No account with email existed!"
        else:
            user = result[0]
            if (user['Password'].__eq__(password)):
                return user
            else:
                return "Wrong password!"

    def register(self, email, password, username, phone, identify, name, address, sign):
        emailExist = self.dl.getUserByEmail(email)

        if (emailExist is not None and len(emailExist) > 0):
            return "Account with email already existed!"
        else:
            self.dl.insertNewUser(email, password, username, phone, identify, name, address, sign)
            return "Register new user success!"

    def getInfo(self, id):
        return self.dl.getInfo(id)

    def getUserInformationsById(self, UserID):
        result = self.dl.getUserInformationsById(UserID)

        if result is None or len(result) <= 0:
            return None
        else:
            user = result[0]
            return user

    def updateGeneralInformations(self, UserID, Email, PhoneNumber, Identify, Name, Address):
        self.dl.updateUserInformations(UserID, Email, PhoneNumber, Identify, Name, Address)

        return "Update profile success!"

    def updatePassword(self, UserID, Password):
        self.dl.updatePassword(UserID, Password)

        return "Update password success!"

    def getUserByListId(self, ListUserID):
        result = self.dl.getAllUsersByListID(ListUserID)

        return result

    def validateLoginAdmin(self, username, password):
        result = self.dl.getAdmin(username)

        if (result is None or len(result) <= 0):
            return "No account with username existed!"
        else:
            admin = result[0]
            if (admin['Password'].__eq__(password)):
                return admin
            else:
                return "Wrong password!"