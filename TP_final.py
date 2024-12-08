import random
import pickle
import os

# Diccionario para almacenar los tickets
tickets = {}

# Cargar tickets desde un archivo si existe
def cargar_tickets():
    if os.path.exists('tickets.pkl'):
        with open('tickets.pkl', 'rb') as file:
            return pickle.load(file)
    return {}

# Guardar tickets en un archivo
def guardar_tickets():
    with open('tickets.pkl', 'wb') as file:
        pickle.dump(tickets, file)

def alta_ticket():
    #Función para dar de alta un nuevo ticket.
    nombre = input("\nIngresa tu nombre: ")
    sector = input("\nIngresa el sector: ")
    asunto = input("\nIngresa el asunto: ")
    problema = input("\nDescribe el problema: ")

    # Generar un número de ticket aleatorio entre 1000 y 9999
    numero_ticket = random.randint(1000, 9999)

    # Almacenar el ticket en el diccionario
    tickets[numero_ticket] = {
        'nombre': nombre,
        'sector': sector,
        'asunto': asunto,
        'problema': problema
    }

    # Mostrar el ticket al usuario
    print("***************************************************")
    print("***************** TICKET GENERADO *****************")
    print("\n______________________________________________________________________")
    print(f"\n\nNúmero de Ticket: {numero_ticket}             Nombre: {nombre}")
    print(f"\nSector: {sector}           Asunto: {asunto}\n\nProblema: {problema}")
    print("\n______________________________________________________________________")
    print("\n¡Recuerda tu número de ticket!")
    input("\nPresion cualquier tecla para continuar")

def leer_ticket():
    #Función para leer un ticket existente.
    numero_ticket = int(input("\nIngresa el número de ticket que deseas leer:"))
    
    if numero_ticket in tickets:
        ticket = tickets[numero_ticket]
        print("\n\n***************************************************")
        print("***************** TICKET ENCONTRADO *****************")
        print("\n______________________________________________________________________")
        print(f"\n\nNúmero de Ticket: {numero_ticket}        Nombre: {ticket['nombre']}")
        print(f"\nSector: {ticket['sector']}              Asunto: {ticket['asunto']}\n\nProblema: {ticket['problema']}")
        print("\n______________________________________________________________________")
    else:
        print("No se encontró ningún ticket con ese número.")
        input("\nPresion cualquier tecla para continuar")

def main():
    #Función principal que muestra el menú y opciones.
    global tickets
    tickets = cargar_tickets()  # Cargar tickets al iniciar

    while True:
        print("\n\n********************************************************************")
        print("***************** BIENVENIDO AL SISTEMA DE TICKETS *****************")
        print("\nMenú:\n")
        print("1. Alta ticket")
        print("2. Leer ticket")
        print("3. Salir")
        
        opcion = input("\nSelecciona una opción (1-3): ")

        if opcion == '1':
            alta_ticket()
            continuar = input("\n¿Deseas crear otro ticket? (si/no):").strip().lower()
            if continuar != 'si':
                continue
        
        elif opcion == '2':
            leer_ticket()
            continuar = input("\n¿Deseas leer otro ticket? (si/no):").strip().lower()
            if continuar != 'si':
                continue
        
        elif opcion == '3':
            confirmacion = input("\n¿Estás seguro de que deseas salir? (si/no):").strip().lower()
            if confirmacion == 'si':
                guardar_tickets()  # Guardar tickets antes de salir
                print("\nSaliendo del programa...")
                break
        
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 3.")

# Ejecución del programa
if __name__ == "__main__":
    main()