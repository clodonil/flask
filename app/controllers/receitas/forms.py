#coding: utf-8
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, FloatField, IntegerField, DateField,TextAreaField, SelectField, FileField, PasswordField,validators, DateTimeField
from wtforms.validators import DataRequired, EqualTo
from wtforms.ext.django.fields import QuerySetSelectField
from app.model import Receitas
from datetime import datetime

class ReceitasForm(Form):
     np           = StringField('NP', validators=[DataRequired()])
     paciente     = StringField('Nome', validators=[DataRequired()])
     tipo_receita = SelectField('Tipo', choices=[('Tratamento','Tratamento'),('Raio X','Raio X')])
     dinheiro     = FloatField('Dinheiro',default=0.0)
     cheque       = FloatField('Cheque',default=0.0)
     cartao       = FloatField('Cartao',default=0.0)
     boleto       = FloatField('Boleto',default=0.0)
     data         = DateField("Until", format="%d/%m/%Y",default=datetime.today, validators=[validators.DataRequired()])


#DateField('data', validators=[DataRequired()],format='%d/%m/%Y')



