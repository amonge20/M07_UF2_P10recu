import pandas as pd
import matplotlib.pyplot as plt

def mostrar_morts_per_mes_per_ciutat():
    # Llegir les dades del fitxer CSV
    dades_covid = pd.read_csv('df_covid19_countries.csv')

    # Escull 10 ciutats
    ciutats = ['New York', 'London', 'Tokyo', 'Paris', 'São Paulo', 'Cape Town', 'Sydney', 'Dubai', 'Mumbai', 'Moscow']

    # Filtrar les dades només per les ciutats especificades
    dades_ciutats = dades_covid[dades_covid['location'].isin(ciutats)]

    # Convertir la columna 'Data' al format de data de Pandas
    dades_ciutats['date'] = pd.to_datetime(dades_ciutats['date'])

    # Agrupar les dades per mes i ciutat i sumar les morts
    dades_agrupades = dades_ciutats.groupby([dades_ciutats['date'].dt.month, 'location']).sum()['total_deaths'].reset_index()

    # Crear una figura per al gràfic
    plt.figure(figsize=(10, 6))

    # Iterar sobre les ciutats i crear una línia per a cada una
    for ciutat in ciutats:
        dades_ciutat = dades_agrupades[dades_agrupades['location'] == ciutat]
        plt.plot(dades_ciutat['date'], dades_ciutat['total_deaths'], label=ciutat)

    # Personalitzar l'aspecte del gràfic
    plt.xlabel('Mes')
    plt.ylabel('Morts totals')
    plt.title('Morts totals per mes per ciutat')
    plt.legend()

    # Mostrar el gràfic
    plt.show()

mostrar_morts_per_mes_per_ciutat()
