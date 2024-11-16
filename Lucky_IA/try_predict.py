import pandas as pd
import numpy as np
from datetime import datetime
import joblib
from tensorflow.keras.models import load_model  # Para cargar el modelo neuronal

# Constantes
FECHA_PREDICCION = "2024-12-31"  # Cambia esta constante según la fecha que desees
MODEL_TREE = "modelo_tree.pkl"
MODEL_NEURON = "modelo_neuron.h5"
ARCHIVO_EXCEL = 'data_test.xlsx'  # El archivo donde guardarás las predicciones

# Cargar modelos entrenados
def cargar_modelo(nombre_archivo, tipo='tree'):
  if tipo == 'tree':
    return joblib.load(nombre_archivo)
  elif tipo == 'neuron':
    return load_model(nombre_archivo)
  else:
    raise ValueError("Tipo de modelo no soportado: elige 'tree' o 'neuron'.")

# Predecir números para una fecha
def predecir_para_fecha(fecha, modelo, tipo='tree'):
  fecha_ordinal = datetime.strptime(fecha, '%Y-%m-%d').toordinal()
  X_nueva = np.array([[fecha_ordinal]])  # Convertir la fecha a formato entrada
  
  if tipo == 'tree':
    # Predicción para modelo de árbol
    prediccion = modelo.predict(X_nueva)
    # Asegurarse de que se redondeen los valores
    prediccion = np.round(prediccion).astype(int)
  elif tipo == 'neuron':
    # Predicción para modelo neuronal
    prediccion = modelo.predict(X_nueva)
    # Si la salida es un conjunto de probabilidades, tomamos las predicciones continuas
    # Es importante asegurarse de que el modelo neuronal también devuelva múltiples números.
    prediccion = np.round(prediccion.flatten()).astype(int)  # Aplanar y redondear las predicciones
  else:
    raise ValueError("Tipo de modelo no soportado: elige 'tree' o 'neuron'.")
  
  return prediccion

# Main
if __name__ == "__main__":
  try:
    # Cargar ambos modelos
    modelo_tree = cargar_modelo(MODEL_TREE, tipo='tree')
    modelo_neuron = cargar_modelo(MODEL_NEURON, tipo='neuron')
    print("Modelos cargados exitosamente.")
    
    # Predecir con el modelo de árbol
    prediccion_tree = predecir_para_fecha(FECHA_PREDICCION, modelo_tree, tipo='tree')
    
    # Predecir con el modelo neuronal
    prediccion_neuron = predecir_para_fecha(FECHA_PREDICCION, modelo_neuron, tipo='neuron')

    print(f"Predicción con modelo Tree para la fecha {FECHA_PREDICCION}: {prediccion_tree}")
    print(f"Predicción con modelo Neuron para la fecha {FECHA_PREDICCION}: {prediccion_neuron}")
  except FileNotFoundError as e:
    print(f"Error: {e}. Asegúrate de que los archivos existan en el directorio.")
  except Exception as e:
    print(f"Error inesperado: {e}")
