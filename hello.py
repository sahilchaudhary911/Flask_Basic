from flask import Flask
from markupsafe import escape
from flask import url_for

app = Flask(__name__)


# Routing
@app.route('/')
def index():
    return f"homepage"


@app.route('/hello')
def hello_world():
    return f"hello world"


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
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Sahil Chaudhary'))

"""
export FLASK_APP=hello
flask run
"""