from ..app import db
from sqlalchemy import Column, Integer, String, Date, Boolean, Numeric, DATE, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship, backref

class Ingredientes_Receita(db.Model):
    __tablename__='ingredientes_receita'

    id_ingrediente_receita = db.Column(db.Integer, primary_key = True, autoincrement=True)
    id_receita = db.Column(db.Integer, ForeignKey('receitas.id_receita'))
    id_ingrediente = db.Column(db.Integer, ForeignKey('ingredientes.id_ingrediente'))
    qtd = db.Column(db.String(30))
    receita = relationship("Receitas", backref="ingredient")
    ingredientes = relationship("Ingredientes", backref="receit")

    def __init__(self,qtd):
        self.qtd = qtd