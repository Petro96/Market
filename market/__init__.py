

from flask import Flask,render_template,redirect,request,url_for;
from flask_sqlalchemy import SQLAlchemy

import os

#file_path = os.path.abspath(os.getcwd())+"\market.db"

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path


app = Flask(__name__) # instance of Flask

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' # config of database

# secret key: d0d1a648ef9f8b5136348fd0 because of CSRF - cross site request forgery

app.config['SECRET_KEY'] = 'd0d1a648ef9f8b5136348fd0' # form config of secret key

db = SQLAlchemy(app) # instance DB

app.app_context().push()

from market import routes