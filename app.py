from flask import Flask, render_template, request
from flask_assets import Environment, Bundle
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length
from forms import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '0123456789'
app.config['WTF_CSRF_ENABLED'] = False 

@app.route('/', methods=['GET', 'POST'])
def home():
    form = RegisterForm()

    if request.method == "POST":
        print("----POST REQUEST RECEIVED----")
        print(f"Form data: {request.form}")

        if form.validate_on_submit():
            print("----FORM VALIDATED SUCCESSFULLY----")

            with open("output.txt", "w", encoding="utf-8") as file:
                file.write(f"Can attend all dates: {form.can_attend_all_dates.data}\n")
                file.write(f"Eligible to attend: {form.eligible_to_attend.data}\n")

                file.write(f"First Name: {form.first_name.data}\n")
                file.write(f"Last Name: {form.last_name.data}\n")
                file.write(f"Email: {form.email.data}\n")
                file.write(f"Phone: {form.phone.data}\n")
                file.write(f"Address 1: {form.address1.data}\n")
                file.write(f"Address 2: {form.address2.data}\n")
                file.write(f"City: {form.city.data}\n")
                file.write(f"Post code: {form.post_code.data}\n")

                file.write(f"Gender: {form.gender.data}\n")
                file.write("Birthday \n")
                file.write(f"Day: {form.birth_day.data}\n")
                file.write(f"Month: {form.birth_month.data}\n")
                file.write(f"Year: {form.birth_year.data}\n")
                file.write(f"Ethnicity: {form.ethnicity.data}\n")
                file.write(f"Disability: {form.disability.data}\n")
                file.write(f"Satisfaction Level: {form.satisfaction_level.data}\n")
                file.write(f"Educational Qualification: {form.educational_qualification.data}\n")

                file.write(f"Privacy Policy: {form.privacy_policy.data}\n")
                file.write(f"News Subscription: {form.news_subscription.data}\n")

            return "Thank you for your registration. <br> Data saved! <a href='/'>Go back</a>"
        elif form.is_submitted() and not form.validate():
            print("----FORM VALIDATION FAILED----")
            print(f"Form errors: {form.errors}")

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
