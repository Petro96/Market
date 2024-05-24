

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from api.views import blueprint
from extensions import db,login_manager,bcrypt,cors



app = Flask(__name__) 

app.config.from_object("config")

db.init_app(app)

app.app_context().push() # make app visible in terminal 

# make hash passwords
bcrypt.init_app(app)
# login 
login_manager.init_app(app)
login_manager.login_view = "login_page" # login required -> locate login page to allow it befor market page 
login_manager.login_message_category = "info" 
# register blueprint
app.register_blueprint(blueprint=blueprint)

cors.init_app(app, resources={r"/api/*":{
    "origins":["http://localhost"]
}})

from market import routes


