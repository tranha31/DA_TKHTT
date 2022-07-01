from .dlbase import DLBase

class RoomRepository(DLBase):
    def __init__(self) -> None:
        super().__init__()

    def getRoomByHotelId(self, HotelID):
        sql = "Select * from room where HotelID = %d;"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (HotelID))
        rooms = cursor.fetchall()
        return rooms