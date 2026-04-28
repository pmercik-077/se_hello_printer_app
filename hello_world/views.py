from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import request, jsonify, render_template


@app.route("/")
def index(request):
    return render(request, 'index.html') 
    data = {"imie": "Pawel", "msg": "Hello world!"}

    if request.args.get("output") == "json":
        return jsonify(data)
    return render_template("index.html", data=data)


moje_imie = "Pawel"
msg = "Hello World!"


@app.route('/')
def index(request):
    return render(request, 'home.html')
    output = request.args.get('output')
    if not output:
        output = PLAIN
    return get_formatted(msg, moje_imie,
                         output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)
