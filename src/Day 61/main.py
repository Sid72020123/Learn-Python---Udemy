from flask import Flask, render_template
from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError

from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = "this is a secret ;)"
bootstrap = Bootstrap5(app)

DUMMY_EMAIL = "admin@email.com"
DUMMY_PASSWORD = "12345678"


def password_length_check(form, field):
    if len(field.data) < 8:
        raise ValidationError("Password must at least be of 8 characters length!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password", validators=[DataRequired(), password_length_check]
    )
    submit = SubmitField("Log In")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        if email == DUMMY_EMAIL and password == DUMMY_PASSWORD:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
