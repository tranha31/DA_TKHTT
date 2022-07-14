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

    result = authservice.register(email, password, username, phone)

    return Response(response=result, status=200, mimetype="application/json")
