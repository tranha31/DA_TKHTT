from flask import Flask
from .tourcontroller import tour
from .authcontroller import auth
from .hotelcontroller import hotel
from .restaurantcontroller import restaurant
from .roomcontroller import room
from .destinationcontroller import destination
from .chatcontroller import chat


def create_app():
    app = Flask(__name__)
    app.register_blueprint(tour)
    app.register_blueprint(auth)
    app.register_blueprint(hotel)
    app.register_blueprint(restaurant)
    app.register_blueprint(room)
    app.register_blueprint(destination)
    app.register_blueprint(chat)
    return app
