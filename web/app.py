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


@app.route('/cash.receipt.book', methods=['GET', 'POST'])
def cash_receipt_b():
    accounts = Account.query.order_by(Account.account_name).all()

    account_form = get_account_forms()

    # for acc_form in account_form:
    #     if acc_form.validate_on_submit():
    #
    #         # Every form class must have a defined method to commit to DB
    #
    #         # entry = models.Entry(client_id=, account_id=, cash=, date=,)
    #         # account_payable = models.AccountPayable(client_id=, transaction_id=, date=, or_number=, )
    #
    #         print(0)
    #         user = User(username=account_form[0].sold_to.data, email=account_form[0].particulars.data)
    #         print(1)
    #         db.session.add(user)
    #         print(2)
    #         db.session.commit()
    #         print(3)
    #         return redirect('/')
    # if account_form[0].validate_on_submit():
    #     print('Form 1 is valid')
    # elif account_form[1].validate_on_submit():
    #     print('Form 2 is valid bro')
    # else:
    #     print('invalid input')
    print(account_form[0].sold_to.data)
    print(account_form[1].sold_to_someone.data)
    print(account_form[0].account_id.data)
    print(account_form[1].account_id.data)

    return render_template('cash_receipt_b.html', account_form=account_form, accounts=accounts)


def get_account_forms():
    return [
        AccountReceivableForm(),
        AccountReceivableForm2()
    ]


if __name__ == '__main__':
    app.run(debug=True)
