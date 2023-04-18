from flask import Flask
from flask_migrate import Migrate
from database import db
import logging
from config import BasicConfig,OtherConfig

from routes.imagen.imagenes import appimagen
from routes.producto.productos import approducto
from routes.persona.personas import appersona

app = Flask(__name__)
app.register_blueprint(appimagen)
app.register_blueprint(approducto)
app.register_blueprint(appersona)
app.config.from_object(BasicConfig)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)
logging.basicConfig(level=logging.DEBUG,filename="debug.log")