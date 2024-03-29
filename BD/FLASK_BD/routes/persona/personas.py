from flask import Blueprint, request, render_template, redirect,url_for
from models import Persona
from forms import PersonaForm
from app import db

appersona = Blueprint('appersona',__name__,template_folder="templates")

@appersona.route('/')
@appersona.route('/index')
def inicio():
    personas = Persona.query.all()
    totalDePersonas = Persona.query.count()
    return render_template('index.html',personas = personas, totalDePersonas = totalDePersonas)

@appersona.route('/agregar',methods=["GET","POST"])
def agregar():
    persona = Persona()
    personaForm = PersonaForm(obj=persona)
    if request.method == "POST":
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            db.session.add(persona)
            db.session.commit()
            return redirect(url_for('apppersona.inicio'))
    return render_template('agregar.html',forma=personaForm)

@appersona.route('/editar/<int:id>',methods=["GET","POST"])
def editar(id):
    persona = Persona.query.get_or_404(id)
    personaForm = PersonaForm(obj=persona)
    if request.method == "POST":
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            db.session.commit()
            return redirect(url_for('appersona.inicio'))
    return render_template('editar.html',forma=personaForm)

@appersona.route('/detalle/<int:id>')
def detalle(id):
    persona = Persona.query.get_or_404(id)
    return render_template('detalle.html',persona = persona)

@appersona.route('/eliminar/<int:id>')
def eliminar(id):
    persona = Persona.query.get_or_404(id)
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('appersona.inicio'))