from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:gr007,,@localhost/catalog'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


class Projet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    codeProjet = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(150), nullable=False)