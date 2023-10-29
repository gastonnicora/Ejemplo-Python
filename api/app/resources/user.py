from flask import jsonify,  request, abort
from app.models.users import User
from app.helpers.serializacion import Serializacion
import json
from app.helpers.message import Message

def create(): 
    sms=User.create(request.get_json())
    print(sms)
    if sms is None:
        return jsonify(Message(error="no se pudo guardar el usuario").dump())
    return jsonify(sms.dump())