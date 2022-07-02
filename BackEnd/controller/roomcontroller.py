from flask import Blueprint, request
from flask.wrappers import Response
from bussiness.roomservice import RoomService
from flask_cors import CORS
from flask_cors.decorator import cross_origin

room = Blueprint("room", __name__)
cors = CORS(room, resources={r"/api/*": {"origins": "*"}})
roomservice = RoomService()


@room.route("/searchRoomByHotel", methods=['GET'])
@cross_origin()
def searchAll():
    _json = request.json
    HotelID = _json['HotelID']

    result = roomservice.getRoomByHotelId(HotelID)
    return Response(response=result, status=200, mimetype="application/json")

