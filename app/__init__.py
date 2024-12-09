from flask import Flask

app = Flask(__name__)
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    return app
