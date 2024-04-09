from flask import Flask  # Importation de la classe Flask depuis le module flask

app = Flask(__name__)  # Création d'une instance de l'application Flask

@app.route('/', strict_slashes=False)  # Définition d'une route pour l'URL '/'
def hello_hbnb():
    return "Hello HBNB"  # Retourne "Hello HBNB" comme réponse à la requête

@app.route('/hbnb', strict_slashes=False)  # Définition d'une route pour l'URL '/hbnb'
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)  # Définition d'une route dynamique pour l'URL '/c/<text>'
def c_is_fun(text):
    return "C {}".format(text.replace('_', ''))
'''
@app.route('/python/<text>', strict_slashes=False)  # Définition d'une route dynamique pour l'URL '/python/<text>'
def python_is_cool(text = 'is_cool'):
    return "Python {}".format(text.replace('_', ' '))  # Retourne "Python " suivi du texte avec les underscores remplacés par des espaces
'''
@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)    
def python_is_cool(text = 'is_cool'):
    return "Python {}".format(text.replace('_', '  '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Démarrage du serveur Flask sur toutes les adresses IP et le port 5000