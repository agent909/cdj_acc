from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField, DecimalField
from wtforms.validators import DataRequired


class AccountReceivableForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    # account id is used to know what validator to be used
    account_id = IntegerField(validators=[DataRequired()])
    date = DateField('Date', format='%m-%d-%Y', validators=[DataRequired()])
    schedule = DateField('Schedule', format='%m-%d-%Y', validators=[DataRequired()])
    or_number = IntegerField('Document no', validators=[DataRequired()])
    sold_to = StringField(validators=[DataRequired()])
    particulars = StringField(validators=[DataRequired()])
    cash = DecimalField('cash', validators=[DataRequired()])
    submit = SubmitField('ADD')


class TestForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    name = StringField(validators=[DataRequired()])
    submit = SubmitField('ADD')


class AccountPayableForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    date = DateField(format='%m/%d/%Y')
    schedule = DateField(format='%m/%d/%Y')
    or_number = IntegerField(validators=[DataRequired()])
    sold_to = StringField(validators=[DataRequired()])
    particulars = StringField(validators=[DataRequired()])
    cash = DecimalField(validators=[DataRequired()])
    submit = SubmitField('Add')


class SalesForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    date = DateField(format='%m/%d/%Y')
    or_number = IntegerField(validators=[DataRequired()])
    sold_to = StringField(validators=[DataRequired()])
    particulars = StringField(validators=[DataRequired()])
    cash = DecimalField(validators=[DataRequired()])
    submit = SubmitField('Add')


class CapitalForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    investor = StringField(validators=[DataRequired()])
    date = DateField(format='%m/%d/%Y')
    cash = DecimalField(validators=[DataRequired()])
    submit = SubmitField('Add')


class SalaryWagesForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    cash = DecimalField(validators=[DataRequired()])
