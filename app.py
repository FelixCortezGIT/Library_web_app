import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
print(os.getenv("DATABASE_URL"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)

class Author(db.Model):
    __tablename__ = "authors"
    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    bio = db.Column(db.String)

@app.route("/")
def home():
    return "home page"

@app.route("/authors")
def authors():
    authors = Author.query.all()
    return render_template("index.html", authors=authors)

if __name__ == "__main__":
    app.run(debug=True)
