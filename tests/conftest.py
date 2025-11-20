import os
import sys
import pytest
from flask import Flask

#This line adds the parent directory to Python's path(without this it can't find the forms and RegisterForm)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'test'
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['TESTING'] = True

    with app.app_context():
        yield app
