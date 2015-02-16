from flask_wtf import Form 
from wtforms import StringField
from wtforms.validators import DataRequired

class Usuario(Form):
    nome = StringField('nome', validators=[DataRequired()])
    