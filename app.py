from flask import Flask, render_template, request
import io
import os
import base64
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
IMG_DIR = "static/images"

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/CasoUsoMLSupervisado")
def CasoUsoMLSupervisado():
  investigationCU = {
    'title': 'Investigacion Caso de Uso Machine Learning Supervisado',
    'subtitle': 'Caso de Éxito: Spotify',
    'problem': 'En la industria de la musica, se necesita proporcionar recomendaciones personalizadas, ya que es crucial para que el usuario tenga una experiencia completa y personalizada.',
    'solution': 'Con K-Nearest Neighbors (KNN), y usando ML Supervisado, se logra predecir que canciones y artistas les gustarian a los usuarios.',
    'benefits': [
      'Personalizacion Avanzada.',
      'Mayor retencion de usuarios.',
      'Descubrimiento de nuevos artistas y generos.',
      'Mejores decisiones comerciales.'
    ]
  }
  
  return render_template(
    'CasoUsoMLSupervisado.html', 
    investigationCU=investigationCU
  )

@app.route("/RegresionLineal", methods=["POST", "GET"])
def RegresionLineal():
    file_path = "data/RegresionLineal.csv"
    img_filename = "regresion_lineal.png"

    img_path = os.path.join(IMG_DIR, img_filename)

    if not os.path.exists(img_path):
      df = pd.read_csv(file_path)
      x = df[['X']]
      y = df['Y']

      model = LinearRegression()
      model.fit(x, y)

      img = io.BytesIO()
      plt.scatter(x, y, color="blue", label="Datos Reales")
      plt.plot(x, model.predict(x), color="red", label="Linea de Regresion")
      plt.title("Regresion Lineal Ventas")
      plt.xlabel("X")
      plt.ylabel("Y")
      plt.legend()

      plt.savefig(img_path)
      plt.close()
    
    with open(img_path, "rb") as img_file:
      plot_url = base64.b64encode(img_file.read()).decode('utf8')

    return render_template (
      'RegresionLineal.html',
      plot_url = plot_url
    )