from .dlbase import DLBase


class ChatRepository(DLBase):
    def __init__(self) -> None:
        super().__init__()

    def getChatRoomByUserID(self, UserID):
        sql = "Select * from chatroom where UserID = %s;"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (UserID, ))
        rooms = cursor.fetchall()
        return rooms

    def createNewChatRoom(self, UserID):
        sql = "insert into chatroom values (UUID(), %s, now());"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (UserID, ))

    def loadAllChatRoom(self):
        sql = "Select * from chatroom;"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, ())

        rooms = cursor.fetchall()
        return rooms

    def loadAllChatRoomByAmount(self, amount):
        sql = "Select * from chatroom limit %s;"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (amount, ))

        rooms = cursor.fetchall()
        return rooms
