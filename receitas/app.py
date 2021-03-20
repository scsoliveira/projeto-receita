from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/GerenciarIngrediente')
def GerenciarIngrediente():
    return "Hello world Ingrediente"

@app.route('/GerenciarReceitas')
def GerenciarReceitas():
    return "Hello world Receitas"