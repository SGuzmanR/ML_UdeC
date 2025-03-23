from flask import Flask, render_template, request
from RegresionLineal import performRegression

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/CasoUsoMLSupervisado")
def CasoUsoMLSupervisado():  
  return render_template(
    'CasoUsoMLSupervisado.html', 
  )

@app.route("/RegresionLineal", methods=["POST", "GET"])
def RegresionLineal():
    plot_url = performRegression()

    return render_template (
      'RegresionLineal.html',
      plot_url = plot_url
    )

@app.route("/RegresionLogistica")
def RegresionLogistica():
  return render_template ('RegresionLogistica.html')