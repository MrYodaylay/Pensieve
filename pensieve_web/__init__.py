from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from argon2 import PasswordHasher

app = Flask(__name__)
app.secret_key = "I1Cvp1JWEFIFUiPEzEcX15axTJJ63HDiDGlX0BG6lvY"
app.template_folder = "template"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///webapp.db"


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)

with app.app_context():
    db.create_all()

ph = PasswordHasher()

import pensieve_web.views
import pensieve_web.models
