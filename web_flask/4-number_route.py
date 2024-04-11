#!/usr/bin/python3
""" Module pour démarrer une application Flask """

from flask import Flask

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

# Définit une route dynamique pour l'URL '/c/<text>' qui renvoie "C " suivi du texte sans underscores
@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ Fonction qui renvoie 'C ' suivi du texte sans underscores """
    return "C {}".format(text.replace('_', ''))

# Définit une route pour l'URL '/python/<text>' et '/python/'
# qui renvoie "Python " suivi du texte sans underscores
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """ Fonction qui renvoie 'Python ' suivi du texte sans underscores """
    return "Python {}".format(text.replace('_', ' '))

# Définit une route dynamique pour l'URL '/number/<n>' qui renvoie "<n> is a number"
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Fonction qui renvoie '<n> is a number' """
    return "{} is a number".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Démarre le serveur Flask sur toutes les adresses IP et le port 5000
