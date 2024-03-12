from flask import Flask
app = Flask(__name__) # initialiseer de Flask-app

# Routing:
@app.route("/") # dit heet een decorator: "Put simply: decorators wrap a function, modifying its behavior." De route-functie van Flask wrapt nu dus onze index-functie.
def index():
    return "<p>Deze pagina wordt gerenderd door Flask!</p><p><a href='/info'>Lees meer</a></p>"

@app.route("/info") # tweede pagina
@app.route("/information") # je kunt ook twee (of meer) url's op één route hebben
def info():
    return "<p>Deze ook.</p><p><a href='/'>Terug</a></p>"

@app.route("/gebruikers/<naam>") # dit is een dynamische route
def cursist(naam):
    return f"<p>Dit is de gebruikerspagina van <span style='font-weight: bold;'>{naam}</span><p>"

@app.route("/codes/<int:id>") # dynamische route met afgedwongen type (string, float, int)
def code(id):
    return f"Pagina met informatie over product met code {id}"

# App starten (maar niet als deze file ergens geincluded wordt):
if __name__ == "__main__":
    app.run(debug=True, port=5000)