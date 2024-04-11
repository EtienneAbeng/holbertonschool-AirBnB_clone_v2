#!/usr/bin/python3
from flask import Flask, render_template  # Import des classes Flask et render_template

app = Flask(__name__)  # Crée une instance de l'application Flask

# Définit une route pour l'URL '/' qui renvoie "Hello HBNB"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Fonction qui renvoie 'Hello HBNB' """
    return "Hello HBNB"

# Définit une route pour l'URL '/hbnb' qui renvoie "HBNB"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Fonction qui renvoie 'HBNB' """
    return "HBNB"

# Définit une route dynamique pour '/c/<text>' qui renvoie "C " suivi du texte sans underscores
@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ Fonction qui renvoie 'C ' suivi du texte sans underscores """
    return "C {}".format(text.replace('_', ''))

# Définit une route dynamique pour '/python/<text>' qui renvoie "Python " suivi du texte sans underscores
@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """ Fonction qui renvoie 'Python ' suivi du texte sans underscores """
    return "Python {}".format(text.replace('_', ' '))

# Définit une route dynamique pour '/number/<n>' qui renvoie "<n> is a number"
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Fonction qui renvoie '<n> is a number' """
    return "{} is a number".format(n)

# Définit une route dynamique pour '/number_template/<n>' qui rend le modèle '5-number.html' avec n comme variable
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Fonction qui rend le modèle '5-number.html' avec n comme variable """
    return render_template('5-number.html', n=n)

# Définit une route dynamique pour '/number_odd_or_even/<n>' qui rend le modèle '6-number_odd_or_even.html' avec n comme variable
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ Fonction qui rend le modèle '6-number_odd_or_even.html' avec n comme variable """
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Démarrage du serveur Flask sur toutes les adresses IP et le port 5000
