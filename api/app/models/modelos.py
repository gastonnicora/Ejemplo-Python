from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.schema import ForeignKey
from datetime import datetime



db = SQLAlchemy()

class Usuario(db.Model):
    id= db.Column(
        db.Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable=True
        )
    nombre= db.Column(
        db.String(255),
        nullable= True
        )
    apellido= db.Column(
        db.String(255),
        nullable= True
        )
    email= db.Column(
        db.String(255),
        nullable=True
        )
    contra = db.Column(
        db.String(255),
        nullable= True,
    ) 
    tipo= db.Column(
        db.Integer,
        nullable= True,
    )
    posicion= db.Column(
        db.Integer
    )
    borrado =db.Column(
        db.Integer,
        nullable=True,
        default=0
    )
    
class Video(db.Model):
    id= db.Column(
        db.Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable= True
    ) 
    nombre=db.Column(
        db.String(255),
        nullable=True
    )
    
class Ejercicio(db.Model):
    id= db.Column(
        db.Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable=True
        )
    nombre= db.Column(
        db.String(255),
        nullable=True
    )
    descripcion= db.Column(
        db.String(255)
    )
    tiempo= db.Column(
        db.Integer
    )
    repeticiones= db.Column(
        db.Integer
    )
    tipo_tiempo= db.Column(
        db.String(255)
    )
    tipo = db.Column(
        db.Integer,
        nullable= True
    )
    categoria = db.Column(
        db.Integer,
        nullable= True
    )
    video = db.Column(
        db.Integer,
        ForeignKey(Video.id),
        nullable= True
    ) 
    entrenador = db.Column(
        db.Integer,
        ForeignKey(Usuario.id),
        nullable= True
    )
    publico =db.Column(
        db.Integer,
        nullable=True,
        default=0
    )
    borrado =db.Column(
        db.Integer,
        nullable=True,
        default=0
    )
    
class Entrenamiento(db.Model):
    id= db.Column(
        db.Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable= True
    )
    nombre= db.Column(
        db.String(255),
        nullable= True
    )
    descripcion= db.Column(
        db.String(255)
    )
    borrado = db.Column(
        db.Integer,
        nullable= True,
        default=0
    )
    tipo = db.Column(
        db.Integer,
        nullable= True,
        default=0
    )
    fecha= db.Column(
        db.String(255),
        nullable=True
    )
    entrenador= db.Column(
        db.Integer,
        ForeignKey(Usuario.id),
        nullable= True
    )
 
    
class Ent_eje(db.Model):
    id= db.Column(
        db.Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable= True
    )   
    ent= db.Column(
        db.Integer,
        ForeignKey(Entrenamiento.id),
        nullable= True
        )
    eje= db.Column(
        db.Integer,
        ForeignKey(Ejercicio.id),
        nullable= True
    )
    
class Notificacion(db.Model):
    id= db.Column(
        db.Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable= True
    ) 
    fecha= db.Column(db.DateTime(timezone=True),
                              default=datetime.today(),
                              onupdate=datetime.today())
    entrenador= db.Column(
        db.Integer,
        ForeignKey(Usuario.id),
        nullable= True
        )
    contenido= db.Column(
        db.String(255),
        nullable= True
    )
    borrado = db.Column(
        db.Integer,
        nullable= True,
        default=0
    )
    
class Notificacion_alumno(db.Model):
    id= db.Column(
        db.Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable= True
    )   
    alumno= db.Column(
        db.Integer,
        ForeignKey(Usuario.id),
        nullable= True
        )
    notificacion= db.Column(
        db.Integer,
        ForeignKey(Notificacion.id),
        nullable= True
    )
    visto=db.Column(
        db.Integer,
        nullable=True,
        default=0
    )
        
class Ent_alu(db.Model):
    id= db.Column(
        db.Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable= True
    )   
    ent= db.Column(
        db.Integer,
        ForeignKey(Entrenamiento.id),
        nullable= True
    )
    alu= db.Column(
        db.Integer,
        ForeignKey(Usuario.id),
        nullable=True
    )
    coment_jug=db.Column(
        db.String
    )
    asistencia=db.Column(
        db.Integer,
        nullable=True,
        default=0
    )
    nota=db.Column(
        db.Integer
    ) 
    coment_ent= db.Column(
        db.String
    )   
   
 
    
class Config(db.Model):
    id= db.Column(
        db.Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable= True
    ) 
    us= db.Column(
        db.Integer,
        ForeignKey(Usuario.id),
        nullable=True
    )
    tema= db.Column(
        db.Integer,
        nullable=True,
        default=1
    )
    
class Entrenador_alumno(db.Model):
    id= db.Column(
        db.Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable= True
    ) 
    entrenador= db.Column(
        db.Integer,
        ForeignKey(Usuario.id),
        nullable=True
    )
    alumno= db.Column(
        db.Integer,
        ForeignKey(Usuario.id),
        nullable=True
    )
    