from flask import Flask
from flask.wrappers import Request
from werkzeug.utils import escape

app = Flask(__name__)

@app.route("/")#Decorador
def hello_world():
    return "<p>Hello World</p>"

@app.route("/teste")
def teste():
    return "<p> muca lol palhaço</p>"

@app.route("/teste2")
def teste2():
    return "<p> za waduro</p>"

@app.route("/cliente/<cliente>")
def mostra_cliente(cliente):
    return f'{escape(cliente)}'

if __name__ == "__main__":
    app.run(debug=True)

    