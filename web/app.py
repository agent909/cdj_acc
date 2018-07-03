from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

DBdir = os.getcwd()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+DBdir.replace("\\","/")+'/sqlite/db1.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/dashboard')
def home():
    return render_template('index.html')


@app.route('/create.account')
def add_user():
    return render_template('register.html')


@app.route('/cash.receipt.book')
def cash_receipt_b():
    return render_template('cash_receipt_b.html')


if __name__ == '__main__':
    app.run(debug=True)
