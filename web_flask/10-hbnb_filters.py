#!/usr/bin/python3
"""Routes:
    /hbnb_filters: display a HTML page like 6-index.html,
        which was done during the project 0x01.
        AirBnB clone - Web static
    Copy files 3-footer.css, 3-header.css, 4-common.css
        and 6-filters.css from web_static/styles/
        to the folder web_flask/static/styles
    Copy files icon.png and logo.png from web_static/images/
        to the folder web_flask/static/images
    Update .popover class in 6-filters.css to allow scrolling
        in the popover and a max height of 300 pixels.
    Use 6-index.html content as source code for the template
        10-hbnb_filters.html:
    Replace the content of the H4 tag under each filter title
        (H3 States and H3 Amenities) by &nbsp;
    State, City and Amenity objects must be loaded from DBStorage
        and sorted by name (A->Z)
    You must use the option strict_slashes=False in your
        route definition
"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """hbnb filters function"""
    return render_template('6-index.html',
                           states=storage.all("State"),
                           amenities=storage.all("Amenity"))


@app.teardown_appcontext
def teardown(exc):
    """closing"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
