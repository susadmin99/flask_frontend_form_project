import sys
import os

#This line adds the parent directory to Python's path(without this it can't find the forms and RegisterForm)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from forms import RegisterForm

def test_ethnicity_choices(app):
    #Verifies that the ethnicity field contains the expected option values.
    form = RegisterForm()
    actual = [value for value, label in form.ethnicity.choices if value]
    assert actual == ['3', '4', '2', '1', '7', '6', '5']


def test_disability_choices(app):
    #Ensures the disability field has the correct list of selectable values.
    form = RegisterForm()
    actual = [value for value, label in form.disability.choices if value]
    assert actual == ['2', '1', '3']


def test_satisfaction_level_choices(app):
    #Checks that the satisfaction level field includes the expected values. Good for catching mistakes when editing form definitions or updating business logic.
    form = RegisterForm()
    actual = [value for value, label in form.satisfaction_level.choices if value]
    assert actual == ['1', '2', '3', '4', '5']


def test_education_choices(app):
    #Validates that the education dropdown contains all expected qualification levels.
    form = RegisterForm()
    actual = [value for value, label in form.educational_qualification.choices if value]
    assert actual == ['1', '2', '3', '4', '5', '6']