import re
from flask import Blueprint, request
from flask.wrappers import Response
from bussiness.tourservice import TourService
from flask_cors import CORS
from flask_cors.decorator import cross_origin
import json

tour = Blueprint("tour", __name__)
cors = CORS(tour, resources={r"/api/*": {"origins": "*"}})
bl = TourService()

@tour.route("/tour/createdata", methods=['POST'])
@cross_origin()
def createDataXML():
    _json = request.json
    bl.createDataXML(_json)

    result = None
    return Response(response=result, status=201, mimetype="application/json")

@tour.route("/tour/gethtml", methods=['GET'])
@cross_origin()
def getTourHTML():
    _json = request.args
    id = _json.get("id")
    result = bl.getTourHTML(id)
    if result is None:
        return f"<html></html>"
    else:
        return result