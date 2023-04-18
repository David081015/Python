from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PersonaForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()]) #Validators hace obligatorio el campo 
    apellido = StringField('Apellido')#No es obligatorio
    email = StringField('Email',validators=[DataRequired()]) 
    enviar =  SubmitField('Enviar')