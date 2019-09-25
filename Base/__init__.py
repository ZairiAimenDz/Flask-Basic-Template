from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey' #Put A Better Secret Key
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
LogMan = LoginManager(app)
LogMan.login_view = 'login'
LogMan.login_message_category = 'info'



from Base import routes
