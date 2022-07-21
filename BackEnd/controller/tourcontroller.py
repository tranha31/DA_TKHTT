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
def getAllDestination():
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
    bl.deleteTemplate(id)
    result = None
    return Response(response=result, status=200, mimetype="application/json")

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