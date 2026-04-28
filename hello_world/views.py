from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import Flask, render_template, request, jsonify

@app.route('/')
def index():
    if request.args.get('output') == 'json':
        return jsonify(imie="Pawel", mgs="Hello World!")
    else:
        return render_template('index.html')
