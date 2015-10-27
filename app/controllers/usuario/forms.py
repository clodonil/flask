from flask.ext.wtf import Form
from config import FILIAL
from wtforms import StringField, BooleanField, FloatField, IntegerField, DateField,TextAreaField, SelectField, FileField, PasswordField,validators
from wtforms.validators import DataRequired, EqualTo
from wtforms.ext.django.fields import QuerySetSelectField


class UserForm(Form):
     opcao=[]
     for f in FILIAL:
         opcao.append((f,f)) 
     nome       = StringField('Nome', validators=[DataRequired()])
     email      = StringField('E-Mail', validators=[DataRequired()])
     password   = StringField('Password', validators=[DataRequired()])
     password   = PasswordField('New Password', [validators.Required(), validators.EqualTo('confirm', message='Passwords must match')])
     confirm    = PasswordField('Repeat Password')
     filial_id = SelectField('Filiais', choices=[(h.id,h.nome) for h in Filial.query.all()],coerce=int)
     perfil     = SelectField('Perfil', choices=[("Operador","Operador"),("Gerente","Gerente")])

