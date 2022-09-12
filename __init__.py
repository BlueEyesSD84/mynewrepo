#!/usr/bin/env python3
#-*-coding: utf8 -*-
"""Sample Hello World Flask App"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return("<h1>Hello, World!</>")

@app.products("/0")
def products():
    product_list = ["Apple", "Orange", "Pears"]
    bullet_list = "".join(
        "<li>%s</li>" % product for product in product_list
    )
    return "<ul>%s</ul>" %bullet_list