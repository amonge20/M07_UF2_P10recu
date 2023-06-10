from mostrar_casos_por_mes import mostrar_casos_por_mes
from mostrar_morts_per_mes_per_ciutat import mostrar_morts_per_mes_per_ciutat
from mostrar_morts_per_mes import mostrar_morts_per_mes

# Función principal (main)
def main():
    # Obtener los datos agregados
    mostrar_casos_por_mes()
    mostrar_morts_per_mes_per_ciutat()
    mostrar_morts_per_mes()

# Llamar a la función principal
main()