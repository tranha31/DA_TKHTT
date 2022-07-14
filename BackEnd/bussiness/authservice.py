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

    def register(self, email, password, username, phone):
        emailExist = self.dl.getUserByEmail(email)

        if (emailExist is not None and len(emailExist) > 0):
            return "Account with email already existed!"
        else:
            self.dl.insertNewUser(email, password, username, phone)
            return "Register new user success!"

    def getUserInformationsById(self, UserID):
        result = self.dl.getUserInformationsById(UserID)

        if result is None or len(result) <= 0:
            return None
        else:
            user = result[0]
            return user
