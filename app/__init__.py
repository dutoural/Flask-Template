from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config.config import DB_secretKey,DB_path

app = Flask(__name__)

app.config['SECRET_KEY'] = DB_secretKey
app.config['SQLALCHEMY_DATABASE_URI'] = DB_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app import routes


