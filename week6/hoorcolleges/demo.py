from flask import Flask, render_template, flash, get_flashed_messages, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, SelectField
from wtforms.validators import DataRequired

# ORM
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# Dit is de moderne manier om met Base te werken:
Base = declarative_base()

dbpath = "sqlite:///demo.sqlite" # in huidige map, alternatieve syntax:
#import os
#basedir = os.path.abspath(os.path.dirname(__file__)) # volledige pad naar huidige map, eventueel aan te passen
#dbpath = 'sqlite:///' + os.path.join(basedir, 'demo.sqlite')
engine = create_engine(dbpath)

class Persoon(Base):
    __tablename__ = 'personen'
    id = Column(Integer, primary_key=True)
    voornaam = Column(String, nullable=False)
    achternaam = Column(String, nullable=False)
    posts = relationship("BlogPost", back_populates="auteur")

class BlogPost(Base):
    __tablename__ = 'blogposts'
    id = Column(Integer, primary_key=True)
    titel = Column(String, nullable=False)
    persoon_id = Column(Integer, ForeignKey("personen.id"))
    auteur = relationship("Persoon", back_populates="posts")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sessionobj = Session()
# einde ORM

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eensupergeheimetekenreeks12345'

# FORMS
class DemoForm(FlaskForm):
    id = HiddenField()
    voornaam = StringField("Wat is je voornaam?", validators=[DataRequired()])
    achternaam = StringField("Wat is je achternaam?", validators=[DataRequired()])
    submit = SubmitField("Verzend")

class BlogForm(FlaskForm):
    titel = StringField("Wat is de titel van je blogpost?", validators=[DataRequired()])
    # selectbox heeft 'choices' nodig: een lijst van tupels (id, naam)
    auteurs = []
    personen = sessionobj.query(Persoon).all()
    for pers in personen:
        auteurs.append((pers.id, pers.voornaam + " " + pers.achternaam))
    auteur = SelectField("Wie is de auteur?", choices=auteurs)
    submit = SubmitField("Verzend")
# einde Forms

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

@app.route('/delete/<id>')
def delete(id):
    pers = sessionobj.query(Persoon).filter(Persoon.id == id).first()
    if pers is not None:
        sessionobj.delete(pers)
        sessionobj.commit()
        flash("Persoon succesvol verwijderd")
    return redirect("/")

@app.route('/edit/<id>')
def edit(id):
    pers = sessionobj.query(Persoon).filter(Persoon.id == id).first()
    form = DemoForm()
    form.id.data = id # wordt automatisch gerenderd
    form.voornaam.data = pers.voornaam
    form.achternaam.data = pers.achternaam
    return render_template("edit.html", form=form)

@app.route('/edit', methods=["POST"])
def update():
    form = DemoForm()
    if form.validate_on_submit():
        id = form.id.data
        voornaam = form.voornaam.data
        achternaam = form.achternaam.data
        pers = sessionobj.query(Persoon).filter(Persoon.id == id).first()
        if pers is not None:
            pers.voornaam = voornaam
            pers.achternaam = achternaam
            sessionobj.add(pers)
            sessionobj.commit()
            flash("Gegevens succesvol aangepast")
    return redirect("/")

@app.route('/newblog', methods=["GET", "POST"])
def newblog():
    form = BlogForm()
    if form.validate_on_submit():
        titel = form.titel.data
        persoon_id = form.auteur.data
        newpost = BlogPost(titel=titel, persoon_id=persoon_id)
        sessionobj.add(newpost)
        sessionobj.commit()
    # Lijst met alle posts:
    posts = sessionobj.query(BlogPost).order_by(BlogPost.titel).all()
    # Lijst met alle auteurs:
    auteurs = sessionobj.query(Persoon).filter(Persoon.posts != None).all()
    return render_template("blog.html", form=form, posts=posts, auteurs=auteurs)

if __name__ == "__main__":
    app.run(debug=True)