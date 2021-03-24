from flask import Flask, render_template, request, redirect, session, flash, url_for
app = Flask(__name__)

class Ingrediente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Receita:
    def __init__(self, id, nome, lIngredientes, lPassos):
        self.id = id
        self.nome = nome
        self.lIngredientes = lIngredientes
        self.lPassos = lPassos



ingrediente1 = Ingrediente(1,'Leite')
ingrediente2 = Ingrediente(2,'Fermento')
ingrediente3 = Ingrediente(3,'Ovo')
ingrediente4 = Ingrediente(4,'Sal')
ingrediente5 = Ingrediente(5,'Chocolate em pó')
ingrediente6 = Ingrediente(6,'Leite em pó')
ingrediente7 = Ingrediente(7,'Açucar')
ingrediente8 = Ingrediente(8,'Farinha')
ingrediente9 = Ingrediente(9,'Granulado')
ingrediente10 = Ingrediente(10, 'Cenoura')

lista = [ingrediente1, ingrediente2, ingrediente3, ingrediente4, ingrediente5, ingrediente6, ingrediente7, ingrediente8, ingrediente9, ingrediente10]

lIngredientesReceita1 = [ingrediente1, ingrediente2, ingrediente3, ingrediente7, ingrediente8, ingrediente10]
lPassosReceita1 = ["Misturar", "Descansar", "Assar", "Servir"]
receita1 = Receita(1, "Bolo de Cenoura", lIngredientesReceita1, lPassosReceita1)

lIngredientesReceita2 = [ingrediente1, ingrediente2, ingrediente3, ingrediente7, ingrediente8, ingrediente5, ingrediente9]
lPassosReceita2 = ["Misturar", "Descansar", "Assar", "Servir"]
receita2 = Receita(2, "Bolo de Chocolate", lIngredientesReceita2, lPassosReceita2)

lista2 = [receita1, receita2]


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/GerenciarIngrediente')
def GerenciarIngrediente():
    return render_template('ingredientes.html', titulo='Gerenciar Ingredientes', ingredientes=lista)

@app.route('/GerenciarReceitas')
def GerenciarReceitas():
    return render_template('receitas.html', titulo='Gerenciar Receitas', receitas=lista2)

if __name__ == "__main__":
    app.run(debug=True)