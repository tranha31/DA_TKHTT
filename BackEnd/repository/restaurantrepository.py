from .dlbase import DLBase

class RestaurantRepository(DLBase):
    def __init__(self) -> None:
        super().__init__()

    def getAllRestaurant(self):
        sql = "Select * from restaurant;"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql)
        restaurants = cursor.fetchall()
        return restaurants

    def getRestaurantByHotelId(self, HotelID):
        sql = "Select * from restaurant where HotelID = %d;"
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(sql, (HotelID))
        restaurants = cursor.fetchall()
        return restaurants