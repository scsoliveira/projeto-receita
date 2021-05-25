from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates", static_folder="static")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:oh6zlppn5@localhost/l-es'

db = SQLAlchemy(app)

from receitas.controllers.main import *

db.create_all()

if __name__ == "__main__":
    app.run(debug=True)