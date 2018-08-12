from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# initialize
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# models
class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=True)
    cost = db.Column(db.Integer, nullable=True)


# views
@app.route("/")
def hello():
    return "Hello World!"


@app.route("/name")
def name():
    return "Hello Frank"
