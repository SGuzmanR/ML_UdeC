from flask import Flask, render_template, request
from RegresionLineal import performRegression
from RegresionLogistica import performLogisticRegression

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

@app.route("/ImplementacionRLogistica", methods=["POST", "GET"])
def ImplementacionRLogistica():
  confusion_img = performLogisticRegression()

  return render_template (
    'ImplementacionRLogistica.html',
    confusion_img = confusion_img
  )