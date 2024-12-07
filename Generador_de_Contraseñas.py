import string
import secrets

def generar_contrasena(tipo):
    #Genera una contraseña basada en el tipo especificado.
    password = ''
    longitud = int(input("Ingresa la longitud de la contraseña: "))

    # Diccionario con tipos de caracteres
    diccionario = {
        'letras': string.ascii_letters,
        'numeros': string.digits,
        'caracteres': string.punctuation
    }

    # Crear una contraseña basada en el tipo seleccionado
    if tipo in diccionario:
        password = ''.join(secrets.choice(diccionario[tipo]) for _ in range(longitud))
    elif tipo == 'letras_numeros':
        password = ''.join(secrets.choice(diccionario['letras'] + diccionario['numeros']) for _ in range(longitud))
    elif tipo == 'letras_numeros_caracteres':
        password = ''.join(secrets.choice(diccionario['letras'] + diccionario['numeros'] + diccionario['caracteres']) for _ in range(longitud))

    return password

def main():
    #Función principal que muestra el menú y gestiona las opciones.
    while True:
        print("\nMenú:")
        print("1. Generar contraseña solo de letras")
        print("2. Generar contraseña solo de números")
        print("3. Generar contraseña letras y números")
        print("4. Generar contraseña letras, números y caracteres")
        print("5. Salir")

        opcion = input("Escriba la opción seleccionada: ")

        if opcion == '1':
            contrasena = generar_contrasena('letras')
            print(f"Contraseña generada: {contrasena}")
            input("\n\nPresiona Enter para continuar...")
        
        elif opcion == '2':
            contrasena = generar_contrasena('numeros')
            print(f"Contraseña generada: {contrasena}")
            input("\n\nPresiona Enter para continuar...")

        elif opcion == '3':
            contrasena = generar_contrasena('letras_numeros')
            print(f"Contraseña generada: {contrasena}")
            input("\n\nPresiona Enter para continuar...")

        elif opcion == '4':
            contrasena = generar_contrasena('letras_numeros_caracteres')
            print(f"Contraseña generada: {contrasena}")
            input("\n\nPresiona Enter para continuar...")

        elif opcion == '5':
            confirmacion = input("¿Estás seguro de que deseas salir? (si/no): ").strip().lower()
            if confirmacion == 'si':
                print("Saliendo del programa...")
                break
        
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")

# Ejecución del programa
if __name__ == "__main__":
    main()