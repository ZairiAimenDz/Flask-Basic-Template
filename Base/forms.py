from flask_wtf import FlaskForm 
from wtforms import StringField , PasswordField,TextAreaField , FileField , SubmitField , BooleanField
from wtforms.validators import DataRequired , Length , Email , EqualTo , ValidationError
# Place Where You Put Your Form Classes