import pandas as pd
import matplotlib.pyplot as plt

def mostrar_casos_por_mes():
    # Leer el archivo CSV utilizando Pandas
    df = pd.read_csv('df_covid19_countries.csv')

    # Seleccionar 10 países diferentes
    paises = ['Spain', 'Italy', 'France', 'Germany', 'United Kingdom', 'United States', 'Brazil', 'Argentina', 'India', 'Russia']
    df_paises = df[df['location'].isin(paises)]

    # Convertir la columna 'date' al tipo de dato datetime
    df_paises['date'] = pd.to_datetime(df_paises['date'])

    # Agrupar los datos por país y mes, y sumar los casos
    df_mensual = df_paises.groupby(['location', pd.Grouper(key='date', freq='M')])['total_cases'].sum().reset_index()

    # Crear una figura de Matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))

    # Iterar sobre los países y dibujar una línea para cada país
    for pais in paises:
        datos_pais = df_mensual[df_mensual['location'] == pais]
        ax.plot(datos_pais['date'], datos_pais['total_cases'], label=pais)

    # Personalizar los ejes y la leyenda
    ax.set_xlabel('Mes')
    ax.set_ylabel('Cantidad de casos')
    ax.set_title('Cantidad de casos de COVID-19 por mes')
    ax.legend()

    # Mostrar el gráfico
    plt.show()

mostrar_casos_por_mes()
