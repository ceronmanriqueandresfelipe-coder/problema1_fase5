# ---------------------------------------------------
# FASE 5 - EVALUACIÓN FINAL POA
# Problema 1
# Fundamentos de Programación
# ---------------------------------------------------

# Matriz de datos:
# [ID Cliente, Duración en segundos, Número de clics]

sesiones = [
    ["C001", 250, 12],
    ["C002", 45, 2],
    ["C003", 120, 5],
    ["C004", 300, 15],
    ["C005", 70, 1]
]

# Función para clasificar el compromiso
def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"


# Título del informe
print("========================================")
print(" INFORME DE CLASIFICACIÓN DE SESIONES ")
print("========================================")

# Recorrer la matriz
for sesion in sesiones:

    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    # Llamado de la función
    clasificacion = clasificar_compromiso(duracion, clics)

    # Mostrar resultados
    print("----------------------------------------")
    print("ID Cliente:", id_cliente)
    print("Duración:", duracion, "segundos")
    print("Clics:", clics)
    print("Clasificación:", clasificacion)

print("========================================")
print("Fin del informe")

input("Presione ENTER para salir...")