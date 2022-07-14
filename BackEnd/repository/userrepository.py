from .dlbase import DLBase


class UserRepository(DLBase):
    def __init__(self) -> None:
        super().__init__()

    def getUserByEmail(self, email):
        sql = "Select * from user where Email = %s;"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (email, ))
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
