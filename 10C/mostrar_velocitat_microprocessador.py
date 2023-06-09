import pandas as pd
import matplotlib.pyplot as plt

def mostrar_velocitat_microprocessador(data):
    # Filtrar las muestras de móviles seleccionados
    muestras_seleccionadas = data[data['id'].isin([3, 13, 34, 56, 70, 85, 110, 120, 210, 400])]

    # Crear una gráfica de barras de la velocidad del microprocesador
    plt.figure(figsize=(10, 6))
    plt.bar(muestras_seleccionadas['id'], muestras_seleccionadas['clock_speed'])
    plt.xlabel('ID del móvil')
    plt.ylabel('Velocidad del microprocesador')
    plt.title('Velocidad del microprocesador de los móviles seleccionados')
    plt.xticks(muestras_seleccionadas['id'])
    plt.legend(['Velocidad'])
    plt.show()

# Cargar el archivo CSV utilizando pandas
data = pd.read_csv('test.csv')

# Llamar a la función para mostrar la velocidad del microprocesador de los móviles seleccionados
mostrar_velocitat_microprocessador(data)