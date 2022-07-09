from flask import Blueprint, request
from flask.wrappers import Response
from bussiness.restaurantservice import RestaurantService
from flask_cors import CORS
from flask_cors.decorator import cross_origin

restaurant = Blueprint("restaurant", __name__)
cors = CORS(restaurant, resources={r"/api/*": {"origins": "*"}})
restaurantservice = RestaurantService()


@restaurant.route("/restaurant/searchAll", methods=['GET'])
@cross_origin()
def searchAll():
    result = restaurantservice.getAllRestaurant()
    return Response(response=result, status=200, mimetype="application/json")


@restaurant.route("/restaurant/searchByHotel", methods=['GET'])
@cross_origin()
def searchByHotelId():
    _json = request.json
    HotelID = _json['HotelID']

    result = restaurantservice.getRestaurantByHotelId(HotelID)
    return Response(response=result, status=200, mimetype="application/json")
