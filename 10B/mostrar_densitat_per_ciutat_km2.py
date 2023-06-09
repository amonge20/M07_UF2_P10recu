import pandas as pd
import matplotlib.pyplot as plt

def mostrar_densitat_per_ciutat_km2(data):
    # Eliminar filas con valores NaN en la columna "Density KM2"
    data = data.dropna(subset=['Density KM2'])

    # Convertir la columna "Density KM2" a tipo de dato numérico
    data['Density KM2'] = data['Density KM2'].astype(int)

    # Filtrar las 10 ciudades con mayor densidad de población
    top_10_ciudades = data.nlargest(10, 'Density KM2')

    # Crear un gráfico de tipo pie con la densidad por km² de cada ciudad
    plt.figure(figsize=(8, 8))
    plt.pie(top_10_ciudades['Density KM2'], labels=top_10_ciudades['City'], autopct='%1.1f%%')
    plt.title('Densidad por km² de las 10 ciudades con mayor densidad de población')
    plt.legend()
    plt.show()

# Cargar el archivo CSV utilizando pandas
data = pd.read_csv('List of cities proper by population density11.csv', thousands=',')

# Llamar a la función para mostrar la densidad por km² de las 10 ciudades en un gráfico de tipo pie
mostrar_densitat_per_ciutat_km2(data)
