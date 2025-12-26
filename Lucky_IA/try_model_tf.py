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
fecha_referencia = datetime(2025, 12, 28)  # Fecha de referencia
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

# ============================================
# TABLA DE EVALUACIÓN - AGREGADA AL FINAL
# ============================================

print('\n' + '='*60)
print('📊 TABLA DE EVALUACIÓN - ¿QUÉ SIGNIFICA TU PÉRDIDA?')
print('='*60)

# Mostrar la tabla
print("\n┌─────────────────┬──────────────────┬─────────────────────┐")
print("│   Rango Loss    │     Calidad      │  Error Promedio (1-41) │")
print("├─────────────────┼──────────────────┼─────────────────────┤")

rangos = [
    (0.00, 0.10, "✅ EXCELENTE", "2-4 números"),
    (0.10, 0.30, "👍 BUENO", "4-12 números"),
    (0.30, 0.70, "⚠️ REGULAR", "12-28 números"),
    (0.70, 1.50, "❌ MALO", "28-61 números"),
    (1.50, 10.0, "🚨 MUY MALO", ">61 números")
]

for rango_min, rango_max, calidad, error in rangos:
    print(f"│  {rango_min:.2f} - {rango_max:.2f}  │ {calidad:<16} │ {error:<19} │")

print("└─────────────────┴──────────────────┴─────────────────────┘")

# Evaluar tu pérdida específica
print(f'\n📈 TU RESULTADO: loss = {test_loss:.6f}')

if test_loss < 0.10:
    print(f'   ✅ EXCELENTE - Tu modelo predice muy bien')
    print(f'   🎯 Error aproximado: {test_loss * 41:.1f} números de diferencia')
elif test_loss < 0.30:
    print(f'   👍 BUENO - Predicciones aceptables')
    print(f'   🎯 Error aproximado: {test_loss * 41:.1f} números de diferencia')
elif test_loss < 0.70:
    print(f'   ⚠️ REGULAR - Necesita mejorar')
    print(f'   🎯 Error aproximado: {test_loss * 41:.1f} números de diferencia')
elif test_loss < 1.50:
    print(f'   ❌ MALO - Revisar datos o modelo')
    print(f'   🎯 Error aproximado: {test_loss * 41:.1f} números de diferencia')
else:
    print(f'   🚨 MUY MALO - Problemas graves en el modelo')
    print(f'   🎯 Error aproximado: {test_loss * 41:.1f} números de diferencia')

# Mostrar ejemplo de lo que significa el error
print(f'\n🔍 ¿QUÉ SIGNIFICA ESTO EN LA PRÁCTICA?')
print(f'   Si predices el número 20 con loss {test_loss:.3f}:')
print(f'   • Tu predicción real podría ser: {20 + (test_loss * 41):.1f}')
print(f'   • O podría ser: {20 - (test_loss * 41):.1f}')

print('\n' + '='*60)
print('💡 CONSEJO: Un loss < 0.30 es buen resultado para empezar')
print('='*60)

# Mostrar también los números predichos en detalle (opcional)
print(f'\n🎯 TUS NÚMEROS PREDICHOS DETALLADOS:')
numeros_enteros = [int(round(num)) for num in numeros_predichos[0]]
numeros_ajustados = [max(1, min(41, num)) for num in numeros_enteros]

print(f'1. Valores exactos: {[f"{num:.2f}" for num in numeros_predichos[0]]}')
print(f'2. Redondeados: {numeros_enteros}')
print(f'3. Ajustados (1-41): {numeros_ajustados}')

if len(set(numeros_ajustados)) < 6:
    print(f'4. ⚠️  Atención: Hay números repetidos')
else:
    print(f'4. ✅ Todos los números son únicos')