from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.schema import ForeignKey
from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID


db = SQLAlchemy()

class Usuario(db.Model):
    uuid= db.Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=True
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
        db.Integer
    )
    borrado =db.Column(
        db.Integer,
        nullable=True,
        default=0
    )
    dateOfCreate=db.Column(
        db.Integer,
        nullaable=True
    )
    terms=db.Column(
        db.integer,
        nullable=True,
        default=0
    )
    