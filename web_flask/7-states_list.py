#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a list of states"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=get_state_name)

    return render_template('states_list.html', states=sorted_states)


def get_state_name(state):
    """Return the name of a state"""
    return state.name


@app.teardown_appcontext
def teardown_storage(exception):
    """Remove SQLAlchemy Session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
