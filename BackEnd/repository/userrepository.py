from .dlbase import DLBase


class UserRepository(DLBase):
    def __init__(self) -> None:
        super().__init__()

    def getUserByEmail(self, email):
        sql = "Select * from user where Email = %s;"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (email,))
        users = cursor.fetchall()
        return users
        

    def insertNewUser(self, email, password, username, phone):
        sql = "insert into user values (UUID(), %s, %s, %s, %s, LEFT(UUID(), 20));"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (username, password, email, phone, ))
        self.conn.commit()

    def getUserInformationsById(self, UserID):
        sql = "select * from user where UserID = %s;"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (UserID, ))
        users = cursor.fetchall()
        return users

    def updateUserInformations(self, UserID, Email, PhoneNumber):
        sql = "update user set Email = %s, PhoneNumber = %s where UserID = %s;"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (Email, PhoneNumber, UserID, ))
        self.conn.commit()

    def updatePassword(self, UserID, Password):
        sql = "update user set Password = %s where UserID = %s;"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (Password, UserID, ))
        self.conn.commit()
        
    def getInfo(self, id):
        sql = "SELECT * FROM user WHERE UserID = %s"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (id,))
        users = cursor.fetchall()
        return users