from flask import Flask, request, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


SQLALCHEMY_TRACK_MODIFICATIONS = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#SQLAlchemyでデータベースに接続する
db_uri = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)

#データベースの仕様をクラスで定義する
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_date = db.Column(db.DateTime, nullable=False,
    default=datetime.utcnow)
    name = db.Column(db.Text())
    article = db.Column(db.Text())

def __init__(self, pub_date, name, article):
    self.pub_date = pub_date
    self.name = name
    self.article = article

db.create_all()
