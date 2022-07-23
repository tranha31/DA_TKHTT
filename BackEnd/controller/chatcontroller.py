from flask import Blueprint, request
from flask.wrappers import Response
from bussiness.chatservice import ChatService
from flask_cors import CORS
from flask_cors.decorator import cross_origin
from flask import jsonify

chat = Blueprint("chat", __name__)
cors = CORS(chat, resources={r"/api/*": {"origins": "*"}})
chatservice = ChatService()


@chat.route("/message/chatroom", methods=['POST'])
@cross_origin()
def getChatRoomByUserID():
    _json = request.json
    UserID = _json["UserID"]

    result = chatservice.getChatRoomByUserID(UserID)

    return jsonify(result)


@chat.route("/message/createRoom", methods=['POST'])
@cross_origin()
def createNewChatRoom():
    _json = request.json
    UserID = _json["UserID"]

    result = chatservice.createNewChatRoom(UserID)

    return Response(response=result, status=200, mimetype="application/json")


@chat.route("/message/searchAll", methods=['GET'])
@cross_origin()
def getAllChatRoom():
    result = chatservice.loadAllChatRoom()

    return jsonify(result)


@chat.route("/message/searchAll", methods=['GET'])
@cross_origin()
def getAllChatRoomByAmount():
    args = request.args
    amount = args["amount"]

    result = chatservice.loadAllChatRoomByAmount(amount)

    return jsonify(result)
