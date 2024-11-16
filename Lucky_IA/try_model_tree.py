import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Leer y Preparar los Datos ----------------------------------------------------
# Constantes
ARCHIVO_EXCEL = 'data_test.xlsx'
MODEL = "modelo_tree.pkl"
RANGO_MAXIMO = 41
CANTIDAD_NUMEROS = 6  # Cantidad de números a predecir

# Leer el archivo Excel
def leer_datos(archivo):
  df = pd.read_excel(archivo)
  df['Fecha'] = pd.to_datetime(df['Fecha'])  # Convertir la fecha al formato adecuado
  print(f"Cantidad de registros en el archivo: {df.shape[0]}")
  return df

datos = leer_datos(ARCHIVO_EXCEL)
print(datos.head())

# Entrenamiento del Modelo -----------------------------------------------------
def preparar_datos(df):
  # Convertir las fechas a números ordinales
  df['FechaOrdinal'] = df['Fecha'].apply(lambda x: x.toordinal())
  
  # Crear X (entrada) y Y (salida)
  X = df[['FechaOrdinal']]
  Y = df.iloc[:, :-2].values  # Las columnas de números
  
  return X, Y

X, Y = preparar_datos(datos)

# Dividir los datos para entrenamiento y prueba
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Entrenar un modelo
def entrenar_modelo(X, Y):
  modelo = RandomForestClassifier(n_estimators=100, random_state=42)
  modelo.fit(X, Y)
  return modelo

modelo = entrenar_modelo(X_train, Y_train)
print("Modelo entrenado")

# Guardar el modelo para uso futuro
joblib.dump(modelo, MODEL)
print("Modelo guardado")

# ------------------------------------------------------------------------------
