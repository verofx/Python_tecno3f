# TP N° 3 - Torres Silvina Verónica
# Ejercicio 1 - Crea una funcion que calcule el promedio de N notas

def calcular_promedio(notas):
    if notas:  # Verificar si la lista no está vacía
        promedio = sum(notas) / len(notas)
        print(f"El promedio de las notas es: {promedio:.2f}") # :.2f especifica que se redondea en dos dígitos el decimal
    else:
        print("No se ingresaron notas.")

def main_promedio(): # función principal para ingresar notas
    print('\n******** PROGRAMA PARA CALCULAR EL PROMEDIO DE N NOTAS ********\n')
    notas = [] #lista vacía para guardar las notas
    
    while True:
        entrada = input("Ingresa una nota (cualquier letra para terminar): ")
        if entrada.isalpha(): # si la entrada es una letra, se sale del bucle
            break
        try:
            nota = float(entrada) # si la entrada es un número, se agrega a la lista
            notas.append(nota)
        except ValueError:
            print("Por favor, ingresa un número válido o cualquier letra para terminar.")
    
    # Calcular y mostrar el promedio
    calcular_promedio(notas)

# Ejecución del programa

main_promedio()


# Ejercicio 2 - Cree una funcion que determine si un color es primario o no, 
# se debe imprimir por pantalla la leyenda “el color X es primario “ o “el color X no es primario”

def es_color_primario(color):
    colores_primarios = ['rojo', 'azul', 'amarillo']
    if color.lower() in colores_primarios:
        print(f"El color {color} es primario.")
    else:
        print(f"El color {color} no es primario.")

while True:
        print('\n******** PROGRAMA PARA DETERMINAR SI UN COLOR ES PRIMARIO O NO ********\n')
        color_ingresado = input("Ingresa un color (0 para terminar): ")
        if color_ingresado == "0":
            break
        es_color_primario(color_ingresado) # se llama la función con el color ingresado

# Ejercicio 3 - Cree una funcion que determine que numero de una serie de N numeros es mayor

def numero_mayor(numeros):
    if len(numeros) > 1: # Verificar si hay más de un número
        maximo = max(numeros) # encontrar el número mayor con el método max()
        print(f"El número mayor es: {maximo}")
    else:
        print("No se ingresaron suficientes números.")

def main_num(): # función principal para ingresar números
    print('\n******** PROGRAMA PARA CALCULAR EL NÚMERO MÁS GRANDE DE N NUMEROS ********\n')
    numeros = [] #lista vacía para guardar los números ingresados
              
    while True:
        entrada = input("Ingresa un número (para salir presiona cualquier letra): ")
        if entrada.isalpha(): # si la entrada es una letra, se sale del bucle
            break
        try:
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, ingresa un número válido o cualquier letra para terminar.") 
    numero_mayor(numeros)

main_num()

# Ejercicio 4 - Cree una funcion que dibuje un rectangulo de X filas y X columnas
# determinadas por el usuario

def dibujar_rectangulo(filas, columnas):
    #Dibuja un rectángulo de asteriscos con el número de filas y columnas especificadas.
    for _ in range(filas):
        print('*' * columnas)

def main_rec():
    #Función principal que solicita al usuario las dimensiones del rectángulo
    print('\n******** PROGRAMA PARA DIBUJAR RETÁNGULOS ********\n')
    while True:
        try:
            filas = int(input("Ingresa el número de filas (0 para terminar): "))
            if filas == 0:
                print("Fin del programa.")
                break  # Salir del bucle si el usuario ingresa 0
            
            columnas = int(input("Ingresa el número de columnas: "))
            if columnas <= 0:
                print("El número de columnas debe ser mayor que 0.")
                continue
            
            # Dibujar el rectángulo
            dibujar_rectangulo(filas, columnas)
        
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

# Ejecución del programa
main_rec()

# Ejercicio 5 - Cree una funcion que calcule el Factorial de un numero entero positivo
def calcular_factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

def main_factorial():
    print('\n******** PROGRAMA PARA CALCULAR FACTORIALES ********\n')
    while True:
        try:
            numero = int(input("Ingresa un número entero positivo (o -1 para terminar): "))
            if numero == -1:
                print("Fin del programa.")
                break  # Salir del bucle si el usuario ingresa -1
            
            if numero < 0:
                print("Por favor, ingresa un número entero positivo.")
                continue
            
            # Calcular y mostrar el factorial
            resultado = calcular_factorial(numero)
            print(f"El factorial de {numero} es: {resultado}")
        
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

# Ejecución del programa
main_factorial()

