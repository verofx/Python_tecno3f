# Torres Silvina Verónica

# Ejercicios de Práctica
# N°1 Realiza un programa que le pida al usuario su nombre y lo muestre en mayúscula
print('*********** Nombre en Maypusculas ***********\n')
nombre = input ('Por favor ingrese su nombre: ')

print('Tu nombre en Mayúsculas es: ', nombre.upper())
print()

# N2 Realizar un programa que le pida al usuario un numero y le sume 5 ,
#  el resultado debemostrarce por pantalla

print('*********** Número + 5 ***********\n')
numero = int(input('Ingrese un número: '))
print('El número ingresado más 5 es: ', numero + 5)
print()
#Realizar un programa que le pida al usuario su nombre y apellido , 
# Mostrarlos en un mensaje de bienvenida por la pantalla

print('*********** Bienvenida ***********\n')
nombre = input ('Por favor ingrese su nombre: ')
apellido = input ('Por favor ingrese su apellido: ')
print('Bienvenido/a: ', nombre, apellido)  
print()

# Ingresar 5 numeros y calcular su promedio , el resultado mostrarlo por pantalla

print('*********** Promedio de 5 números ***********\n')
numero1 = float(input('Ingrese el número 1: ')) 
numero2 = float(input('Ingrese el número 2: '))
numero3 = float(input('Ingrese el número 3: '))
numero4 = float(input('Ingrese el número 4: '))
numero5 = float(input('Ingrese el número 5: '))
print()
promedio = (numero1 + numero2 + numero3 + numero4 + numero5)/5
print ('El promedio de los 5 números ingresados es: ', promedio)
print()

# Realizar un programa que muestre cualquier frase ingresada por el usuario enminuscula

print('*********** Frase en minúscula ***********\n')
frase = input ('Por favor Ingrese una frase: ')
print('Su frase en minúscula es: ', frase.lower())