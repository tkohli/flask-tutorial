from flask import url_for
from logging import debug
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


# @app.route("/")
# def hello():
#     return "<h1>Index page</h1>"


# @app.route("/hello")
# def helloworld():
#     return "<h1>Hello World!!!</h1>"


# @app.route("/<name>")
# def names(name):
#     return f'hello, {escape(name)}!!'


if __name__ == "__main__":
    app.run(debug=True)
