from flask_wtf import FlaskForm
from wtforms import SelectField, validators, BooleanField, StringField, SubmitField
from wtforms.validators import Email, InputRequired, Length, DataRequired

class RegisterForm(FlaskForm):
    cant_validate = ""

    #Confirm eligibility and ability to attend
    can_attend_all_dates = BooleanField(
        label="I can attend all dates.",
        name="signup[custom_values][ca_can_attend]",
        validators=[validators.DataRequired(message="If you can attend all is required")]
    )
    eligible_to_attend = BooleanField(
        label="I am eligible to attend.",
        name="signup[custom_values][ca_eligible]",
        validators=[validators.DataRequired(message="If you're eligible to attend is required")]
    )

    #Name, contact details and address
    first_name = StringField(
        label="First Name",
        name="signup[first_name]",
        validators=[validators.InputRequired(message="First name is required")],
        render_kw={
            "placeholder": "First Name",
            "aria-describedby": "first_name_error",
            "autocomplete": "given-name"
        }
    )
    last_name = StringField(
        label="Last Name",
        name="signup[last_name]",
        validators=[validators.InputRequired(message="Last name is required")],
        render_kw={
            "placeholder": "Last Name",
            "aria-describedby": "last_name_error",
            "autocomplete": "family-name"
        }
    )

    email = StringField(
        label="E-mail",
        name="signup[email]",
        validators=[validators.InputRequired(message="E-mail is required")],
        render_kw={
            "placeholder": "example@mail.com",
            "type": "email",
            "aria-describedby": "email_error",
            "autocomplete": "email"
        }
    )
    phone = StringField(
        label="Phone (mobile or home)",
        name="signup[mobile_number]",
        validators=[validators.InputRequired(message="Phone is required")],
        render_kw={
            "placeholder": "",
            "type": "tel",
            "aria-describedby": "phone_error",
            "autocomplete": "phone"
        }
    )
    address1 = StringField(
        label="Address Line 1",
        name="signup[home_address_attributes][address1]",
        validators=[validators.InputRequired(message="Address is required")],
        render_kw={
            "placeholder": "",
            "type": "text",
            "aria-describedby": "address_error",
            "autocomplete": "address"
        }
    )
    address2 = StringField(
        label="Address Line 2",
        name="signup[home_address_attributes][address2]",
        render_kw={
            "placeholder": "",
            "type": "text"
        }
    )
    city = StringField(
        label="City",
        name="signup[home_address_attributes][city]",
        validators=[validators.InputRequired(message="City is required")],
        render_kw={
            "placeholder": "City",
            "type": "text",
            "aria-describedby": "city_error",
            "autocomplete": "city"
        }
    )
    post_code = StringField(
        label="Post Code",
        name="signup[home_address_attributes][zip]",
        validators=[validators.InputRequired(message="Post Code is required")],
        render_kw={
            "placeholder": "Post code",
            "type": "text",
            "aria-describedby": "post_code_error",
            "autocomplete": "postal code"
        }
    )

    #About you
    gender = SelectField(
        label="What gender do you identify as?",
        name="signup[custom_values][gender]",
        choices=[
            ('', 'Please select...'),
            ('2', 'Female'),
            ('1', 'Male'),
            ('3', 'Non-binary or Other')
        ],
        validators=[validators.DataRequired(message="Please identify your gender")],
        render_kw={
            "id": "signup_custom_values_gender_custom",
            "aria-describedby": "gender_error"
        }
    )
    birth_day = SelectField(
        label = "Day",
        name = "signup[custom_values][dob_day]",
        choices=[
            ('', 'Please select...')] + [(str(i), str(i)) for i in range(1, 32)],
        validators=[DataRequired(message="Please select the day of birth")],
        render_kw={
            "class": "user-success",
            "id": "signup_custom_values_dob_day_custom",
            "aria-describedby": "birth_day_error"
            } 
    )
    birth_month = SelectField(
        label = "Month",
        name = "signup[custom_values][dob_month]",
        choices=[
            ('', 'Please select...'),
            ('1', 'January'),
            ('2', 'February'),
            ('3', 'March'),
            ('4', 'April'),
            ('5', 'May'),
            ('6', 'June'),
            ('7', 'July'),
            ('8', 'August'),
            ('9', 'September'),
            ('10', 'October'),
            ('11', 'November'),
            ('12', 'December')
        ],
        validators=[DataRequired(message="Please select the month of birth")],
        render_kw={
            "id": "signup_custom_values_dob_month_custom",
            "aria-describedby": "birth_month_error"
        }
    )
    birth_year = StringField(
        label = "Year",
        name = "signup[custom_values][dob_year]",
        validators=[
            DataRequired(message="Year of birth is required"),
        ],
        render_kw={
            "class": "text form-control",
            "placeholder": "YYYY",
            "id": "signup_custom_values_dob_year_custom",
            "aria-describedby": "birth_year_error"
        }
    )
    ethnicity = SelectField(
        label = "What is your ethnic group?",
        name = "signup[custom_values][ethnicity]",
        choices=[
            ('', 'Please select...'),
            ('3', 'Asian or Asian British'),
            ('4', 'Black, African, Caribbean or Black British'),
            ('2', 'Mixed or Multiple ethnic groups'),
            ('1', 'White English, Welsh, Scottish, Northern Irish or British'),
            ('7', 'White Irish'),
            ('6', 'White other'),
            ('5', 'Other ethnic group')
        ],
        validators=[DataRequired(message="Please select ethnicity")],
        render_kw={
            "id": "signup_custom_values_ethnicity_custom",
            "aria-describedby": "ethnicity_error"
        }
    )
    disability = SelectField(
        label = "Do you have any physical or mental health conditions or illnesses lasting or expected to last 12 months or more which limit your ability to carry out day-to-day activities?",
        name = "signup[custom_values][disability]",
        choices=[
            ('', 'Please select...'),
            ('2', 'Yes, limited a little'),
            ('1', 'Yes, limited a lot'),
            ('3', 'No')
        ],
        validators=[DataRequired(message="Please choose if you have disability")],
        render_kw={
            "id": "signup_custom_values_disability_custom",
            "aria-describedby": "disability_error"
        }
    )
    satisfaction_level = SelectField(
        label = "All in all, how satisfied or dissatisfied would you say you are with the way in which the National Health Service runs nowadays?",
        name = "signup[custom_values][multiple_choice_one]",
        choices=[
            ('', 'Please select...'),
            ('1', 'Very satisfied'),
            ('2', 'Quite satisfied'),
            ('3', 'Neither satisfied nor dissatisfied'),
            ('4', 'Quite dissatisfied'),
            ('5', 'Very dissatisfied')
        ],
        validators=[DataRequired(message="Please select satisfaction level")],
        render_kw={
            "id": "signup_custom_values_multiple_choice_one_custom",
            "aria-describedby": "satisfaction_level_error"
        }
    )
    educational_qualification = SelectField(
        label = "What is your highest educational qualification (please see below for definitions)?",
        name = "signup[custom_values][scotland_educational_qualification]",
        choices=[
            ('', 'Please select...'),
            ('1', 'No qualifications, or none yet'),
            ('2', 'Level 1'),
            ('3', 'Level 2'),
            ('4', 'Level 3'),
            ('5', 'Level 4 or above'),
            ('6', 'Apprenticeship, or other qualification')
        ],
        validators=[DataRequired(message="Please choose from educational qualifications")],
        render_kw={
            "id": "signup_custom_values_scotland_educational_qualification_custom",
            "aria-describedby": "educational_qualification_error"
        }
    )

    #Consent to Use Data and Submit
    privacy_policy = BooleanField(
        label="I consent to the use of my data as described on thi page, and in more detail in our <a href=''>privacy policy.</a>",
        name="signup[custom_values][consent]",
        validators=[validators.DataRequired(message="It is required to accept privacy policy")]
    )
    news_subscription = BooleanField(
        label="Please also inform me of similar events in the future (do not delete my details after this event).",
        name="signup[custom_values][stay_on_db]",
    )

    register = SubmitField(
        label = "Register"
    )
