#setup flask app
from flask import Flask


def create_app():
    created_app = Flask(__name__)
    created_app.config['SECRET_KEY'] = 'Secret'

    return created_app