from flask import render_template, flash, redirect, request,session, redirect, Blueprint, url_for, session
from werkzeug import secure_filename
from app import db
from app.controllers.usuario.forms import UserForm
from app.model import Usuario
from flask.ext.login import login_required
from config import FILIAL




usuario = Blueprint('usuario',__name__)

@usuario.route('/index')
@usuario.route('/')
@login_required
def index():
    session['tela'] = "usuario"
    todos = Usuario.query.all()
 
    return render_template('usuario/index.html',title='Lista de Usuario',todos=todos)


@usuario.route('/new', methods=['GET','POST'])
@login_required
def new():
    form = UserForm()
    if form.validate_on_submit():
       user = Usuario(
                           nome       = form.nome.data,
                           email      = form.email.data,
                           password   = form.password.data,
                           perfil     = form.perfil.data,
                           filial     = form.filial.data
                          )
       user.add(user)
       return redirect(url_for('usuario.index'))
    return render_template('usuario/new.html',title='Cadastro de Usuario',form=form)

@usuario.route("/edit/<int:user_id>", methods = ["GET","POST"])
@login_required
def edit(user_id):
    user = Usuario.query.get(user_id)
    src_path = user.empresa.nome + '/' + user.nome
    form = UserForm(obj=user)
    if form.validate_on_submit():
       user.nome       = form.nome.data
       user.email      = form.email.data
       user.password   = form.password.data
       user.filial     = form.filial.data

       dst_path = Empresa.query.get(user.filial_id).nome + "/" + user.nome

       user.update(src_path, dst_path)
       return redirect(url_for('usuario.index'))
    return render_template("usuario/edit.html",title='Alterar de Empresa', form=form)

@usuario.route("/delete/<int:user_id>")
@login_required
def delete(user_id):
    user = Usuario.query.get(user_id)
 
    # Verificar se existe movimentação do usuário antes de apagar ou apagar todas as movimentacoes
    user.delete(user)
    return redirect(url_for('usuario.index'))


