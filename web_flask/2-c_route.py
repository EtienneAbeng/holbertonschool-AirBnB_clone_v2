#!/usr/bin/python3
""" Module pour démarrer une application Flask """
from flask import Flask  # Importation de la classe Flask depuis le module flask

app = Flask(__name__)  # Création d'une instance de l'application Flask

@app.route('/', strict_slashes=False)  # Définition d'une route pour l'URL '/'
def hello_hbnb():
    return "Hello HBNB"  # Retourne "Hello HBNB" comme réponse à la requête

@app.route('/hbnb', strict_slashes=False)  # Définition d'une route pour l'URL '/hbnb'
def hbnb():
    return "HBNB"  # Retourne "HBNB" comme réponse à la requête

@app.route('/c/<text>', strict_slashes=False)  # Définition d'une route dynamique pour l'URL '/c/<text>'
def c_is_fun(text):
    return "C {}".format(text.replace('_', ' '))  # Retourne "C " suivi du texte avec les underscores remplacés par des espaces

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Démarrage du serveur Flask sur toutes les adresses IP et le port 5000
