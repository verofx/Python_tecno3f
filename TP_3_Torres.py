# TP N° 3 - Torres Silvina Verónica
# Ejercicio 1 - Crea una funcion que calcule el promedio de N notas
def promedio_notas(nota1, nota2, nota3, nota4, nota5)
    return (nota1 + nota2 + nota3 + nota4 + nota5) /

# Ejercicio 2 - Cree una funcion que determine si un color es primario o no, 
# se debe imprimir porpantalla la leyenda “el color X es primero “ o “el color X no es primario”
def es_primario(color)
    if color == "rojo" or color == "azul" or color == "amar
    print("el color " + color + " es primario")
    else:
print("el color " + color + " no es primario")

# Ejercicio 3 - Cree una funcion que determine que numero de una serie de N numeros es mayor
def mayor_numero(num1, num2, num3, num4, num5):
    return max(num1, num2, num3, num4, num5)


# Ejercicio 4 - Cree una funcion que dibuje un rectangulo de X filas y X columnas
# determinadas por el usuario
def dibuja_rectangulo(filas, columnas):
    for i in range(filas):
        for j in range(columnas):
            print("*", end=" ")
            print()


# Ejercicio 5 - Cree una funcion que calcule el Factorial de un numero entero positivo

