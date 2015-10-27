from flask import render_template, flash, redirect, request,session, redirect, Blueprint, url_for
from werkzeug import secure_filename
from app import db
from app.controllers.filial.forms import EmpForm
from app.model import Filial
from flask.ext.login import login_required
import os



filial = Blueprint('filial',__name__)

@filial.route('/index')
@filial.route('/')
@login_required
def index():
    todos = Filial.query.all()
 
    return render_template('filial/index.html',title='Lista de Filiais',todos=todos)


@filial.route('/new', methods=['GET','POST'])
@login_required
def new():
    form = EmpForm()
    if form.validate_on_submit():
       emp = Filial(
                           nome   = form.nome.data,
                          )
       emp.add(emp)
       return redirect(url_for('filial.index'))
    return render_template('filial/new.html',title='Cadastro de Filiais',form=form)

@filial.route("/edit/<int:emp_id>", methods = ["GET","POST"])
@login_required
def edit(emp_id):
    emp = Filial.query.get(emp_id)
    src_path = emp.nome
    form = EmpForm(obj=emp)
    if form.validate_on_submit():
       emp.nome       = form.nome.data
       emp.update(src_path,emp.nome)
       return redirect(url_for('empresa.index'))
    return render_template("filial/edit.html",title='Alterar de Empresa', form=form)

@filial.route("/delete/<int:emp_id>")
@login_required
def delete(emp_id):
    emp = Filial.query.get(emp_id)
    if len(emp.Usuario.all()) == 0:
       emp.delete(emp)
    return redirect(url_for('empresa.index'))



