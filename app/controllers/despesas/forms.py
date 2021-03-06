#coding: utf-8
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, FloatField, IntegerField, DateField,TextAreaField, SelectField, FileField, PasswordField,validators
from wtforms.validators import DataRequired, EqualTo
from wtforms.ext.django.fields import QuerySetSelectField
from app.model import Despesas
from datetime import datetime

class DespesasForm(Form):
     fornecedor   = StringField('Fornecedor', validators=[DataRequired()])
     finalidade   = StringField('NP', validators=[DataRequired()])
     obs          = StringField('Nome', validators=[DataRequired()])
     dinheiro     = FloatField('Dinheiro', default=0.0)
     cheque       = FloatField('Cheque', default=0.0)
     cartao       = FloatField('Cartao', default=0.0)
     boleto       = FloatField('Boleto', default=0.0)
     data         = DateField("Until", format="%d/%m/%Y",default=datetime.today, validators=[validators.DataRequired()])



