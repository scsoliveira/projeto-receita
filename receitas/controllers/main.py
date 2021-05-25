import string
from ..app import app
from ..models.ingredientes import *
from ..models.ingredientes_receita import *
from ..models.receitas import *
from flask import render_template, request, jsonify

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/GerenciarIngrediente')
def GerenciarIngrediente():
    lista = Ingredientes.query.all()
    return render_template('ingredientes.html', titulo='Gerenciar Ingredientes', ingredientes=lista)

@app.route('/GerenciarIngrediente/Cadastrar', methods=['POST'])
def CadastrarIngrediente():

    nome = request.form['nome']

    if nome:
        i = Ingredientes(nome)
        db.session.add(i)
        db.session.commit()

        return jsonify({'nome' : nome})

    return jsonify({'error' : 'Erro ao inserir ao banco!'})

@app.route('/GerenciarIngrediente/Excluir', methods=['POST'])
def ExcluirIngrediente():

    id = request.form['id']

    i = Ingredientes.query.get(id)

    ir = Ingredientes_Receita.query.filter_by(id_ingrediente = id).all()

    if not ir:
        if i:
            db.session.delete(i)
            db.session.commit()

            return jsonify({'nome' : i.nome})

    return jsonify({'error' : 'Erro ao deleter!'})

@app.route('/GerenciarIngrediente/Editar', methods=['POST'])
def EditarIngrediente():

    id = request.form['id']
    nome = request.form['nome']

    i = Ingredientes.query.get(id)

    if i:
        i.nome = nome
        db.session.commit()

        return jsonify({'nome' : nome})

    return jsonify({'error' : 'Erro ao editar!'})


@app.route('/GerenciarReceitas')
def GerenciarReceitas():
    lista = Ingredientes.query.all()
    lista2 = Receitas.query.all()
    print(lista2)
    return render_template('receitas.html', titulo='Gerenciar Receitas', receitas=lista2, ingredientes=lista)

@app.route('/GerenciarReceitas/Cadastrar', methods=['POST'])
def CadastrarReceita():

    nome = request.form['nome']
    modo = request.form['modo']
    ingredientes = request.form.getlist("ingredientes[]")
    print(ingredientes)
    if nome:
        r = Receitas(nome, modo)
        for ingrediente in ingredientes:
            str = ingrediente.split("-") 
            ir = Ingredientes_Receita(str[0])
            ir.ingredientes = Ingredientes.query.get(str[1])
            r.ingredientes.append(ir)
        db.session.add(r)
        db.session.commit()

        return jsonify({'nome' : nome})

    return jsonify({'error' : 'Erro ao inserir ao banco!'})

@app.route('/GerenciarReceita/Excluir', methods=['POST'])
def ExcluirReceita():
    id = request.form['id']

    r = Receitas.query.get(id)

    ir = Ingredientes_Receita.query.filter_by(id_receita=id).delete(synchronize_session='fetch')

    if ir:
        db.session.delete(r)
        db.session.commit()

        return jsonify({'nome' : r.nome})

    return jsonify({'error' : 'Erro ao deleter!'})
    