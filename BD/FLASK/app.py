from flask import Flask,request,render_template, url_for, jsonify, session
import logging
from werkzeug.utils import redirect
from werkzeug.exceptions import abort
#Se crea la app
app = Flask(__name__)
app.secret_key="llave_secreta"
logging.basicConfig(filename='error.log',level=logging.DEBUG)

@app.route('/')
def inicio():
    if 'username' in session:
        return render_template('inicio.html')
    else:
        return redirect(url_for('login'))

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        usuario = request.form["username"]
        session["username"]=usuario
        return redirect(url_for('inicio'))
    return render_template('Login.html')

@app.route('/salir')
def salir():
    session.pop('username')
    return redirect(url_for('login'))

@app.route("/juego",methods={"POST"})
def insertarJuego():
    print(request.headers)
    token = request.headers.get('token')
    body = request.get_json()
    nombre = body["nombre"]
    precio = body["precio"]
    calificacion = body["calificacion"]
    return f'Juego recibido {token} {nombre} {precio} {calificacion}'

@app.route("/juego/<int:id>")
def obtenerJuego(id):
    juegos = [
        {"nombre":"ejemplo1","precio":80,"calificacion":95.5},
        {"nombre":"ejemplo2","precio":90,"calificacion":100}]
    return jsonify(juegos[id])

@app.errorhandler(404)
def paginaNoEncontrada(error):
    return render_template('error404.html', error=error),404