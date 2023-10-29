from sqlalchemy.sql.schema import ForeignKey
import uuid
from sqlalchemy.dialects.postgresql import UUID
from app.models.db import db
from app.helpers.modelo import User  as U
from app.helpers.message import Message
import datetime
from werkzeug.security import check_password_hash as checkph
from werkzeug.security import generate_password_hash as genph


class User(db.Model):
    uuid= db.Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=True, unique=True
        )
    name= db.Column(
        db.String(255),
        nullable= True
        )
    lastName= db.Column(
        db.String(255),
        nullable= True
        )
    email= db.Column(
        db.String(255),
        nullable=True
        )
    password = db.Column(
        db.String(255),
        nullable= True,
    ) 
    birthdate= db.Column(
        db.String(255),
        nullable=True
    )
    removed =db.Column(
        db.Integer,
        nullable=True,
        default=0
    )
    dateOfCreate=db.Column(
        db.String(255),
        nullable=True
    )
    terms=db.Column(
        db.Integer,
        nullable=True,
        default=1
    )

    @classmethod
    def create(cls,data):
        date= datetime.datetime.now()
        strDate= date.strftime("%x")
        usu= cls.existEmail(data.get("email"))
        if usu is not None:
            return Message(error="El email ya fue registrado").dump()
        user= cls(
                name= data.get("name"), 
                lastName= data.get("lastName"),
                email= data.get("email"),
                password = genph(data.get("password")), 
                birthdate= data.get("birthdate"), 
                dateOfCreate= strDate
            )
        
        db.session.add(user)
        db.session.commit()
        usuario= U(user)
        db.session.close()
        return Message(content=usuario).dump()
    
    @classmethod
    def all(cls):
        users=cls.query.filter_by(borrado=0).all()  
        db.session.close()
        return users
    
    @classmethod
    def get(cls,id):
        user= cls.query.filter_by(id=id,borrado=0).first()
        db.session.close()
        return user
    
    @classmethod
    def update(cls,data):
        user= cls.get(data.get("id"))
        if user is None:
            return None
        user.nombre= data.get("nombre")
        user.apellido= data.get("apellido")
        user.email= data.get("email")
        user.contra = data.get("contra") 
        user.tipo= data.get("tipo") 
        user.posicion= data.get("posicion") 
        db.session.merge(user)
        db.session.commit() 
        usuario= U(user)
        db.session.close()
        return usuario
    
        
    @classmethod
    def delete(cls,id):
        usuario = cls.get(id)
        if usuario is None:
            return 400
        usuario.borrado=1
        db.session.merge(usuario)
        db.session.commit()
        db.session.close()
        return 200
     
    @classmethod
    def get_in_list(cls,list):
        usuarios = db.session.query(cls).filter(cls.id.in_(list),cls.borrado==0).all()
        return usuarios 
    
    @classmethod
    def not_in_list(cls,list):
        usuarios = db.session.query(cls).filter(cls.id.notin_(list),cls.borrado==0,cls.tipo==1).all()
        return usuarios 
    
    @classmethod
    def login(cls,data):
        usuario = cls.query.filter_by(email= data.get("email"),contra=data.get("contra"),borrado=0).first()
        db.session.close()
        return usuario
    
    @classmethod
    def existEmail(cls,email):
        usuario = cls.query.filter_by(email=email, removed=0).first()
        db.session.close()
        return usuario
    
    @classmethod
    def alumnos(cls):
        usuarios= cls.query.filter_by(borrado= 0,tipo=1).all() 
        db.session.close()
        return usuarios
    
    @classmethod
    def update_pass(cls,data):
        user= cls.get(data.get("id"))
        sms=""
        if user is None:
            return {"error":"No se pudo editar la contraseña por que el id no existe"}
        if user.contra==data.get("contra"):
            if data.get("new_contra")==data.get("rp_contra"):
                user.contra = data.get("new_contra") 
                db.session.merge(user)
                db.session.commit() 
                db.session.close()
                sms="La contraseña se actualizo con exito"
            else:
                sms={"error":"Los campos Nueva contraseña y Repita la contraseña no coinciden"}
        else:
            sms={"error":"Error al ingresar la contraseña antigua"}
        return sms
