from repository.roomrepository import RoomRepository

class RoomService:
    dl = None
    def __init__(self) -> None:
        self.dl = RoomRepository()

    def getRoomByHotelId(self, HotelID):
        result = self.dl.getRoomByHotelId(HotelID)
        return result
