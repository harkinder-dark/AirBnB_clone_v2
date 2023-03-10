#!/usr/bin/python3
"""
Routes:
    /states: display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present
                in DBStorage sorted by name (A->Z) tip
    LI tag: description of one State:
                <state.id>: <B><state.name></B>
    /states/<id>: display a HTML page: (inside the tag BODY)
        If a State object is found with this id:
        H1 tag: “State: ”
        H3 tag: “Cities:”
    UL tag: with the list of City objects linked to
                            the State sorted by name (A->Z)
    LI tag: description of one City: <city.id>: <B><city.name></B>
    Otherwise:
        H1 tag: “Not found!”
"""
from flask import Flask
from flask import render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """states function"""
    return render_template("9-states.html",
                           states=storage.all(State))


@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    """states for id"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", states=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """closing"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
