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

    def getHotelById(self, hotelId):
        sql = "Select * from hotel where HotelID = %s;"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (hotelId, ))
        hotels = cursor.fetchall()
        return hotels

    def insertNewHotel(self, Name, HotelCode, Acreage, Address, PhoneNumber, Rank, Email, Solgan, Described, SortDescribed, DescribedRoom):
        sql = "insert into hotel values (UUID(), UUID(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (HotelCode, Name, Email, PhoneNumber, Solgan,
                       Described, Address, Acreage, Rank, SortDescribed, DescribedRoom, '', ))

        return 'Insert New Hotel Success!'
