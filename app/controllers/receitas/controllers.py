from flask import render_template, flash, redirect, request,session, redirect, Blueprint, url_for,session
from werkzeug import secure_filename
from app import db
from app.controllers.receitas.forms import ReceitasForm
from app.model import Usuario,Receitas
from flask.ext.login import login_required,current_user
from datetime import datetime
from config import FILIAL



receitas = Blueprint('receitas',__name__)

@receitas.route('/index')
@receitas.route('/')
@login_required
def index():
    # Se o usuário corrente é o operador
    if current_user.perfil == "Operador":
        # Recupera a data de hoje
        hoje  = datetime.today()
        hoje  = hoje.strftime('%Y/%m/%d')

        # Pesquisa apenas os registro de hoje
        todos = Receitas.query.filter(Receitas.data == hoje).all()
        session['tela'] = "receitas"
    else:
        todos = Receitas.query.all() 
    return render_template('receitas/index.html',title='Lista de Receitas',todos=todos)


@receitas.route('/new', methods=['GET','POST'])
@login_required
def new():
    form = ReceitasForm()
    if form.validate_on_submit():
       receitas = Receitas(
                           form.data.data,
                           form.np.data,
                           form.paciente.data,                           
                           form.tipo_receita.data,
                           form.dinheiro.data,
                           form.cheque.data,
                           form.cartao.data,
                           form.boleto.data,
                          )
       receitas.usuario_id = current_user.id
       receitas.filial = current_user.filial
       receitas.add(receitas)
       return redirect(url_for('receitas.index'))
    return render_template('receitas/new.html',title='Cadastro de Receitas',form=form)

@receitas.route("/edit/<int:user_id>", methods = ["GET","POST"])
@login_required
def edit(user_id):
    receita = Receitas.query.get(user_id)
    form = UserForm(obj=user)
    if form.validate_on_submit():
        receita.paciente     = form.paciente.data,
        receita.tipo_receita = form.tipo_receita.data
        receita.dinheiro     = form.dinheiro.data
        receita.cheque       = form.cheque.data
        receita.cartao       = form.cartao.data
        receita.boleto       = form.boleto.data

        receita.update()
        return redirect(url_for('receitas.index'))
    return render_template("receita/edit.html",title='Alterar de Receitas', form=form)

@receitas.route("/delete/<int:user_id>")
@login_required
def delete(user_id):
    receita = Receitas.query.get(user_id)
 
    # Verificar se existe movimentação do usuário antes de apagar ou apagar todas as movimentacoes
    receita.delete(receita)
    return redirect(url_for('receitas.index'))


