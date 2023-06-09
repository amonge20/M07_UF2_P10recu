import pandas as pd
import matplotlib.pyplot as plt

def mostrar_densitat_per_ciutat_m2(data):
    # Filtrar las 10 primeras ciudades
    top_10_ciudades = data.head(10)

    # Convertir la columna "Density per M2" a valores numéricos y reemplazar NaN por cero
    top_10_ciudades['Density per M2'] = pd.to_numeric(top_10_ciudades['Density M2'].str.replace(',', ''), errors='coerce').fillna(0)

    # Crear un gráfico de pie de la densidad por m² de cada ciudad
    plt.figure(figsize=(8, 8))
    plt.pie(top_10_ciudades['Density per M2'], labels=top_10_ciudades['City'], autopct='%1.1f%%')
    plt.title('Densidad por m² de las 10 primeras ciudades')
    plt.legend()
    plt.show()

# Cargar el archivo CSV utilizando pandas
data = pd.read_csv('List of cities proper by population density11.csv')

# Llamar a la función para mostrar la densidad por m² de las 10 ciudades en un gráfico de pie
mostrar_densitat_per_ciutat_m2(data)
