from flask import Flask
from database import db
from encriptador import bcrypt
from flask_migrate import Migrate
from config import BasicConfig
from flask_cors import CORS
from routes.user.user import appuser

app = Flask(__name__)
app.register_blueprint(appuser)
app.config.from_object(BasicConfig)
CORS(app)
bcrypt.init_app(app)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)