from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
# from forms import AccountReceivableForm, TestForm
from forms import *
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


@app.route('/testing', methods=['GET', 'POST'])
def testing():
    return render_template('tz.html', myvar='got the variable')


@app.route('/create.account')
def add_user():
    return render_template('register.html')


@app.route('/cash.receipt.book', methods=['GET','POST'])
def cash_receipt_b():
    accounts = Account.query.order_by(Account.account_name).all()

    account_forms = get_account_forms()
    for acc_form in account_forms:
        if acc_form.validate_on_submit():
            #Every form class must have a defined method to commit to DB

            # entry = models.Entry(client_id=, account_id=, cash=, date=,)
            # account_payable = models.AccountPayable(client_id=, transaction_id=, date=, or_number=, )
            print(0)
            user = User(username=account_forms[0].sold_to.data, email=account_forms[0].particulars.data)
            print(1)
            db.session.add(user)
            print(2)
            db.session.commit()
            print(3)
            return redirect('/')

    return render_template('cash_receipt_b.html', account_form=account_forms, accounts=accounts)


def get_account_forms():
    return [
        AccountReceivableForm(),
        TestForm()
    ]


if __name__ == '__main__':
    app.run(debug=True)