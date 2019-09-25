from Base import app ,db , bcrypt
from flask import render_template , url_for , flash  , redirect , request 
from flask_login import login_user , current_user , logout_user , login_required

@app.route('/')
def home():
     flash('This Is A Random Flashed Message So You Know How to do them', 'info')
     return render_template('index.html',title='Home page')

#Place For Routes