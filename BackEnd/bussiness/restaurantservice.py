from repository.restaurantrepository import RestaurantRepository

class RestaurantService:
    dl = None
    def __init__(self) -> None:
        self.dl = RestaurantRepository()

    def getAllRestaurant(self):
        result = self.dl.getAllRestaurant()
        return result

    def getRestaurantByHotelId(self, HotelID):
        result = self.dl.getRestaurantByHotelId(HotelID)
        return result
