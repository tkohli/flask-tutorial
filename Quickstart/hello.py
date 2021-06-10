from flask import session
from flask import url_for
from logging import debug
from flask import Flask, render_template, request, abort, redirect
from markupsafe import escape

app = Flask(__name__)


# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         abort(401)
#         return login_form()


# @app.errorhandler(404)
# def page_not_found(error):
#     return "<h1>No such page</h1>"

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))


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
