import json
class Usuario():
    def __init__(cls,data):
        cls.id=data.id
        cls.nombre= data.nombre
        cls.apellido=data.apellido
        cls.email=data.email
        cls.tipo=data.tipo
        cls.posicion= data.posicion
        cls.borrado = data.borrado
    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))