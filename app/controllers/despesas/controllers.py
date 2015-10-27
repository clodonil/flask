from flask import render_template, flash, redirect, request,session, redirect, Blueprint, url_for, session
from werkzeug import secure_filename
from app import db
from app.controllers.despesas.forms import DespesasForm
from app.model import Usuario,Despesas
from flask.ext.login import login_required
from config import FILIAL




despesas = Blueprint('despesas',__name__)

@despesas.route('/index')
@despesas.route('/')
@login_required
def index():
    session['tela'] = 'despesas'
    todos = Despesas.query.all() 
    return render_template('despesas/index.html',title='Lista de Despesas',todos=todos,FILIAL=FILIAL)


@despesas.route('/new', methods=['GET','POST'])
@login_required
def new():
    form = DespesasForm()
    if form.validate_on_submit():
       despesas = Despesas(
                           form.fornecedor.data,
                           form.finalidade.data,
                           form.obs.data,
                           form.dinheiro.data,                           
                           form.cheque.data,
                           form.cartao.data,
                           form.boleto.data,
                           form.data.data,
                          )
       despesas.add(despesas)
       return redirect(url_for('despesas.index'))
    return render_template('despesas/new.html',title='Cadastro de Despesas',form=form,FILIAL=FILIAL)

@despesas.route("/edit/<int:user_id>", methods = ["GET","POST"])
@login_required
def edit(user_id):
    despesas = Despesas.query.get(user_id)
    form = DespesasForm(obj=user)
    if form.validate_on_submit():
        despesas.fornecedor  = form.fornecedor.data,
        despesas.finalidade  = form.finalidade.data,
        despesas.obs         = form.obs.data
        despesas.dinheiro    = form.dinheiro.data
        despesas.cheque      = form.cheque.data
        despesas.cartao      = form.cartao.data
        despesas.boleto      = form.boleto.data
        despesas.data        = form.data.data  

        receita.update()
        return redirect(url_for('despesas.index'))
    return render_template("despesas/edit.html",title='Alterar de Despesas', form=form)

@despesas.route("/delete/<int:user_id>")
@login_required
def delete(user_id):
    despesas = Despesas.query.get(user_id)
 
    # Verificar se existe movimentação do usuário antes de apagar ou apagar todas as movimentacoes
    despesas.delete(receita)
    return redirect(url_for('despesas.index'))


