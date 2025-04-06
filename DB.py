import sqlite3
from flask import g

modelos = [
  (
    "Regresión Logística", 
    "Es un modelo de clasificación utilizado para predecir una variable dependiente binaria, usando una combinación lineal de características. Por ejemplo, supongamos que desea adivinar si el visitante de su sitio web va a hacer clic en el botón de pago de su carrito de compras o no. El análisis de regresión logística analiza el comportamiento de los visitantes anteriores, como el tiempo que permanecen en el sitio web y la cantidad de artículos que hay en el carrito. Determina que, si anteriormente los visitantes pasaban más de cinco minutos en el sitio y agregaban más de tres artículos al carrito, hacían clic en el botón de pago. Con esta información, la función de regresión logística puede predecir el comportamiento de un nuevo visitante en el sitio web.", 
    "https://aws.amazon.com/es/what-is/logistic-regression/#:~:text=La%20regresi%C3%B3n%20log%C3%ADstica%20es%20una,entre%20dos%20factores%20de%20datos. ", 
    "/static/images/DB/RegresionLogistica.jpg"
  ),
  (
    "K-Nearest Neighbors (KNN) ", 
    "Clasifica un punto basado en las clases más comunes entre sus 'K' vecinos más cercanos en el espacio de características. El algoritmo de k vecinos más cercanos, también conocido como KNN o k-NN, es un clasificador de aprendizaje supervisado no paramétrico, que utiliza la proximidad para hacer clasificaciones o predicciones sobre la agrupación de un punto de datos individual. Si bien se puede usar para problemas de regresión o clasificación, generalmente se usa como un algoritmo de clasificación, partiendo de la suposición de que se pueden encontrar puntos similares cerca uno del otro.", 
    "https://www.ibm.com/mx-es/topics/knn", 
    "/static/images/DB/KNN.jpg"
  ),
  (
    "Random Forest", 
    "Un conjunto de árboles de decisión que realiza predicciones mediante un voto mayoritario de múltiples arboles individuales. Los algoritmos de bosque aleatorio tienen tres hiperparámetros principales, que deben configurarse antes del entrenamiento. Estos incluyen el tamaño del nodo, la cantidad de árboles y la cantidad de características muestreadas. A partir de ahí, el clasificador de bosque aleatorio se puede utilizar para resolver problemas de regresión o clasificación.", 
    "https://www.ibm.com/mx-es/think/topics/random-forest", 
    "/static/images/DB/RandomForest.png"
  ),
  (
    "Arboles de Decisión", 
    "Un árbol de decisión es un algoritmo de aprendizaje supervisado no paramétrico, que se utiliza tanto para tareas de clasificación como de regresión. Tiene una estructura jerárquica de árbol, que consta de un nodo raíz, ramas, nodos internos y nodos hoja. Como puede ver en el siguiente diagrama, un árbol de decisión comienza con un nodo raíz, que no tiene ninguna rama entrante. Las ramas salientes del nodo raíz luego alimentan los nodos internos, también conocidos como nodos de decisión. En función de las características disponibles, ambos tipos de nodos realizan evaluaciones para formar subconjuntos homogéneos, que se denotan mediante nodos hoja o nodos terminales. Los nodos hoja representan todos los resultados posibles dentro del conjunto de datos.", 
    "https://www.ibm.com/es-es/think/topics /decision-trees", 
    "/static/images/DB/ArbolesDecision.jpg"
  ),
  (
    "Support Vector Machine (SVM)", 
    "SVM funciona correlacionando datos a un espacio de características de grandes dimensiones de forma que los puntos de datos se puedan categorizar, incluso si los datos no se puedan separar linealmente de otro modo. Se detecta un separador entre las categorías y los datos se transforman de forma que el separador se puede extraer como un hiperplano. Tras ello, las características de los nuevos datos se pueden utilizar para predecir el grupo al que pertenece el nuevo registro.", 
    "https://www.ibm.com/docs/es/spss-modeler/saas?topic=models-how-svm-works", 
    "/static/images/DB/SVM.jpg"
  ),
  (
    "Gradient Boosting (XGBoost, etc)", 
    "Una técnica de ensamblado que construye modelos de manera secuencial, donde cada nuevo modelo intenta corregir los errores de los anteriores.Este algoritmo construye un modelo aditivo de forma progresiva por etapas; permite la optimización de funciones de pérdida diferenciables arbitrarias. En cada etapa, los árboles de regresión de n_clases_ se ajustan al gradiente negativo de la función de pérdida, por ejemplo, la pérdida logarítmica binaria o multiclase. La clasificación binaria es un caso especial en el que sólo se induce un único árbol de regresión.", 
    "https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html", 
    "/static/images/DB/GradientBoosting.png"
  ),
  (
    "Naive Bayes", 
    "Un clasificador probabilistico basado en el teorema de Bayes, asumiendo independencia entre las características. Naïve Bayes forma parte de una familia de algoritmos de aprendizaje generativo, lo que significa que busca modelar la distribución de las entradas de una clase o categoría determinada. A diferencia de los clasificadores discriminativos, como la regresión logística, no aprende qué características son las más importantes para diferenciar entre clases.", 
    "https://www.ibm.com/es-es/think/topics/naive-bayes", 
    "/static/images/DB/NaiveBayes.png"
  )
]

def getDB():
  db = getattr(g, '_database', None)
  if db is None:
    db = g._database = sqlite3.connect('ML.db')
    print("Connected to DB")
    cursor = db.cursor()

    cursor.execute("""
      CREATE TABLE IF NOT EXISTS modelos (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nombre TEXT NOT NULL, 
        descripcion TEXT NOT NULL, 
        fuente TEXT NOT NULL, 
        imagen TEXT NOT NULL
      )
    """)

    cursor.executemany("INSERT INTO modelos (nombre, descripcion, fuente, imagen) VALUES (?, ?, ?, ?)", modelos)

    # Print DB Rows
    for row in cursor.execute("SELECT * FROM modelos"):
      print(row)

    cursor.execute("SELECT * FROM modelos")
  return cursor.fetchall()


def close_db(exception):
  db = getattr(g, '_database', None)
  if db is not None:
    db.close()