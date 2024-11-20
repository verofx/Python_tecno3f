# Ejercicios Prácticos N° 2 - Torres Silvina Verónica
# Ej N° 1 - Realizar un programa que me diga si un numero es par o impar

print('***** Programa que indica si un número es par o impar *****\n')
numero = input('Ingrear un número: \n')
if int(numero) % 2 == 0:
    print(f'El número {numero} es par\n')
elif int(numero) % 2 != 0:
    print(f'El número {numero} es impar\n')
else:
    print('El número ingresado no es un número entero\n')

# Ej N° 2 - Realizar un programa que genere la tabla de multiplicar de un numero ingresado por el usuario (del 1 al 10)

print('***** Programa que genera tabla de multiplicar *****\n')
numero = int(input('Ingresar un número del 1 al 10: '))
if numero >= 1 and numero <= 10:
    print('Tabla del ', numero,'\n')
    for i in range (1,11,1):
        print(numero,' x ', i,  ' = ',numero * i,'\n')

# Ej N° 3 - Realizar un programa que le pida al usuario su nombre y edad y nos diga si es mayor de edad

print('***** Programa que indica si es mayor de edad *****\n')
nombre = input('Ingresar su nombre: \n')
edad = int(input('Ingresar su edad: \n'))
if edad >= 18:
    print('El usuario',nombre,'es mayor de edad\n')
else:
    print('El usuario',nombre,'es menor de edad\n')

# Ej N° 4 - Realizar un programa donde el usuario ingrese una palabra y un numero e imprima por pantalla 
#           la palabra ingresa tantas veces como el numero ingresado

print('***** Programa que imprime una palabra tantas veces como un número *****\n')
palabra = input('Ingresar una palabra: \n')
numero = int(input('Ingresar un número: \n'))
for i in range(0,numero,1):
    print(palabra)  # Imprime la palabra tantas veces como el número ingresado

# Ej N° 5 - Realizar un programa que sume los números ingresados por el usuario hasta que seingrese un 0.
#           Al finalizar nos debe mostrar la suma por pantalla

print('***** Programa que suma los numeros ingresados corta en 0 *****\n')
numero = int(input('Ingresar un número (Con "0" corta la suma)):'))
suma = 0
while numero != 0:
    suma = suma + numero
    numero = int(input('Ingresar un número (Con "0" corta la suma):'))
print('\n La sumatoria total de los números ingresados es: ', suma)