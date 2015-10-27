import os

WTF_CSRF_ENABLED=True
SECRET_KEY = "you-will-never-guess"

WTF_CSRF_ENABLED=True
SECRET_KEY = "you-will-never-guess"

FILIAL = ('Brasilia','Rio de Janeiro','São Paulo')

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/banco_de_dados.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

DEBUG = True

# upload_documentos

UPLOAD_FOLDER = os.path.join(basedir,"app/static/docs_repository")
