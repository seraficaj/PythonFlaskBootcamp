from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
)

app = Flask(__name__)

app.config["SECRET_KEY"] = "mysecretkey"


class SimpleForm(FlaskForm):
    breed = StringField('Puppy Breed')
    submit = SubmitField('Click me')


@app.route('/', methods=['GET', 'POST'])
def index():
    # Create instance of the form.
    form = SimpleForm()
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        flash('You just clicked the button!')
        return redirect(url_for("index"))

    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
