from flask import Flask,jsonify, request, render_template
from flask_cors import CORS
from os import path, environ
from config import config
from app import db_config
from app.models.modelos import db


from app.socket.socketio import socketio


def create_app(environment="development"):
    # Configuración inicial de la app
    app = Flask(__name__) 
    app.config['CORS_HEADERS'] = 'Content-Type'
    cors = CORS(app)

    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])
    
    socketio.init_app(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = db_config.connection(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
 
    
    @app.route("/")
    def home():
        return render_template("home.html")

    
    return app 