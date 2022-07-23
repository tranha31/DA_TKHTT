from email.headerregistry import Address
from flask import Blueprint, request
from flask.wrappers import Response
from bussiness.authservice import AuthService
from flask_cors import CORS
from flask_cors.decorator import cross_origin
from flask import jsonify

auth = Blueprint("auth", __name__)
cors = CORS(auth, resources={r"/api/*": {"origins": "*"}})
authservice = AuthService()


@auth.route("/auth/login", methods=['POST'])
@cross_origin()
def loginUser():
    _json = request.json
    email = _json['email']
    password = _json['password']

    result = authservice.validateLogin(email, password)

    if (type(result) == str):
        return Response(response=result, status=200, mimetype="application/json")
    else:
        return jsonify(result)


@auth.route("/auth/register", methods=['POST'])
@cross_origin()
def registerNewUser():
    _json = request.json
    email = _json['email']
    password = _json['password']
    username = _json['username']
    phone = _json['phone']
    identify = _json['identify']
    name = _json['name']
    address = _json['address']
    sign = _json['sign']
    result = authservice.register(email, password, username, phone, identify, name, address, sign)

    return Response(response=result, status=200, mimetype="application/json")

@auth.route("/auth/getUserById", methods=['POST'])
@cross_origin()
def getUserById():
    _json = request.json
    UserID = _json['UserID']

    result = authservice.getUserInformationsById(UserID)

    return jsonify(result)


@auth.route("/auth/updateUserInfos", methods=['POST'])
@cross_origin()
def updateUserInfos():
    _json = request.json
    UserID = _json['UserID']
    Email = _json['Email']
    PhoneNumber = _json['PhoneNumber']
    Identify = _json['Identification']
    Name = _json["Name"]
    Address = _json["Address"]

    result = authservice.updateGeneralInformations(UserID, Email, PhoneNumber, Identify, Name, Address)

    return Response(response=result, status=200, mimetype="application/json")


@auth.route("/auth/updatePassword", methods=['POST'])
@cross_origin()
def updatePassword():
    _json = request.json
    UserID = _json['UserID']
    Password = _json['Password']

    result = authservice.updatePassword(UserID, Password)

    return Response(response=result, status=200, mimetype="application/json")