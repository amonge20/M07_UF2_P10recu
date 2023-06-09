import pandas as pd
import matplotlib.pyplot as plt

def mostrar_megapixeles_por_movil(data):
    # Filtrar las 10 muestras de móviles
    muestras = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]
    muestras_filtradas = data[data['id'].isin(muestras)]

    # Crear un gráfico de barras para mostrar los megapíxeles por móvil
    plt.figure(figsize=(10, 6))
    plt.bar(muestras_filtradas['id'], muestras_filtradas['px_height'], color='blue', alpha=0.7)
    plt.xlabel('ID del móvil')
    plt.ylabel('Megapíxeles')
    plt.title('Megapíxeles de los móviles seleccionados')
    plt.xticks(muestras_filtradas['id'])
    plt.legend(['Megapíxeles'])
    plt.show()

# Cargar el archivo CSV utilizando pandas
data = pd.read_csv('test.csv')

# Llamar a la función para mostrar los megapíxeles por móvil en un gráfico de barras
mostrar_megapixeles_por_movil(data)
