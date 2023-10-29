from app.helpers.serializacion import Serializacion
class Message(object):
    def __init__(self,content=None,error=""):
        self.content=Serializacion.dump(content)
        self.error=error
    
    def dump(self):
        return Serializacion.dump(self)