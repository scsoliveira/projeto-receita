from ..app import db
from sqlalchemy import Column, Integer, String, Date, Boolean, Numeric, DATE, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship, backref

class Receitas(db.Model):
    __tablename__='receitas'

    id_receita = db.Column(db.Integer, primary_key = True, autoincrement=True)
    nome = db.Column(db.String(50))
    passo_a_passo = db.Column(db.String(250))
    ingredientes = relationship("Ingredientes_Receita", backref="receit")

    def __init__(self,nome, passo_a_passo):
        self.nome= nome
        self.passo_a_passo = passo_a_passo