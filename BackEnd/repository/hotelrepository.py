from .dlbase import DLBase


class HotelRepository(DLBase):
    def __init__(self) -> None:
        super().__init__()

    def getAllHotel(self):
        sql = "Select * from hotel;"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, ())
        hotels = cursor.fetchall()
        return hotels

    def getHotelByAmount(self, amount):
        sql = "Select * from hotel limit %d;"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (amount, ))
        hotels = cursor.fetchall()
        return hotels
