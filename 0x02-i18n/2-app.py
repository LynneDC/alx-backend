#!/usr/bin/env python3
'''Task 2: Get locale from request

This script is a Flask application that
handles internationalization (i18n) by
retrieving the locale from the request headers.
It uses the Flask-Babel extension
and the Babel library to handle translations and language preferences.
The main features of this script include:
- Setting up the Flask application with the necessary configurations for i18n.
- Defining a locale selector function that
determines the best match for the user's
 preferred language based on the available languages.
- Implementing a default route that renders the homepage template.
To run the application, execute this script directly.
'''

from flask import Flask, render_template, request
from flask_babel import Babel
from babel import Locale
from babel.support import Translations


class Config:
    """ class"""

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.

    Returns:
        str: best match
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    '''default route

    Returns:
        html: homepage
    '''
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
