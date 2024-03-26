from flask import Flask, render_template, flash, get_flashed_messages
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eensupergeheimetekenreeks12345'

class DemoForm(FlaskForm):
    voornaam = StringField("Wat is je voornaam?", validators=[DataRequired()])
    achternaam = StringField("Wat is je achternaam?", validators=[DataRequired()])
    submit = SubmitField("Verzend")

@app.route("/", methods=["GET", "POST"])
def index():
    # Database connecten en (tabel) aanmaken indien nodig
    db = sqlite3.connect("demo.sqlite")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS personen (voornaam TEXT, achternaam TEXT)')

    form = DemoForm()
    if form.validate_on_submit():
        flash("Formulier succesvol ontvangen")
        voornaam = form.voornaam.data
        achternaam = form.achternaam.data
        flash(f"Bedankt voor het aanmelden, {voornaam} {achternaam}!")
        cursor.execute('INSERT INTO personen (voornaam, achternaam) VALUES (?,?)', (voornaam, achternaam))
        db.commit()
        flash('Succesvol toegevoegd aan de database')

    rows = cursor.execute('SELECT * FROM personen').fetchall()

    cursor.close()
    db.close()

    return render_template("demo.html", form=form, rows=rows)

if __name__ == "__main__":
    app.run(debug=True)