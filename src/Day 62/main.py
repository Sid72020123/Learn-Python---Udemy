from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = StringField(
        "Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()]
    )
    opening_time = StringField(
        "Opening Time (e.g., 08:00 AM)", validators=[DataRequired()]
    )
    closing_time = StringField(
        "Closing Time (e.g., 05:30 PM)", validators=[DataRequired()]
    )
    coffee_rating = SelectField(
        "Coffee Rating",
        choices=[
            "☕️",
            "☕️☕️",
            "☕️☕️☕️",
            "☕️☕️☕️☕️",
            "☕️☕️☕️☕️☕️",
        ],
        validators=[DataRequired()],
    )
    wifi_strength_rating = SelectField(
        "WiFi Strength Rating",
        choices=[
            "✘",
            "💪",
            "💪💪",
            "💪💪💪",
            "💪💪💪💪",
            "💪💪💪💪💪",
        ],
        validators=[DataRequired()],
    )
    power_socket_availability = SelectField(
        "Power Socket Availability",
        choices=[
            "✘",
            "🔌",
            "🔌🔌",
            "🔌🔌🔌",
            "🔌🔌🔌🔌",
            "🔌🔌🔌🔌🔌",
        ],
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    print(form.data.values())
    if form.validate_on_submit():
        with open("cafe-data.csv", "a+", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            writer.writerow(list(form.data.values())[:-2])
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
