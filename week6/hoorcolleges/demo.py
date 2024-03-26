from flask import Flask, render_template, flash, get_flashed_messages, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# ORM
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

base = declarative_base()
dbpath = "sqlite:///demo.sqlite" # in huidige map, alternatieve syntax:
#import os
#basedir = os.path.abspath(os.path.dirname(__file__)) # volledige pad naar huidige map, eventueel aan te passen
#dbpath = 'sqlite:///' + os.path.join(basedir, 'demo.sqlite')
engine = create_engine(dbpath)

class Persoon(base):
    __tablename__ = 'personen'
    id = Column(Integer, primary_key=True)
    voornaam = Column(String, nullable=False)
    achternaam = Column(String, nullable=False)

base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sessionobj = Session()
# einde ORM

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eensupergeheimetekenreeks12345'

class DemoForm(FlaskForm):
    voornaam = StringField("Wat is je voornaam?", validators=[DataRequired()])
    achternaam = StringField("Wat is je achternaam?", validators=[DataRequired()])
    submit = SubmitField("Verzend")

@app.route("/", methods=["GET", "POST"])
def index():
    form = DemoForm()
    if form.validate_on_submit():
        flash("Formulier succesvol ontvangen")
        voornaam = form.voornaam.data
        achternaam = form.achternaam.data
        flash(f"Bedankt voor het aanmelden, {voornaam} {achternaam}!")
        pers = Persoon(voornaam=voornaam, achternaam=achternaam)
        sessionobj.add(pers)
        sessionobj.commit()
        flash('Succesvol toegevoegd aan de database')
        return redirect(url_for('index'))

    rows = sessionobj.query(Persoon).order_by(Persoon.voornaam)
    return render_template("demo.html", form=form, rows=rows)

if __name__ == "__main__":
    app.run(debug=True)