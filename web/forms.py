from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField, DecimalField
from wtforms.validators import DataRequired


class AccountReceivableForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    date = DateField('Date', format='%m-%d-%Y', validators=[DataRequired()])
    or_number = IntegerField('Document no', validators=[DataRequired()])
    debtor = StringField(validators=[DataRequired()])
    quantity = IntegerField()
    item = StringField()
    cash = DecimalField('cash', validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'account_receivable'


class LoansReceivableForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'loans_receivable'


class CashAdvanceForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'cash_advance'


class AccruedExpensesForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'accrued_expenses'


class AccountsPayableForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'accounts_payable'


class LoansPayableForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'loans_payable'


class SssHdmfPhicPremiumPayableForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'sss_hdmf_phic_premium_payable'


class CapitalForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'capital'


class NetIncomeForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'net_income'


class SalesForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'sales'


class InterestEarnedForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'interest_earned'


class ServiceForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'service_fee'


class PenaltyForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'penalty'


class OtherIncomeForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'other_income'


class PurchasesForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'purchases'


class SalariesAndWagesForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'salaries_and_wages'


class LightAndPowerForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'light_and_power'


class OfficeSuppliesForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'office_supplies'


class StoreSuppliesForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'store_supplies'


class RentalForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'rental'


class CommunicationForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'communication'


class SssContributionForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'sss_contribution'


class HdmfContributionForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'hdmf_contribution'


class PhicContributionForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'phic_contribution'


class TransportationForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'transportation'


class AllowancesForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'allowances'


class RepairAndMaintenanceForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'repair_and_maintenance'


class TaxesAndLicencesForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'taxes_and_licences'


class SecurityServicesForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'security_services'


class MiscellaneousForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'miscellaneous'


class ProfessionalFeeForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'professional_fee'


class DepreciationFeeForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'depreciation_fee'


class AllowanceForDepreciationForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'allowance_for_depreciation'


class BadDebtsForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'bad_debts'


class AllowanceForBadDebtsForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'allowance_for_bad_debts'


class AmortizationForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'amortization'


class InsuranceForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'insurance'


class FuelAndOilForm(FlaskForm):
    client_id = IntegerField(validators=[DataRequired()])
    account_id = IntegerField(validators=[DataRequired()])
    submit = SubmitField('ADD')

    def __repr__(self):
        return 'fuel_and_oil'
