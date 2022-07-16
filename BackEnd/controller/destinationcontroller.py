import re
from flask import Blueprint, request
from flask.wrappers import Response
from bussiness.destinationservice import DestinationService
from flask_cors import CORS
from flask_cors.decorator import cross_origin
import json

destination = Blueprint("destination", __name__)
cors = CORS(destination, resources={r"/api/*": {"origins": "*"}})
bl = DestinationService()

@destination.route("/province/import", methods=['POST'])
@cross_origin()
def importProvince():
    bl.importProvince()
    result = None
    return Response(response=result, status=201, mimetype="application/json")

@destination.route("/province/all", methods=['GET'])
@cross_origin()
def getAllProvince():
    result = bl.getAllProvince()
    result = json.dumps(result, ensure_ascii=False)
    return Response(response=result, status=200, mimetype="application/json")

@destination.route("/district/all", methods=['GET'])
@cross_origin()
def getAllDistrict():
    result = bl.getAllDistrict()
    result = json.dumps(result, ensure_ascii=False)
    return Response(response=result, status=200, mimetype="application/json")

@destination.route("/province/byid", methods=['GET'])
@cross_origin()
def getProvinceByID():
    r = request
    r = r.args
    id = r.get("id")
    result = bl.getProvinceByID(id)
    result = json.dumps(result, ensure_ascii=False)
    return Response(response=result, status=200, mimetype="application/json")

@destination.route("/district/byid", methods=['GET'])
@cross_origin()
def getDistrictByID():
    r = request
    r = r.args
    id = r.get("id")
    result = bl.getDistrictByID(id)
    result = json.dumps(result, ensure_ascii=False)
    return Response(response=result, status=200, mimetype="application/json")

@destination.route("/district/inprovince", methods=['GET'])
@cross_origin()
def getDistrictInProvince():
    r = request
    r = r.args
    id = r.get("pid")
    result = bl.getDistrictInProvince(id)
    result = json.dumps(result, ensure_ascii=False)
    return Response(response=result, status=200, mimetype="application/json")

@destination.route("/destination/update", methods=['POST'])
@cross_origin()
def update():
    r = request
    r = r.json
    result = bl.updateDestination(r)
    serviceResult = {
        "error" : ""
    }
    if result == False:
        serviceResult["error"] = "DupliacteName"
    serviceResult = json.dumps(serviceResult)
    return Response(response=serviceResult, status=201, mimetype="application/json")

@destination.route("/destination/all", methods=['GET'])
@cross_origin()
def getAllDestination():
    r = request
    r = r.args
    search = r.get("search")
    size = int(r.get("size"))
    page = int(r.get("page"))
    result = bl.getList(search, size, page)
    result = json.dumps(result, ensure_ascii=False)
    return Response(response=result, status=200, mimetype="application/json")

@destination.route("/destination/byid", methods=['GET'])
@cross_origin()
def getDestinationByID():
    r = request
    r = r.args
    id = r.get("id")
    result = bl.getDestinationByID(id)
    result = json.dumps(result, ensure_ascii=False)
    return Response(response=result, status=200, mimetype="application/json")

@destination.route("/destination/delete", methods=['DELETE'])
@cross_origin()
def deleteDestination():
    r = request
    r = r.args
    id = r.get("id")
    result = bl.deleteDestination(id)
    serviceResult = {
        "error" : ""
    }
    if result == False:
        serviceResult["error"] = "ExistReperence"
    serviceResult = json.dumps(serviceResult)
    return Response(response=serviceResult, status=200, mimetype="application/json")

@destination.route("/destination/inprovince", methods=['GET'])
@cross_origin()
def deleteDestinationInProvince():
    r = request
    r = r.args
    id = r.get("id")
    result = bl.deleteDestinationInProvince(id)
    result = json.dumps(result)
    return Response(response=result, status=200, mimetype="application/json")