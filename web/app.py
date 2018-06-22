from flask import Flask, render_template
app = Flask(__name__)


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
