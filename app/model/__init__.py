from app import db
from datetime import datetime
from flask.ext.login import LoginManager, login_user,UserMixin, logout_user
from sqlalchemy.sql.expression import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.dialects.postgresql import INET
from werkzeug import generate_password_hash, check_password_hash
from flask.ext.login import LoginManager, UserMixin, current_user, login_user, logout_user
from config import UPLOAD_FOLDER, FILIAL
import os



class Usuario(db.Model,UserMixin):
      id            = db.Column(db.Integer, primary_key=True)
      nome          = db.Column(db.String(100), index=True)
      email         = db.Column(db.String(100), unique=True, index=True)      
      password      = db.Column(db.String(100), index=True)      
      perfil        = db.Column(db.String(100), index=True)
      filial_id    = db.Column(db.Integer, db.ForeignKey('filial.id'))
      date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
      date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())


      def __repr__(self):
          return '<Usuario %r>' %(self.nome)


      def __init__(self,nome, email, password, perfil, filial_id):
          self.nome       = nome
          self.email      = email.lower()         
          self.set_password(password)
          self.perfil     = perfil
          self.filial_id     = filial_id

      
      def add(self,user):
          db.session.add(user)
          session_commit()
#          create_dir(user.filial.nome + '/' + user.nome)
          return True
          

      def update(self,src,dst):
          edit_dir(src,dst)
          return session_commit()


      def delete(self,user):
          path = user.empresa.nome + '/' + user.nome
          delete_dir(path)
          db.session.delete(user)
          return session_commit()
     
      def set_password(self, password):
          self.password = generate_password_hash(password)
   
      def check_password(self, password):
          return check_password_hash(self.password, password)

class Filial(db.Model):
      id            = db.Column(db.Integer, primary_key=True)
      nome          = db.Column(db.String(100), index=True)
      Usuario       = db.relationship('Usuario', backref='filial', lazy='dynamic')
      date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
      date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())


      def __repr__(self):
          return '<Filial %r>' %(self.nome)


      def __init__(self,nome):
          self.nome  = nome


      def get_id(self):
          return str(self.id)

      def add(self,filial):
          db.session.add(filial)
          create_dir(filial.nome)
          return session_commit()

      def update(self,src,dst):
          edit_dir(src,dst)
          return session_commit()

      def delete(self,nome):
          db.session.delete(nome)
          delete_dir(emp.nome)
          return session_commit()


class Despesas(db.Model):
      id            = db.Column(db.Integer, primary_key=True)
      fornecedor    = db.Column(db.String(100), index=True)
      finalidade    = db.Column(db.String(100), index=True)
      obs           = db.Column(db.String(100), index=True)
      dinheiro      = db.Column(db.Float, index=True)
      cheque        = db.Column(db.Float, index=True)
      cartao        = db.Column(db.Float, index=True)
      boleto        = db.Column(db.Float, index=True)
      data          = db.Column(db.Date, default=datetime.utcnow, index=True)
      usuario_id    = db.Column(db.Integer, db.ForeignKey('usuario.id'))
      filial        = db.Column(db.String(100), index=True)
      date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
      date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())


      def __repr__(self):
          return '<Despesas %r>' %(self.finalidade)


      def __init__(self,fornecedor,finalidade, obs, dinheiro, cheque, cartao, boleto,data):
          self.fornecedor  = fornecedor
          self.finalidade  = finalidade
          self.obs         = obs
          self.dinheiro    = dinheiro
          self.cheque      = cheque
          self.cartao      = cartao
          self.boleto      = boleto



      def get_id(self):
          return str(self.id)

      def add(self,dados):
          db.session.add(dados)
          return session_commit()

      def update(self):
          return session_commit()

      def delete(self,dados):
          db.session.delete(dados)
          return session_commit()

class Receitas(db.Model):
      id            = db.Column(db.Integer, primary_key=True)
      np            = db.Column(db.String(100), index=True)
      paciente      = db.Column(db.String(100), index=True)
      tipo_receita  = db.Column(db.String(100), index=True)
      dinheiro      = db.Column(db.Float, index=True)
      cheque        = db.Column(db.Float, index=True)
      cartao        = db.Column(db.Float, index=True)
      boleto        = db.Column(db.Float, index=True)
      data          = db.Column(db.Date, default=datetime.utcnow, index=True)
      usuario_id    = db.Column(db.Integer, db.ForeignKey('usuario.id'))
      filial        = db.Column(db.String(100), index=True)
      date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
      date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())


      def __repr__(self):
          return '<Receitas %r>' %(self.paciente)


      def __init__(self,data,np,paciente, tipo_receita, dinheiro, cheque, cartao, boleto):
          self.data         = data
          self.np           = np
          self.paciente     = paciente
          self.tipo_receita = tipo_receita
          self.dinheiro     = dinheiro
          self.cheque       = cheque
          self.cartao       = cartao
          self.boleto       = boleto
         

      def get_id(self):
          return str(self.id)

      def add(self,dados):
          db.session.add(dados)
          return session_commit()

      def update(self):
          return session_commit()

      def delete(self,dados):
          db.session.delete(dados)
          return session_commit()


#Universal functions

def  session_commit():
      try:
        db.session.commit()
      except SQLAlchemyError as e:             
         db.session.rollback()
         reason=str(e)
         return reason


def create_dir(path_dir):
    path = UPLOAD_FOLDER+"/"+ path_dir.lower()
    print(path)
    if not os.path.exists(path):
       os.makedirs(path)    

def delete_dir(path_dir):
    src_path = UPLOAD_FOLDER+"/"+ path_dir.lower()
    dst_path = UPLOAD_FOLDER+"/"+ path_dir.lower() + '_deletado'
    if os.path.exists(src_path):
       os.rename(src_path,dst_path)    

def edit_dir(src_path,dst_path):
    src_path = UPLOAD_FOLDER+"/"+ src_path.lower()
    dst_path = UPLOAD_FOLDER+"/"+ dst_path.lower()
    if os.path.exists(src_path):
       os.rename(src_path,dst_path)    

