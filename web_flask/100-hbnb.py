#!/usr/bin/python3
"""Routes:
        /hbnb: display a HTML page like 8-index.html,
            done during the 0x01. AirBnB clone
            - Web static project
        Copy files 3-footer.css, 3-header.css, 4-common.css,
            6-filters.css and 8-places.css from web_static/styles/
            to the folder web_flask/static/styles
        Copy all files from web_static/images/ to the folder
            web_flask/static/images
        Update .popover class in 6-filters.css to enable scrolling
            in the popover and set max height to 300 pixels.
        Update 8-places.css to always have the price by night on the
            top right of each place element, and the name correctly
            aligned and visible (i.e. screenshots below)
        Use 8-index.html content as source code for the template
            100-hbnb.html:
        Replace the content of the H4 tag under each filter title
            (H3 States and H3 Amenities) by &nbsp;
        Make sure all HTML tags from objects are correctly used
            (example: <BR /> must generate a new line)
        State, City, Amenity and Place objects must be loaded from
            DBStorage and sorted by name (A->Z)
        You must use the option strict_slashes=False in your
        route definition
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """function hbnb"""
    return render_template("100.hbnb.html",
                           states=storage.all(State),
                           amenities=storage.all(Amenity),
                           places=storage.all(Place))


@app.teardown_appcontext
def teardown(exc):
    """closing"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
