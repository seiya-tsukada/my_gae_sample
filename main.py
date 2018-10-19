#! /usr/bin/env python
# coding: utf-8

from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def index():
    return jsonify({"message": "hello world!"})

if __name__ == "__main__":
    app.run()