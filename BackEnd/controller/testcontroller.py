from flask import Blueprint
from flask.wrappers import Response
from bussiness.testbl import TestBL
from flask_cors import CORS
from flask_cors.decorator import cross_origin
import json

test = Blueprint("test", __name__)
cors = CORS(test, resources={r"/api/*": {"origins": "*"}})
bl = TestBL()

@test.route("/test", methods=['GET'])
@cross_origin()
def testDB():
    result = bl.TestConnect()
    result = json.dumps(result, ensure_ascii=False)
    return Response(response=result, status=200, mimetype="application/json")

@test.route("/testmongo", methods=['POST'])
@cross_origin()
def testMongo():
    bl.TestMongo()
    return Response(status=201, mimetype="application/json")
