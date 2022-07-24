from .dlbase import DLBase
import uuid

class UserRepository(DLBase):
    def __init__(self) -> None:
        super().__init__()

    def getUserByEmail(self, email):
        sql = "Select * from user where Email = %s;"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (email,))
        users = cursor.fetchall()
        return users

    def insertNewUser(self, email, password, username, phone, identify, name, address, sign):
        refID = str(uuid.uuid4())
        sql = "insert into user values (%s, %s, %s, %s, %s, %s, %s, %s);"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (refID, username, password, email, phone, identify, name, address))
        self.conn.commit()

        collection = self.dbMongo["UserSignature"]
        dic = {"_id": str(uuid.uuid4()), "UserID": refID, "ContentSign": sign}
        collection.insert_one(dic)

    def getUserInformationsById(self, UserID):
        sql = "select * from user where UserID = %s;"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (UserID, ))
        users = cursor.fetchall()
        return users

    def updateUserInformations(self, UserID, Email, PhoneNumber, Identify, Name, Address):
        sql = "update user set Email = %s, PhoneNumber = %s, IdentityNumber = %s, Name = %s, Address = %s where UserID = %s;"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (Email, PhoneNumber, UserID, Identify, Name, Address))
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

    def getAllUsersByListID(self, ListUserID):
        sql = "select * from user where UserID in (%s);"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (ListUserID, ))
        users = cursor.fetchall()
        return users
