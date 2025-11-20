import sys
import os

#This line adds the parent directory to Python's path(without this it can't find the forms and RegisterForm)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from forms import RegisterForm

def test_ethnicity_html_attributes(app):
    #Checks that the ethnicity field renders with the correct HTML id and name.
    #This is important because the frontend and backend rely on these attributes for form binding, styling and data processing.
    form = RegisterForm()
    html = str(form.ethnicity)

    assert 'id="signup_custom_values_ethnicity_custom"' in html
    assert 'name="signup[custom_values][ethnicity]"' in html


def test_disability_html_attributes(app):
    #Ensures the disability field outputs the expected HTML attributes.
    form = RegisterForm()
    html = str(form.disability)

    assert 'id="signup_custom_values_disability_custom"' in html
    assert 'name="signup[custom_values][disability]"' in html


def test_satisfaction_level_html_attributes(app):
    #Confirms that the satisfaction level field is rendered with the correct id and name. This protects against mismatches between frontend form fields and the backend WTForms field definitions.
    form = RegisterForm()
    html = str(form.satisfaction_level)

    assert 'id="signup_custom_values_multiple_choice_one_custom"' in html
    assert 'name="signup[custom_values][multiple_choice_one]"' in html