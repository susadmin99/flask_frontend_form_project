import sys
import os

#This line adds the parent directory to Python's path(without this it can't find the forms and RegisterForm)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from forms import RegisterForm  

def build_form_data():
    """Default valid form values."""
    data = {
        "signup[custom_values][ca_can_attend]": True,
        "signup[custom_values][ca_eligible]": True,

        "signup[first_name]": "John",
        "signup[last_name]": "Doe",
        "signup[email]": "john@example.com",
        "signup[mobile_number]": "12345678",
        "signup[home_address_attributes][address1]": "123 Test Street",
        "signup[home_address_attributes][address2]": "",
        "signup[home_address_attributes][city]": "TestCity",
        "signup[home_address_attributes][zip]": "12345",

        "signup[custom_values][gender]": "1",
        "signup[custom_values][dob_day]": "10",
        "signup[custom_values][dob_month]": "3",
        "signup[custom_values][dob_year]": "1990",
        "signup[custom_values][ethnicity]": "3",
        "signup[custom_values][disability]": "3",
        "signup[custom_values][multiple_choice_one]": "1",
        "signup[custom_values][scotland_educational_qualification]": "3",

        "signup[custom_values][consent]": True,
        "signup[custom_values][stay_on_db]": False,
    }
    return data


def test_form_valid_with_correct_data(app):
    #Tests the normal working way where all required fields are filled correctly.
    #This ensures the form works as expected when users submit valid values.
    with app.test_request_context(method="POST", data=build_form_data()):
        form = RegisterForm()

        assert form.validate() is True, form.errors


def test_form_invalid_missing_required_fields(app):
    #Checks that the form correctly rejects form submissions when required fields are missing. The server-side validation is working if this is okay.
    data = build_form_data()
    del data["signup[first_name]"]

    form = RegisterForm(data=data)
    assert form.validate() is False


def test_invalid_year_format(app):
    #Verifies that the form catches invalid year formats (e.g. letters or impossible dates). Helps to prevent bad date input from going through.
    data = build_form_data()
    data["signup[custom_values][dob_year]"] = "abcd"

    form = RegisterForm(data=data)
    assert form.validate() is False


def test_invalid_day_value(app):
    #Ensures the form refuses invalid day numbers (like 0 or >31).
    data = build_form_data()
    data["signup[custom_values][dob_day]"] = "40"

    form = RegisterForm(data=data)
    assert form.validate() is False


def test_invalid_ethnicity_option(app):
    #Provides an ethnicity value outside the allowed choices.
    #Important to prevent clients from tampering with POST data.
    data = build_form_data()
    data["signup[custom_values][ethnicity]"] = "999"

    form = RegisterForm(data=data)
    assert form.validate() is False


def test_invalid_disability_option(app):
    #Tests a disability option that does not exist.
    #Protects against invalid select inputs and maintains data integrity.
    data = build_form_data()
    data["signup[custom_values][disability]"] = "-1"

    form = RegisterForm(data=data)
    assert form.validate() is False


def test_invalid_satisfaction_level(app):
    #Provides an invalid value for the satisfaction level select.
    #Ensures only valid specific options are accepted.
    data = build_form_data()
    data["signup[custom_values][multiple_choice_one]"] = "999"

    form = RegisterForm(data=data)
    assert form.validate() is False


def test_invalid_education_option(app):
    #Uses an invalid dropdown option for education level.
    #This test ensures backend validation matches frontend choices.
    data = build_form_data()
    data["signup[custom_values][scotland_educational_qualification]"] = "999"

    form = RegisterForm(data=data)
    assert form.validate() is False