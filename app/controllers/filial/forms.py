from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, FloatField, IntegerField, DateField,TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired


class EmpForm(Form):
     nome       = StringField('Nome', validators=[DataRequired()])
     email      = StringField('email', validators=[DataRequired()])

