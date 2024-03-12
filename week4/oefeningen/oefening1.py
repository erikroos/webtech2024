from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welkom bij muziekschool Session</h1>'

@app.route('/informatie')
def info():
    return '<h1>Dit hebben we jou te bieden:</h1>'

@app.route('/cursist/<naam>')
def cursist(naam):
    output = f'<h1>Dit is de pagina van {naam}<h1>'
    return output

# Optie 1: via URL (/artiest/henk)
@app.route('/artiest/<naam>')
def naam2artiest(naam):
    eindletter = naam[-1]
    if eindletter == 's':
        artiestnaam = naam + 'sy'
    else:
        artiestnaam = naam + 'tezy'
    return f"Welkom {naam}! Je coole artiestennaam issss... {artiestnaam.upper()}"

# Optie 2: via URL-parameter (/artistifier?naam=henk)
@app.route('/artistifier')
def naam2artiest2():
    naam = request.args.get('naam')
    if naam is not None:
        eindletter = naam[-1]
        if eindletter == 's':
            artiestnaam = naam + 'sy'
        else:
            artiestnaam = naam + 'tezy'
        return f"Welkom {naam}! Je coole artiestennaam issss... {artiestnaam.upper()}"
    return "Geef een naam op via de naam-parameter"

if __name__ == '__main__':
    app.run(debug=True)
