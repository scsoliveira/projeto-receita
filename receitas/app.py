from flask import Flask, render_template, request, redirect, session, flash, url_for
from models import ingrediente, receita
app = Flask(__name__, template_folder="templates", static_folder="static")

# TESTES
ingrediente1 = ingrediente.Ingrediente(1,'Leite', '100ml')
ingrediente2 = ingrediente.Ingrediente(2,'Fermento', '150g')
ingrediente3 = ingrediente.Ingrediente(3,'Ovo', '2')
ingrediente4 = ingrediente.Ingrediente(4,'Sal', '200g')
ingrediente5 = ingrediente.Ingrediente(5,'Chocolate em pó', '400g')
ingrediente6 = ingrediente.Ingrediente(6,'Leite em pó', '500g')
ingrediente7 = ingrediente.Ingrediente(7,'Açucar', '300g')
ingrediente8 = ingrediente.Ingrediente(8,'Farinha', '500g')
ingrediente9 = ingrediente.Ingrediente(9,'Granulado', '300g')
ingrediente10 = ingrediente.Ingrediente(10, 'Cenoura', '3')

lista = [ingrediente1, ingrediente2, ingrediente3, ingrediente4, ingrediente5, ingrediente6, ingrediente7, ingrediente8, ingrediente9, ingrediente10]

lIngredientesReceita1 = [ingrediente1, ingrediente2, ingrediente3, ingrediente7, ingrediente8, ingrediente10]
lPassosReceita1 = ["Misturar", "Descansar", "Assar", "Servir"]
receita1 = receita.Receita(1, "Bolo de Cenoura", lIngredientesReceita1, lPassosReceita1)

lIngredientesReceita2 = [ingrediente1, ingrediente2, ingrediente3, ingrediente7, ingrediente8, ingrediente5, ingrediente9]
lPassosReceita2 = ["Misturar", "Descansar", "Assar", "Servir"]
receita2 = receita.Receita(2, "Bolo de Chocolate", lIngredientesReceita2, lPassosReceita2)

lista2 = [receita1, receita2]

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/GerenciarIngrediente')
def GerenciarIngrediente():
    return render_template('ingredientes.html', titulo='Gerenciar Ingredientes', ingredientes=lista)

@app.route('/GerenciarReceitas')
def GerenciarReceitas():
    return render_template('receitas.html', titulo='Gerenciar Receitas', receitas=lista2, ingredientes=lista)

if __name__ == "__main__":
    app.run(debug=True)