from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import *
from sqlalchemy.exc import IntegrityError
from sqlalchemy.engine import Engine
from sqlalchemy import event

import os
import sqlite3
import datetime

from models import *


app = Flask(__name__)
DB_directory = os.getcwd()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+DB_directory.replace("\\", "/")+'/sqlite/data.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'julius'
db = SQLAlchemy(app)


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if type(dbapi_connection) is sqlite3.Connection:  # play well with other DB backends
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()


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


@app.route('/cash.receipt.book/<client_id_>', methods=['GET', 'POST'])
def cash_receipt_b(client_id_):
    client = Client.query.filter_by(id=client_id_).first()
    account_form = get_account_forms()

    try:
        form_id = account_form[0].account_id.data-1
    except TypeError:
        form_id = -1

    if account_form[form_id].validate_on_submit():
        entry = Entry(client_id=client_id_,
                      account_id=account_form[form_id].account_id.data,
                      cash=account_form[form_id].cash.data,
                      entry_date=datetime.datetime.now(),
                      doc_date=datetime.datetime.strptime(
                          datetime.datetime.strftime(account_form[form_id].date.data, '%m-%d-%Y'), '%m-%d-%Y').date()
                      )
        try:
            db.session.add(entry)
            db.session.commit()
        except IntegrityError:
            flash("ERROR! data not committed to database")
            db.session.rollback()
            return redirect(url_for('cash_receipt_b', client_id_=client_id_))

        print('form validated JUL!!!! form_id: ', form_id)
        flash('SUCCESS: Entry submitted')

        return redirect(url_for('cash_receipt_b', client_id_=client_id_))
    elif form_id != (-1):
        print("invalid input")
        flash('FAILED: Invalid input')
        return redirect(url_for('cash_receipt_b', client_id_=client_id_))

    return render_template('cash_receipt_b.html',
                           account_form=account_form,
                           client_name=[client.first_name,
                                        client.middle_name,
                                        client.last_name],
                           client_id=client_id_)


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
