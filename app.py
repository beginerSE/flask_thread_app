from flask import Flask, request, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

db_uri = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)

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


@app.route("/")
def bbs():
    text = Article.query.all()
    return render_template("index.html", lines = text)

@app.route("/thread", methods=["POST"])
def thread():
    thread_get = request.form["thread"]
    threads = Thread.query.all()
    thread_list = []
    threads = Thread.query.all()
    for th in threads:
        thread_list.append(th.threadname)
        if thread_get in thread_list:
            thread = Thread.query.filter_by(threadname=thread_get).first()
            articles = Article.query.filter_by(thread_id=thread.id).all()
            return render_template("thread.html",articles=articles,thread=thread_get)
        else:
            thread_new = Thread(thread_get)
            db.session.add(thread_new)
            db.session.commit()
            articles = Article.query.filter_by(thread_id=thread_new.id).all()
            return render_template("thread.html",
            articles=articles,
            thread=thread_get)

@app.route("/result", methods=["POST"])
def result():
    date = datetime.now()
    article = request.form["article"]
    name = request.form["name"]
    admin = Article(pub_date=date, name=name, article=article)
    db.session.add(admin)
    db.session.commit()
    return render_template("result.html", article=article, name=name, now=date)

if __name__ == "__main__":
    app.run(debug=True)
