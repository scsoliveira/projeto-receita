from ..app import db
from sqlalchemy import Column, Integer, String, Date, Boolean, Numeric, DATE, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship, backref

class Ingredientes(db.Model):
    __tablename__='ingredientes'

    id_ingrediente = db.Column(db.Integer, primary_key = True, autoincrement=True)
    nome = db.Column(db.String(50))

    def __init__(self,nome):
        self.nome = nome