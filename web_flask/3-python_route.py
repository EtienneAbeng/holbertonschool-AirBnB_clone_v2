#!/usr/bin/python3
''' Module pour démarrer une application Flask '''

from flask import Flask

app = Flask(__name__)

# Définit une route pour l'URL '/' qui renvoie "Hello HBNB"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    ''' Fonction exécutée lorsque l'URL '/' est accédée '''
    return "Hello HBNB"

# Définit une route pour l'URL '/hbnb' qui renvoie "HBNB"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' Fonction exécutée lorsque l'URL '/hbnb' est accédée '''
    return "HBNB"

# Définit une route dynamique pour l'URL '/c/<text>'
# qui renvoie "C " suivi du texte avec les underscores remplacés par des espaces
@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    ''' Fonction exécutée lorsque l'URL '/c/<text>' est accédée '''
    return "C {}".format(text.replace('_', ' '))

# Définit une route pour l'URL '/python/<text>' et '/python/'
# qui renvoie "Python " suivi du texte avec les underscores remplacés par des espaces
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    ''' Fonction exécutée lorsque l'URL '/python/<text>' est accédée '''
    return "Python {}".format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
