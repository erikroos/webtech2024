from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return "<h1>Welkom op de Home</h1><p><a href='/example'>Naar het eerste voorbeeld</a></p>"

@app.route('/example')
def example():
    return render_template('example.html', cijfer=5, naam="Erik", lijst=[1,2,3,4], dict={'naam': "Piet", 'cijfer': 5.5})

@app.route('/example2')
def example2():
    return render_template('example2.html', cijfer=5, naam="Erik", lijst=[1,2,3,4], dict={'naam': "Piet", 'cijfer': 5.5})

@app.route('/form', methods=['get', 'post'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        naam = request.form['naam']
        return f"Bedankt, {naam} voor het invullen!"    

if __name__ == "__main__":
    app.run(debug=True)