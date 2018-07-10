from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import AccountReceivableForm
import os


from models import *

app = Flask(__name__)
DB_directory = os.getcwd()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+DB_directory.replace("\\", "/")+'/sqlite/data.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'julius'
db = SQLAlchemy(app)


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
    return render_template('cash_receipt_b.html', account_form=idk())


def idk():
    return [AccountReceivableForm()]


if __name__ == '__main__':
    app.run(debug=True)
