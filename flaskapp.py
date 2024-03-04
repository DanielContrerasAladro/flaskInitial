# python3 ejemplo1.py

from flask import Flask,render_template, request

app = Flask(__name__)

valores = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "cierto": False
  }

@app.route('/')
def principal():
  return render_template("portada.html", valores=valores, lista=["uno","dos","tres"])

@app.route('/adios')
def adios():
  return '<h1>adioos</h1>'

@app.route('/saludar/<nombre>')
def saludar(nombre):
  return f'<h1>{nombre[11]}</h1>'


@app.route('/c1')
def c1():
  return render_template("contenido1.html", valores=valores, lista=["uno","dos","tres"])

@app.route('/c2')
def c2():
  nombre = request.args.get('nombre')
  apellidos = request.args.get('apellidos')
  return render_template("contenido2.html", valores=valores, lista=["uno","dos","tres"], nombre=nombre, apellidos=apellidos)


if __name__ == '__main__':
  app.run(debug = True)