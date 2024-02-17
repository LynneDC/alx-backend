#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the index.html template.

    Returns:
        The rendered index.html template.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
