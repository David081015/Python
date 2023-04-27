from flask import Blueprint,request,jsonify
from sqlalchemy import exc
from models import Usuario
from app import db,bcrypt
from auth import tokenCheck

appuser = Blueprint('appuser',__name__,template_folder='templates')

@appuser.route('/registro',methods=["POST"])
def registro():
    user = request.get_json()
    userExists = Usuario.query.filter_by(email=user['email']).first()
    if not userExists:
        usuario = Usuario(email=user['email'],password=user['password'])
        try:
            db.session.add(usuario)
            db.session.commit()
            mensaje = "Usuario creado"
        except exc.SQLAlchemyError as e:
            mensaje = e
    else:
        mensaje = "Usuario existe"
    return jsonify({"message":mensaje})