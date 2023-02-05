#!/usr/bin/python3
"""
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)

@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """hbnb filters function"""
    return render_template('6-index.html')

@app.teardown_appcontext
def teardown(exc):
    """closing"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")