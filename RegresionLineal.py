import io
import os
import base64
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

IMG_DIR = "static/images"
def performRegression(file_path="data/RegresionLineal.csv", img_filename="regresion_lineal.png"):
  img_path = os.path.join(IMG_DIR, img_filename)

  if not os.path.exists(img_path):
    df = pd.read_csv(file_path)
    x = df[['X']]
    y = df['Y']

    model = LinearRegression()
    model.fit(x, y)

    plt.scatter(x, y, color="blue", label="Datos Reales")
    plt.plot(x, model.predict(x), color="red", label="Linea de Regresion")
    plt.title("Regresion Lineal Ventas")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()

    plt.savefig(img_path)
    plt.close()
  with open(img_path, "rb") as img_file:
    return base64.b64encode(img_file.read()).decode('utf8')