#python3 -m flask --app app.py --debug run

from flaskapp import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template("index.html", name='dani')

@app.route('/p/<world>')
def param_world(world):
  return f'hello {world}'

@app.route('/b')
def bonojur_world():
  return 'bonjour world'