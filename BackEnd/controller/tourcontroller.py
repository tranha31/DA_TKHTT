from dataclasses import dataclass
import re
from this import d
from urllib import response
from flask import Blueprint, request, make_response, render_template
from flask.wrappers import Response
from bussiness.tourservice import TourService
from flask_cors import CORS
from flask_cors.decorator import cross_origin
import json
import requests
import pdfkit

tour = Blueprint("tour", __name__)
cors = CORS(tour, resources={r"/api/*": {"origins": "*"}})
bl = TourService()

@tour.route("/tour/updatetemplate", methods=['POST'])
@cross_origin()
def updateTemplateTour():
    _json = request.json
    result = bl.updateTour(_json)
    serviceResult = {
        "error" : ""
    }
    if result == False:
        serviceResult["error"] = "DupliacteName"
    serviceResult = json.dumps(serviceResult)
    return Response(response=serviceResult, status=201, mimetype="application/json")

@tour.route("/tour/gettourtemp", methods=['GET'])
@cross_origin()
def getTourPDF():
    _json = request.args
    id = _json.get("id")
    html = bl.getTourHTML(id)
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html, False, configuration=config)
    response = make_response(pdf)
    response.headers['Content-type'] = "application/pdf"
    response.headers['Content-Disposition'] = 'inline; filename=contract.pdf'

    return response

@tour.route("/tour/newtourcode", methods=['GET'])
@cross_origin()
def getNewTourCode():
    result = bl.getNewTourCode()
    result = json.dumps(result, ensure_ascii=False)
    return Response(response=result, status=200, mimetype="application/json")

@tour.route("/tour/saymoney", methods=['GET'])
@cross_origin()
def sayMoney():
    _json = request.args
    money = _json.get("money")
    api = "http://forum.vdevs.net/nossl/mtw.php?number="+money
    response = requests.get(f"{api}")
    if response.status_code == 200:
        data = response.json()
        result = data.get("result")
    else:
        result = ""
    result = json.dumps(result, ensure_ascii=False)
    return Response(response=result, status=200, mimetype="application/json")

@tour.route("/tour/filter", methods=['GET'])
@cross_origin()
def getTourFilter():
    r = request
    r = r.args
    search = r.get("search")
    size = int(r.get("size"))
    page = int(r.get("page"))
    isStop = int(r.get("isStop"))
    mode = int(r.get("mode"))
    result = bl.getList(search, size, page, isStop, mode)
    result = json.dumps(result, ensure_ascii=False)
    return Response(response=result, status=200, mimetype="application/json")

@tour.route("/tour/deleteTemplate", methods=['DELETE'])
@cross_origin()
def deleteTemplate():
    r = request
    r = r.args
    id = r.get("id")
    result = bl.deleteTemplate(id)
    serviceResult = {
        "error" : ""
    }
    if result == False:
        serviceResult["error"] = "ExistInCart"
    serviceResult = json.dumps(serviceResult)
    return Response(response=serviceResult, status=200, mimetype="application/json")

@tour.route("/tour/updatestatus", methods=['GET'])
@cross_origin()
def updateStatusTemplate():
    r = request
    r = r.args
    id = r.get("id")
    status = r.get("status")
    bl.updateStatusTemplate(id, status)
    result = None
    return Response(response=result, status=200, mimetype="application/json")

@tour.route("/tour/getbyid", methods=['GET'])
@cross_origin()
def getByID():
    r = request
    r = r.args
    id = r.get("id")
    result = bl.getByID(id)
    result = json.dumps(result, ensure_ascii=False)
    return Response(response=result, status=200, mimetype="application/json")

@tour.route("/tour/user/filter", methods=['GET'])
@cross_origin()
def getTourFilterSideUser():
    r = request
    r = r.args
    search = r.get("search")
    size = int(r.get("size"))
    page = int(r.get("page"))
    destinationID = r.get("destinationID")
    startID = r.get("startID")
    timeOfTour = r.get("time")
    price = r.get("price")
    result = bl.getListTourSideUser(search, destinationID, startID, timeOfTour, price, size, page)
    result = json.dumps(result, ensure_ascii=False)
    return Response(response=result, status=200, mimetype="application/json")

@tour.route("/tour/user/suggest", methods=['GET'])
@cross_origin()
def getListTourSuggest():
    r = request
    r = r.args
    tourID = r.get("tourID")
    destinationID = r.get("toID")
    result = bl.getListTourSuggest(tourID, destinationID)
    result = json.dumps(result, ensure_ascii=False)
    return Response(response=result, status=200, mimetype="application/json")

@tour.route("/tour/updatetour", methods=['POST'])
@cross_origin()
def updateCustomerTour():
    _json = request.json
    result = bl.updateTour(_json)
    serviceResult = {
        "error" : ""
    }
    if result == False:
        serviceResult["error"] = "DupliacteName"
    serviceResult = json.dumps(serviceResult)
    return Response(response=serviceResult, status=201, mimetype="application/json")

@tour.route("/tour/addtocart", methods=['POST'])
@cross_origin()
def addToCart():
    r = request.json
    tourID = r["TourID"]
    userID = r["UserID"]
    execute = bl.addToCart(tourID, userID)
    serviceResult = {
        "error" : ""
    }
    if execute == False:
        serviceResult["error"] = "ExistInCart"
    serviceResult = json.dumps(serviceResult)
    return Response(response=serviceResult, status=201, mimetype="application/json")

@tour.route("/tour/deleteincart", methods=['DELETE'])
@cross_origin()
def deleteInCart():
    r = request
    r = r.args
    tourID = r.get("tourID")
    userID = r.get("userID")
    bl.deleteInCart(tourID, userID)
    result = None
    return Response(response=result, status=201, mimetype="application/json")

@tour.route("/tour/getcart", methods=['GET'])
@cross_origin()
def getInCart():
    r = request
    r = r.args
    userID = r.get("userID")
    result = bl.getTourUserInCart(userID)
    result = json.dumps(result, ensure_ascii=False)
    return Response(response=result, status=201, mimetype="application/json")

@tour.route("/tour/getlistorder", methods=['GET'])
@cross_origin()
def getListOrder():
    r = request
    r = r.args
    userID = r.get("userID")
    result = bl.getListOrder(userID)
    result = json.dumps(result, ensure_ascii=False)
    return Response(response=result, status=201, mimetype="application/json")

@tour.route("/tour/canceltour", methods=['GET'])
@cross_origin()
def cancelTourByUser():
    r = request
    r = r.args
    userID = r.get("userID")
    tourId = r.get("tourID")
    bl.cancelTourByUser(userID, tourId)
    result = None
    return Response(response=result, status=201, mimetype="application/json")

@tour.route("/tour/cancelTourA", methods=['GET'])
@cross_origin()
def cancelTourByAdmin():
    r = request
    r = r.args
    id = r.get("id")
    bl.cancelTourByAdmin(id)
    result = None
    return Response(response=result, status=201, mimetype="application/json")

@tour.route("/tour/deletetour", methods=['DELETE'])
@cross_origin()
def deleteTourByUser():
    r = request
    r = r.args
    userID = r.get("userID")
    tourId = r.get("tourID")
    result = bl.deleteTourByUser(userID, tourId)
    serviceResult = {
        "error" : ""
    }
    if result == False:
        serviceResult["error"] = "CannotDelete"
    serviceResult = json.dumps(serviceResult)
    return Response(response=serviceResult, status=201, mimetype="application/json")

@tour.route("/tour/confirmTour", methods=['POST'])
@cross_origin()
def confirmTourByAdmin():
    r = request
    r = r.args
    id = r.get("id")
    result = bl.confirmTourByAdmin(id)
    serviceResult = {
        "error" : ""
    }
    if result == False:
        serviceResult["error"] = "TourNotExist"
    serviceResult = json.dumps(serviceResult)
    return Response(response=serviceResult, status=201, mimetype="application/json")

@tour.route("/tour/confirmtouser", methods=['POST'])
@cross_origin()
def confirmTourByUser():
    r = request
    r = r.args
    id = r.get("tourID")
    usrId = r.get("userID")
    bl.confirmTourByUser(id, usrId)
    return Response(response=None, status=201, mimetype="application/json")

@tour.route("/tour/listCancel", methods=['GET'])
@cross_origin()
def getListCancel():
    r = request
    r = r.args
    size = int(r.get("size"))
    page = int(r.get("page"))
    result = bl.getListCancel(size, page)
    result = json.dumps(result, ensure_ascii=False)
    return Response(response=result, status=201, mimetype="application/json")