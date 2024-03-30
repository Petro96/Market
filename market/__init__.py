

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

import os

#file_path = os.path.abspath(os.getcwd())+"\market.db"

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path


app = Flask(__name__) # instance of Flask

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' # config of database

# secret key: d0d1a648ef9f8b5136348fd0 because of CSRF - cross site request forgery

app.config['SECRET_KEY'] = 'd0d1a648ef9f8b5136348fd0' # form config of secret key

db = SQLAlchemy(app) # instance DB

app.app_context().push() # make app visible in terminal 

# make hash passwords

bcrypt = Bcrypt(app)

# login 

login_manager = LoginManager(app)

login_manager.login_view = "login_page" # login required -> locate login page to allow it befor market page 
login_manager.login_message_category = "info" 


from market import routes