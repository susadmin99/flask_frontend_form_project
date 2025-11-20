import sys
import os

#This line adds the parent directory to Python's path(without this it can't find the forms and RegisterForm)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

#Here testing a basic route that it rsponses OK so the website is reachable
def test_base_route():
    response = app.test_client().get('/')
    assert response.status_code == 200

test_base_route()

