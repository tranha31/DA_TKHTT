from flask import Blueprint, request
from flask.wrappers import Response
from bussiness.restaurantservice import RestaurantService

restaurant = Blueprint("restaurant", __name__)
cors = CORS(test, resources={r"/api/*": {"origins": "*"}})
restaurantservice = RestaurantService()

@restaurant.route("/searchAll", methods=['GET'])
@cross_origin()
def searchAll():
    result = restaurantservice.getAllRestaurant()
    return Response(response=result, status=200, mimetype="application/json")

@restaurant.route("/searchByHotel", methods=['GET'])
@cross_origin()
def searchByHotelId():
    _json = request.json
    HotelID = _json['HotelID']

    result = restaurantservice.getRestaurantByHotelId(HotelID)
    return Response(response=result, status=200, mimetype="application/json")
