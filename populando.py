#!env/bin/python
from app import db
from app.model import Usuario
import datetime



user = Usuario('admin','admin@localhost','x','Gerente','São Paulo')
user.add(user)
