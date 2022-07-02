from flask import Blueprint, request
from flask.wrappers import Response
from bussiness.hotelservice import HotelService
from flask_cors import CORS
from flask_cors.decorator import cross_origin

hotel = Blueprint("hotel", __name__)
cors = CORS(hotel, resources={r"/api/*": {"origins": "*"}})
hotelservice = HotelService()

@hotel.route("/searchAll", methods=['GET'])
@cross_origin()
def searchAll():
    result = hotelservice.getAllHotel()
    return Response(response=result, status=200, mimetype="application/json")


@hotel.route("/searchHotel", methods=['GET'])
@cross_origin()
def searchByAmount():
    _json = request.json
    amount = _json['amount']

    result = hotelservice.getHotelByAmount(amount)
    return Response(response=result, status=200, mimetype="application/json")

