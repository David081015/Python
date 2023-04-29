from flask import Blueprint,request,jsonify,render_template
from models import Imagenes
from auth import tokenCheck
from sqlalchemy import exc
from app import db
import base64

imageUser = Blueprint('imageUser',__name__,template_folder="template")

def render_image(data):
    render_pic = base64.b64encode(data).decode('ascii')
    return render_pic

@imageUser.route("/displayImage",methods=["GET"])
@tokenCheck
def showImage(usuario):
    searchImage = Imagenes.query.filter_by(user_id=usuario['user_id']).first()
    if searchImage:
        image = searchImage.rendered_data
        return render_template('PerfilDeUsuario.html',{'img':image,'user':usuario})
    else:
        return jsonify({"message":"Imagen no encontrada"})