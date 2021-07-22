from flask import Flask, request, render_template
from markupsafe import escape
from flask import url_for

app = Flask(__name__)


# Routing
@app.route('/')
def index():
    return f"homepage"


# @app.route('/hello')
# def hello_world():
#     return f"hello world"


# Variable Rules
# @app.route('/user/<username>')
# def show_user_profile(username):
#     return f"User {escape(username)}"


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post {post_id}"


@app.route('/path/<path:subpath>')
def show_path(subpath):
    return f"Subpath {escape(subpath)}"


# Unique URLs / Redirection Behavior
@app.route('/projects/')
def projects():
    return "The project page"


@app.route('/about')
def about():
    return"The about page"


# URL Building
# @app.route('/login')
# def login():
#     return "Login"


@app.route('/user/<username>')
def profile(username):
    return f"{username}'s profile"


with app.test_request_context():
    print(url_for('index'))
    # print(url_for('login'))
    # print(url_for('login', next='/'))
    print(url_for('profile', username='Sahil Chaudhary'))


# HTTP Methods

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "do_the_login"
    else:
        return "show_the_login_form"


# Static Files
# url_for('static', filename='static/style.css')


# Rendering Templates
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


"""
export FLASK_APP=hello
flask run
"""