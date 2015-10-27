#!env/bin/python
from app import db
from app.model import Usuario, Filial
import datetime

f = Filial('São Paulo'); f.add(f)
f = Filial('Rio de Janeiro'); f.add(f)
f = Filial('Brasilia'); f.add(f)

user = Usuario('admin','admin@localhost','x','Gerente',1)
user.add(user)
