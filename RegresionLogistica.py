import os
import base64
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

IMG_DIR = "static/images"

def performLogisticRegression(file_path="data/RegresionLogistica.csv", img_filename="regresion_logistica.png"):
  img_path = os.path.join(IMG_DIR, img_filename)

  if not os.path.exists(img_path):
    df = pd.read_csv(file_path)

    df['target'] = (df['Y'] > 0).astype(int)

    X = df[['X', 'Y']]
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)

    fig, ax = plt.subplots(figsize=(5, 5))

    cax = ax.matshow(conf_matrix, cmap="Blues", alpha=0.6)

    for (i, j), val in np.ndenumerate(conf_matrix):
      ax.text(j, i, f'{val}', ha='center', va='center', color='red')

    plt.title('Matriz de Confusión')
    plt.xlabel('Predicciones')
    plt.ylabel('Valores reales')
    plt.colorbar(cax)

    plt.savefig(img_path)
    plt.close()

  with open(img_path, "rb") as img_file:
    confusion_img = base64.b64encode(img_file.read()).decode('utf8')
  
  return confusion_img