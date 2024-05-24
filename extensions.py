
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS

db = SQLAlchemy()
ma = Marshmallow()
login_manager = LoginManager()
bcrypt = Bcrypt()
cors = CORS()