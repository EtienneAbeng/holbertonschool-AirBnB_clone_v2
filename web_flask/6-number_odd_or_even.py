from flask import Flask, render_template  # Import des classes Flask et render_template

app = Flask(__name__)  # Création de l'application Flask

@app.route('/', strict_slashes=False)  # Route pour l'URL '/'
def hello_hbnb():
    return "Hello HBNB"  # Retourne "Hello HBNB"

@app.route('/hbnb', strict_slashes=False)  # Route pour l'URL '/hbnb'
def hbnb():
    return "HBNB"  # Retourne "HBNB"

@app.route('/c/<text>', strict_slashes=False)  # Route dynamique pour '/c/<text>'
def c_is_fun(text):
    return "C {}".format(text.replace('_', ''))  # Retourne "C <text>" sans underscores

@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)  # Route dynamique pour '/python/<text>'
def python_is_cool(text):
    return "Python {}".format(text.replace('_', ' '))  # Retourne "Python <text>" sans underscores

@app.route('/number/<int:n>', strict_slashes=False)  # Route dynamique pour '/number/<n>'
def number(n):
    return "{} is a number".format(n)  # Retourne "<n> is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)  # Route dynamique pour '/number_template/<n>'
def number_template(n):
    return render_template('5-number.html', n=n)  # Rend le modèle '5-number.html' avec n comme variable

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """odd_or_even = odd if n % 2 != 0 else even """
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Démarrage du serveur Flask sur toutes les adresses IP et le port 5000
