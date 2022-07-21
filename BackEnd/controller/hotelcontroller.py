from flask import Blueprint, request
from flask.wrappers import Response
from bussiness.hotelservice import HotelService
from flask_cors import CORS
from flask_cors.decorator import cross_origin
from flask import jsonify

hotel = Blueprint("hotel", __name__)
cors = CORS(hotel, resources={
            r"/api/*": {"origins": "*"}})
hotelservice = HotelService()


@hotel.route("/hotel/searchAll", methods=['GET'])
@cross_origin()
def searchAll():
    result = hotelservice.getAllHotel()
    return jsonify(result)


@hotel.route("/hotel/searchHotel", methods=['GET'])
@cross_origin()
def searchByAmount():
    _json = request.json
    amount = _json['amount']

    result = hotelservice.getHotelByAmount(amount)
    return jsonify(result)


@hotel.route("/hotel/searchById", methods=['POST'])
@cross_origin()
def searchById():
    _json = request.json
    hotelId = _json['HotelID']

    result = hotelservice.getHotelById(hotelId)
    return jsonify(result)


@hotel.route("/hotel/addNewHotel", methods=['POST'])
@cross_origin()
def addNewHotel():
    _json = request.json
    Name = _json['Name']
    HotelCode = _json['HotelCode']
    Acreage = _json['Acreage']
    Address = _json['Address']
    PhoneNumber = _json['PhoneNumber']
    Rank = _json['Rank']
    Email = _json['Email']
    Solgan = _json['Solgan']
    Described = _json['Described']
    SortDescribed = _json['SortDescribed']
    DescribedRoom = _json['DescribedRoom']

    result = hotelservice.addNewHotel(Name, HotelCode, Acreage, Address, PhoneNumber,
                                      Rank, Email, Solgan, Described, SortDescribed, DescribedRoom)
    return Response(response=result, status=200, mimetype="application/json")
