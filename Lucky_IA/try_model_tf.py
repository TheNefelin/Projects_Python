# Importar las librerías necesarias
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers, models

# --- Paso 1: Cargar y preprocesar los datos ---

# Cargar los datos desde un archivo CSV (o puede ser otro formato)
df = pd.read_excel("data_hist.xlsx")

# Convertir las fechas a número de días desde una fecha de referencia
fecha_referencia = datetime(2024, 12, 8)  # Fecha de referencia
df['Fecha'] = pd.to_datetime(df['Fecha'])
df['Dias'] = (df['Fecha'] - fecha_referencia).dt.days

# Normalizar los números entre 1 y 41
scaler = MinMaxScaler(feature_range=(0, 1))
numeros = df[['Número 1', 'Número 2', 'Número 3', 'Número 4', 'Número 5', 'Número 6']].values
numeros_normalizados = scaler.fit_transform(numeros)

# Crear un DataFrame con los datos de entrada (Fecha convertida en días) y las salidas (Números normalizados)
X = df['Dias'].values.reshape(-1, 1)  # Fecha convertida en días
y = numeros_normalizados  # Números normalizados

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ver los datos preprocesados (opcional)
print(X_train[:5])
print(y_train[:5])

# --- Paso 2: Construcción del modelo de red neuronal ---

# Construcción del modelo de red neuronal
model = models.Sequential([
    layers.Dense(128, activation='relu', input_dim=1),  # Capa densa con 128 neuronas y ReLU
    layers.Dense(64, activation='relu'),  # Capa densa con 64 neuronas y ReLU
    layers.Dense(6, activation='sigmoid')  # Capa de salida con 6 neuronas (los números normalizados)
])

# Compilación del modelo
model.compile(optimizer='adam', loss='mean_squared_error')

# Entrenamiento del modelo
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

# Evaluar el modelo en los datos de prueba
test_loss = model.evaluate(X_test, y_test)
print('---------------------->')
print(f'Pérdida en datos de prueba: {test_loss}')
print('---------------------->')

# --- Paso 3: Realizar predicciones ---

# Predecir los números para una fecha de ejemplo
fecha_ejemplo = datetime(2024, 11, 17)
dias_ejemplo = (fecha_ejemplo - fecha_referencia).days

# Realizar la predicción
prediccion_normalizada = model.predict(np.array([[dias_ejemplo]]))

# Desnormalizar los números (convertirlos al rango original de 1 a 41)
numeros_predichos = scaler.inverse_transform(prediccion_normalizada)

# Mostrar los números predichos
print(f'Predicción de los 6 números: {np.round(numeros_predichos)}')
