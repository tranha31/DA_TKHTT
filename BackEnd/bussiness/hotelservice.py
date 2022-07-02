from repository.hotelrepository import HotelRepository

class HotelService:
    dl = None
    def __init__(self) -> None:
        self.dl = HotelRepository()

    def getAllHotel(self):
        result = self.dl.getAllHotel()
        return result

    def getHotelByAmount(self, amount = 30):
        result = self.dl.getHotelByAmount(amount)
        return result
