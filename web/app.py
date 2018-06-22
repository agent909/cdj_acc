from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/dashboard')
def home():
    return render_template('index.html')


@app.route('/registration')
def add_user():
    return render_template('register.html')


@app.route('/test')
def test():
    return render_template('test.html')



if __name__ == '__main__':
    app.run(debug=True)
