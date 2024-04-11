#!/usr/bin/python3
""" COMMENt"""
from flask import Flask  # Importation de la classe Flask depuis le module flask


app = Flask(__name__)  # Création d'une instance de l'application Flask


@app.route('/', strict_slashes=False)  # Définition d'une route pour l'URL '/'
def hello_hbnb():  # Fonction exécutée lorsque l'URL '/' est accédée
    """ Fonction retournant 'Hello HBNB!' """
    return "Hello HBNB!"  # Retourne "Hello HBNB!" comme réponse à la requête


if __name__ == '__main__':  # Vérification si le script est exécuté directement
    app.run(host='0.0.0.0', port=5000)  # Démarrage du serveur Flask sur toutes les adresses IP (0.0.0.0) et le port 5000
