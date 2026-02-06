#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv

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


@app.route('/items')
def items():
    try:
        with open('items.json', 'r', encoding='utf-8') as file:
            list_items = json.load(file)
            items = list_items['items']
    except Exception:
        items = []
    return render_template('items.html', items=items)


@app.route('/products')
def products():

    file = request.args.get('source')
    id = request.args.get('id')

    if file == 'json':
        try:
            with open('products.json', 'r', encoding='utf-8') as json_content:
                data = json.load(json_content)
        except Exception as error:
            data = error
            return render_template('product_display.html', data=data)

    elif file == 'csv':
        try:
            with open('products.csv', 'r', encoding='utf-8') as csv_content:
                csv_reader = csv.DictReader(csv_content)
                data = []
                for row in csv_reader:
                    data.append(row)
        except Exception as error:
            data = error
            return render_template('product_display.html', data=data)

    else:
        data = "Wrong source"
        return render_template('product_display.html', data=data)

    if id:
        try:
            i = 0
            id = int(id)
            for product in data:
                if int(product.get('id')) == id:
                    data = [product]
                    i += 1
                    break
            if i == 0:
                data = "Product not found"
        except Exception as error:
            data = error

    return render_template('product_display.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
