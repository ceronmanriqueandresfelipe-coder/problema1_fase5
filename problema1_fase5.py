# =============================================================================
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA (UNAD)
# Escuela de Ciencias Básicas, Tecnología e Ingeniería (ECBTI)
# Programa: Ingeniería de Sistemas
# Curso: Fundamentos de Programación (Código: 213022)
# Fase 5 - Evaluación Final POA
#
# Estudiante: Andres Felipe Ceron Manrique
# Correo: ceronmanriqueandresfelipe@gmail.com
# Problema Seleccionado: Problema 1
# =============================================================================

# Matriz de datos iniciales (Mínimo 5 filas requeridas)
sesiones = [
    ["C001", 250, 12],  # Alto (> 180s y > 8 clics)
    ["C002", 45, 2],    # Bajo (< 60s)
    ["C003", 120, 5],   # Medio (Caso estándar)
    ["C004", 300, 15],  # Alto (> 180s y > 8 clics)
    ["C005", 70, 1]     # Bajo (< 3 clics)
]

# Módulo (función) para clasificar el compromiso
def clasificar_compromiso(duracion, clics):
    """
    Evalúa la duración y los clics para retornar el nivel de compromiso.
    """
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

def main():
    # Título del informe
    print("==================================================================")
    print("          INFORME DE EVALUACIÓN DE COMPROMISO DE SESIONES         ")
    print("==================================================================\n")

    # Cabeceras del informe alineadas
    print(f"{'ID CLIENTE':<15}{'DURACIÓN (s)':<18}{'EVENTOS CLICS':<18}{'CLASIFICACIÓN':<15}")
    print("-" * 66)

    # Recorrer la matriz de forma estructurada
    for sesion in sesiones:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]

        # Llamado de la función modular
        clasificacion = clasificar_compromiso(duracion, clics)

        # Mostrar resultados en formato tabular
        print(f"{id_cliente:<15}{duracion:<18}{clics:<18}{clasificacion:<15}")

    print("-" * 66)
    print("Fin del informe de auditoría.")
    print("==================================================================")
    
    input("\nPresione ENTER para salir...")

if __name__ == "__main__":
    main()
