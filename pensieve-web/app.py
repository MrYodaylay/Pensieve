from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)

login = LoginManager()
login.init_app(app)


@app.route("/")
def index():
    return "Hello World"


@app.route("/home")
def home():
    return "Logged in"
