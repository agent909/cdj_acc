from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import *
import os
import sqlite3

from models import *


app = Flask(__name__)
DB_directory = os.getcwd()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+DB_directory.replace("\\", "/")+'/sqlite/data.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'julius'
db = SQLAlchemy(app)

conn = sqlite3.connect(DB_directory.replace("\\", "/")+'/sqlite/data.sqlite')
c = conn.cursor()
c.execute("PRAGMA foreign_keys=ON;")
# c.execute("insert into entry(client_id,account_id,cash,entry_date,doc_date) values(1,1,143,'2007-01-01 10:00:00','2010-05-11 11:00:00')")
conn.commit()
c.close()
conn.close()


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
    # accounts = Account.query.order_by(Account.account_name).all()
    account_form = get_account_forms()

    try:
        form_id = account_form[0].account_id.data-1
    except TypeError:
        form_id = -1

    if account_form[form_id].validate_on_submit():
        print('form validated JUL!!!!', form_id)
        flash('Success: Valid Entry')
        return redirect(url_for('cash_receipt_b'))
    elif form_id != (-1):
        flash('Invalid Input')
        return

    return render_template('cash_receipt_b.html', account_form=account_form)


def get_account_forms():
    return [
        AccountReceivableForm(),
        LoansReceivableForm(),
        CashAdvanceForm(),
        AccruedExpensesForm(),
        AccountsPayableForm(),
        LoansPayableForm(),
        SssHdmfPhicPremiumPayableForm(),
        CapitalForm(),
        NetIncomeForm(),
        SalesForm(),
        InterestEarnedForm()

        # ServiceForm(),
        # PenaltyForm(),
        # OtherIncomeForm(),
        # PurchasesForm(),
        # SalariesAndWagesForm(),
        # LightAndPowerForm(),
        # OfficeSuppliesForm(),
        # StoreSuppliesForm(),
        # RentalForm(),
        # CommunicationForm(),
        # SssContributionForm(),
        # HdmfContributionForm(),
        # PhicContributionForm(),
        # TransportationForm(),
        # AllowancesForm(),
        # RepairAndMaintenanceForm(),
        # TaxesAndLicencesForm(),
        # SecurityServicesForm(),
        # MiscellaneousForm(),
        # ProfessionalFeeForm(),
        # DepreciationFeeForm(),
        # AllowanceForDepreciationForm(),
        # BadDebtsForm(),
        # AllowanceForBadDebtsForm(),
        # AmortizationForm(),
        # InsuranceForm(),
        # FuelAndOilForm()
    ]


if __name__ == '__main__':
    app.run(debug=True)
