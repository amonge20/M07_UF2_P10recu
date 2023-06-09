import pandas as pd
import matplotlib.pyplot as plt

def mostrar_poblacio_per_ciutat():
    data = pd.read_csv('List of cities proper by population density11.csv')
    top_10_cities = data.head(10)

    # Filtrar valores no nulos
    top_10_cities = top_10_cities[pd.notnull(top_10_cities['Population'])]

    # Eliminar comas y redondear los valores a enteros
    top_10_cities["Population"] = top_10_cities['Population'].str.replace(',', '').astype(float).round().astype(int)

    plt.figure(figsize=(8, 8))
    plt.pie(top_10_cities['Population'], labels=top_10_cities['City'], autopct='%1.1f%%')
    plt.title("Distribución de población por ciudad")
    plt.legend()
    plt.show()

mostrar_poblacio_per_ciutat()