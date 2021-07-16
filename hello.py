from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"

# export FLASK_APP=hello
# flask run