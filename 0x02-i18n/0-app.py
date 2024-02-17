#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
app.config['LANGUAGES'] = ['en', 'fr']
app.config['BABEL_DEFAULT_LOCALE'] = 'en'


@app.route('/')
def index():
    """
    Renders the index.html template.

    Returns:
        The rendered index.html template.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)