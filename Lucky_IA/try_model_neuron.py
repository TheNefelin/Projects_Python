import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from datetime import datetime

# Leer y Preparar los Datos ----------------------------------------------------
ARCHIVO_EXCEL = 'data_test.xlsx'
MODEL = "modelo_neuron.h5"
CANTIDAD_NUMEROS = 6  # Cantidad de números a predecir

# Leer el archivo Excel
def leer_datos(archivo):
    df = pd.read_excel(archivo)
    df['Fecha'] = pd.to_datetime(df['Fecha'])  # Convertir la fecha al formato adecuado
    print(f"Cantidad de registros en el archivo: {df.shape[0]}")
    return df

datos = leer_datos(ARCHIVO_EXCEL)

# Preparar los datos
def preparar_datos(df):
    df['FechaOrdinal'] = df['Fecha'].apply(lambda x: x.toordinal())
    X = df[['FechaOrdinal']].values.astype(np.float32)  # Asegurar tipo float32
    Y = df.iloc[:, :-2].values.astype(np.float32)  # Usar float32
    return X, Y

X, Y = preparar_datos(datos)

# Dividir los datos
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Crear el Modelo --------------------------------------------------------------
def crear_modelo():
    modelo = Sequential([
        Dense(64, activation='relu', input_shape=(1,)),  # Aumento las neuronas en la primera capa
        Dense(128, activation='relu'),                   # Nueva capa oculta
        Dense(64, activation='relu'),                    # Otra capa oculta
        Dense(CANTIDAD_NUMEROS, activation='linear')     # Salida: valores continuos
    ])
    modelo.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])
    return modelo

modelo = crear_modelo()

# Entrenar el modelo
modelo.fit(X_train, Y_train, epochs=50, batch_size=16, validation_split=0.1)
print("Modelo entrenado")

# Guardar el modelo
modelo.save(MODEL)
print(f"Modelo guardado en {MODEL}")

# Evaluar el modelo
loss, mae = modelo.evaluate(X_test, Y_test)
print(f"Pérdida: {loss}, Error absoluto medio (MAE): {mae}")


# Predecir para una fecha específica -------------------------------------------
# def predecir_para_fecha(fecha, modelo):
#     fecha_ordinal = datetime.strptime(fecha, '%Y-%m-%d').toordinal()
#     X_nueva = np.array([[fecha_ordinal]], dtype=np.float32)
#     prediccion = modelo.predict(X_nueva)[0]
    
#     # Redondear y prevenir repeticiones
#     prediccion_redondeada = np.round(prediccion).astype(int)
#     prediccion_unica = ajustar_a_unicos(prediccion_redondeada)
    
#     # Convertir a enteros nativos de Python
#     return [int(num) for num in prediccion_unica]

# # Función para ajustar los números predichos a valores únicos ------------------
# def ajustar_a_unicos(prediccion):
#     prediccion_unica = []
#     for num in prediccion:
#         while num in prediccion_unica:
#             num += 1  # Incrementar hasta encontrar un valor único
#         prediccion_unica.append(num)
#     return sorted(prediccion_unica)  # Ordenar los números para mantener consistencia

# fecha_input = "2024-11-20"
# prediccion = predecir_para_fecha(fecha_input, modelo)
# print(f"Predicción para la fecha {fecha_input}: {prediccion}")

# ------------------------------------------------------------------------------

