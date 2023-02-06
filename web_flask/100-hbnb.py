#!/usr/bin/python3
"""
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """function hbnb"""
    return render_template("100.hbnb.html",
                           states=storage.all("State"),
                           amenities=storage.all("Amenity"),
                           places=storage.all("Place"))

@app.teardown_appcontext
def teardown(exc):
    """closing"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
