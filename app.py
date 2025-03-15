import re
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

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