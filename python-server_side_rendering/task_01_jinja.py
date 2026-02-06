#!/usr/bin/python3

from flask import Flask, render_template

'''Module that use jinja for reusable html code, and load all the data in
the server side'''

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
