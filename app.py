from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    BooleanField,
    DateTimeField,
    RadioField,
    SelectField,
    TextField,
    SubmitField,
)
from wtforms.fields.simple import TextAreaField

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config["SECRET_KEY"] = "mysecretkey"


class InfoForm(FlaskForm):
    breed = StringField("What breed are you?")
    submit = SubmitField("Submit")
    breed = StringField("What breed are you?", validators=[DataRequired()])
    has_nametag = BooleanField("Does this dog have a nametag?")
    mood = RadioField(
        "Please choose your mood:",
        choices=[("mood_one", "Happy"), ("mood_two", "Excited")],
    )
    food_choice = SelectField(
        u"Pick your favorite food:",
        choices=[("chi", "Chicken"), ("bf", "beef"), ("fish", "Fish")],
    )
    feedback = TextAreaField()
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session["breed"] = form.breed.data
        session["has_nametag"] = form.has_nametag.data
        session["mood"] = form.mood.data
        session["food"] = form.food_choice.data
        session["feedback"] = form.feedback.data

        return redirect(url_for("thankyou"))

    return render_template("index.html", form=form)


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")


if __name__ == "__main__":
    app.run(debug=True)
