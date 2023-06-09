import pandas as pd
import matplotlib.pyplot as plt


# Función para mostrar la cantidad total de casos por mes por país hola
def casos_totals_per_mes_per_pais(dades, paisos):
    dades_filt = dades[dades['location'].isin(paisos)]
    dades_agregades = dades_filt.groupby(['Month', 'location'])['total_cases'].sum()
    return dades_agregades


# Función para mostrar la cantidad total de muertes por mes por ciudad
def morts_totals_per_mes_per_ciutat(dades, ciutats):
    dades_filt = dades[dades['City'].isin(ciutats)]
    dades_agregades = dades_filt.groupby(['Month', 'City'])['total_deaths'].sum()
    return dades_agregades


# Función para mostrar el número de muertes por mes por país
def morts_per_mes_per_pais(dades, paisos):
    dades_filt = dades[dades['location'].isin(paisos)]
    dades_agregades = dades_filt.groupby(['Month', 'location'])['total_deaths'].sum()
    return dades_agregades


# Función principal (main)
def main():
    # Leer los datos del archivo CSV
    dades = pd.read_csv('df_covid19_countries.csv')

    # Definir los países y ciudades
    paisos = ['Spain', 'Italy', 'Germany', 'France', 'United Kingdom', 'United States', 'Canada', 'China', 'Australia', 'Brazil']
    ciutats = ['New York', 'Los Angeles', 'London', 'Paris', 'Madrid', 'Rome', 'Berlin', 'Toronto', 'Sydney', 'Rio de Janeiro']

    # Obtener los datos agregados
    casos_por_mes_pais = casos_totals_per_mes_per_pais(dades, paisos)
    morts_por_mes_ciutat = morts_totals_per_mes_per_ciutat(dades, ciutats)
    morts_por_mes_pais = morts_per_mes_per_pais(dades, paisos)

    # Gráficas con Matplotlib
    plt.figure(figsize=(10, 6))

    # Gráfica 1: Casos totales por mes por país
    for pais in paisos:
        casos_pais = casos_por_mes_pais.loc[:, pais]
        meses = casos_por_mes_pais.index.get_level_values(0)
        plt.plot(meses, casos_pais, label=pais)

    plt.xlabel('Mes')
    plt.ylabel('Casos Totales')
    plt.title('Casos Totales por Mes y País')
    plt.legend()
    plt.show()

    # Gráfica 2: Muertes totales por mes por ciudad
    plt.figure(figsize=(10, 6))
    for ciudad in ciutats:
        muertes_ciudad = morts_por_mes_ciutat.loc[:, ciudad]
        meses = morts_por_mes_ciutat.index.get_level_values(0)
        plt.plot(meses, muertes_ciudad, label=ciudad)

    plt.xlabel('Mes')
    plt.ylabel('Muertes Totales')
    plt.title('Muertes Totales por Mes y Ciudad')
    plt.legend()
    plt.show()

    # Gráfica 3: Número de muertes por mes por país
    plt.figure(figsize=(10, 6))
    for pais in paisos:
        muertes_pais = morts_por_mes_pais.loc[:, pais]
        meses = morts_por_mes_pais.index.get_level_values(0)
        plt.plot(meses, muertes_pais, label=pais)

    plt.xlabel('Mes')
    plt.ylabel('Número de Muertes')
    plt.title('Número de Muertes por Mes y País')
    plt.legend()
    plt.show()

# Llamar a la función principal
main()