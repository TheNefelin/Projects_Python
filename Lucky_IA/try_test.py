import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from datetime import datetime, timedelta

# Configuración ----------------------------------------------------------------
CANTIDAD_NUMEROS = 6  # Cantidad de números a elegir aleatoriamente
RANGO_MAXIMO = 41     # Rango máximo para el random
ARCHIVO_EXCEL = "data_test.xlsx"

# Función para generar una fecha aleatoria -------------------------------------
def generar_fecha_aleatoria(inicio, fin):
    """Genera una fecha aleatoria entre dos fechas."""
    delta = fin - inicio
    dias_random = np.random.randint(0, delta.days + 1)
    return inicio + timedelta(days=dias_random)

# Generar Secuencias de Números Aleatorios -------------------------------------
def generar_secuencias_excel(cantidad, archivo):
  secuencias = [np.random.choice(range(1, RANGO_MAXIMO +1), size=CANTIDAD_NUMEROS, replace=False) for _ in range(cantidad)]
  
  # Generar fechas aleatorias
  fecha_inicio = datetime(1998, 1, 1)
  fecha_fin = datetime.now()
  fechas = [generar_fecha_aleatoria(fecha_inicio, fecha_fin) for _ in range(cantidad)]
  
  # Convertir las secuencias a un DataFrame
  df = pd.DataFrame(secuencias, columns=[f"Número {i+1}" for i in range(CANTIDAD_NUMEROS)])
  df["Fecha"] = fechas

  # Guardar las secuencias en un archivo Excel
  df.to_excel(archivo, index=False)
  
  print(f"Secuencias guardadas en {archivo}")

  return df

# Generar 1000 secuencias y guardarlas en un archivo Excel
secuencias = generar_secuencias_excel(1000, ARCHIVO_EXCEL)

# Organizar los Datos ----------------------------------------------------------
# Convertir las secuencias a un DataFrame
df = pd.DataFrame(secuencias, columns=[f"Número {i+1}" for i in range(CANTIDAD_NUMEROS)])

# Mostrar las primeras filas
print(df.head())

# Visualizar Distribuciones ----------------------------------------------------
# Unir todas las columnas en una sola para analizar frecuencias
todos_los_numeros = pd.melt(df, var_name="Posición", value_name="Número")

# Graficar la distribución de frecuencias
plt.figure(figsize=(10, 6))
sns.histplot(todos_los_numeros["Número"], bins=RANGO_MAXIMO , kde=True, color="blue")
plt.title("Distribución de Frecuencias de Números")
plt.xlabel("Número")
plt.ylabel("Frecuencia")
plt.show()

# Extraer Patrones con IA ------------------------------------------------------
# Convertir las secuencias a una representación numérica
datos = df.to_numpy()

# Aplicar K-Means con 5 clusters
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(datos)

# Agregar los resultados al DataFrame
df['Cluster'] = kmeans.labels_

# Mostrar un resumen
print(df.groupby('Cluster').size())

# Visualizar Clusters ----------------------------------------------------------
# Reducir dimensiones a 2D para graficar
pca = PCA(n_components=2)
reducido = pca.fit_transform(datos)

# Crear un DataFrame para graficar
df_reducido = pd.DataFrame(reducido, columns=["Componente 1", "Componente 2"])
df_reducido['Cluster'] = kmeans.labels_

# Graficar los clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_reducido, x="Componente 1", y="Componente 2", hue="Cluster", palette="tab10")
plt.title("Clusters de Secuencias Aleatorias")
plt.show()

# ------------------------------------------------------------------------------
