import os
from flask import Flask, Blueprint, redirect,url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import basedir
from config import FILIAL

app = Flask(__name__)
app.config.from_object('config')


# Basic Routes #

@app.route('/')
def index():
    return redirect(url_for('auth.login'))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Banco de Dados
db = SQLAlchemy(app)

# Autenticação
login_manager = LoginManager()
login_manager.init_app(app)

# Modulos
from app import model
from app.controllers.auth.controllers import auth
from app.controllers.filial.controllers import filial
from app.controllers.usuario.controllers import usuario
from app.controllers.receitas.controllers import receitas
from app.controllers.despesas.controllers import despesas


app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(filial, url_prefix='/filial')
app.register_blueprint(usuario, url_prefix='/usuario')
app.register_blueprint(receitas, url_prefix='/receitas')
app.register_blueprint(despesas, url_prefix='/despesas')


