from .dlbase import DLBase

class UserRepository(DLBase):
    def __init__(self) -> None:
        super().__init__()

    def getUserByEmail(self, email):
        sql = "Select * from user where Email like %s;"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (email))
        users = cursor.fetchall()
        return users

    def insertNewUser(self, email, password, username, phone):
        sql = "insert into user values (%s, %s, %s, %s);"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (username, password, email, phone))
        self.conn.commit()