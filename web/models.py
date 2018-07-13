from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    business_name = db.Column(db.String(150), nullable=False)
    cellular = db.Column(db.String(15), nullable=True)
    telephone = db.Column(db.String(20), nullable=True)
    entries = db.relationship('Entry', backref='client', lazy=True)

    def __repr__(self):
        return '<Client %r>' % self.first_name
#insert into client(first_name,middle_name,last_name,business_name,cellular) values ('juan','dela','cruz','business1','09184412707');


class Entry(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    cash = db.Column(db.Numeric, default=0)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Entry %r>' % self.tranaction_id
#insert into entry(client_id,account_id,cash,date) values(1,1,143,'2007-01-01');
#date time format '2007-01-01 10:00:00' y-m-d t


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry = db.relationship('Entry', backref='account', lazy=True)
    account_name = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return '<Account %r>' % self.account_name
#insert into account(account_name) values('Cash');
#insert into account(account_name) values('Account Payable');


class CashAdvance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, nullable=False)
    transaction_id = db.Column(db.Integer, nullable=False)
    employee = db.Column(db.String(200), nullable=True)
    debit = db.Column(db.Numeric, default=0)
    credit = db.Column(db.Numeric, default=0)

    def __repr__(self):
        return '<cash>'


class AccountPayable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, nullable=False)
    transaction_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    or_number = db.Column(db.Integer, nullable=True)
    check_voucher_no = db.Column(db.Integer, nullable=True)
    pay_to = db.Column(db.String(200), nullable=True)
    particulars = db.Column(db.String(200), nullable=True)
    debit = db.Column(db.Numeric, default=0)
    credit = db.Column(db.Numeric, default=0)

    def __repr__(self):
        return '<payable>'


class AccountReceivable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, nullable=False)
    transaction_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    schedule = db.Column(db.DateTime, nullable=False)
    or_number = db.Column(db.Integer, nullable=True)
    sold_to = db.Column(db.String(200), nullable=True)
    particulars = db.Column(db.String(200), nullable=True)
    debit = db.Column(db.Numeric, default=0)
    credit = db.Column(db.Numeric, default=0)

    def __repr__(self):
        return '<receivable>'


class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, nullable=False)
    transaction_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    or_number = db.Column(db.Integer, nullable=True)
    sold_to = db.Column(db.String(200), nullable=True)
    particulars = db.Column(db.String(200), nullable=True)
    debit = db.Column(db.Numeric, default=0)
    credit = db.Column(db.Numeric, default=0)

    def __repr__(self):
        return '<sales>'


class Capital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, nullable=False)
    transaction_id = db.Column(db.Integer, nullable=False)
    investor = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    debit = db.Column(db.Numeric, default=0)
    credit = db.Column(db.Numeric, default=0)


class SalariesAndWages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, nullable=False)
    transaction_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    debit = db.Column(db.Numeric, default=0)
    credit = db.Column(db.Numeric, default=0)


db.create_all()
