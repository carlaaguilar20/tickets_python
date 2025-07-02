
import random

# Diccionario para almacenar los tickets
tickets = {}

def generar_numero_ticket():
    return random.randint(1000, 9999)

def alta_ticket():
    while True:
        print("\n--- Alta de Ticket ---")
        nombre = input("Nombre: ")
        sector = input("Sector: ")
        asunto = input("Asunto: ")
        problema = input("Problema: ")

        numero_ticket = generar_numero_ticket()
        while numero_ticket in tickets:
            numero_ticket = generar_numero_ticket()

        tickets[numero_ticket] = {
            "Nombre": nombre,
            "Sector": sector,
            "Asunto": asunto,
            "Problema": problema
        }

        print(f"\nTicket generado exitosamente. Número de ticket: {numero_ticket}")
        print("Por favor, recuerde este número para futuras consultas.")

        otra = input("\n¿Desea crear otro ticket? (s/n): ").strip().lower()
        if otra != 's':
            break

def leer_ticket():
    while True:
        print("\n--- Lectura de Ticket ---")
        try:
            numero = int(input("Ingrese el número de ticket: "))
            if numero in tickets:
                ticket = tickets[numero]
                print(f"\n--- Ticket N° {numero} ---")
                for clave, valor in ticket.items():
                    print(f"{clave}: {valor}")
            else:
                print("❌ No se encontró un ticket con ese número.")
        except ValueError:
            print("⚠️ Por favor ingrese un número válido.")

        otra = input("\n¿Desea leer otro ticket? (s/n): ").strip().lower()
        if otra != 's':
            break

def confirmar_salida():
    confirmacion = input("¿Está seguro que desea salir? (s/n): ").strip().lower()
    return confirmacion == 's'

def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Alta Ticket")
        print("2. Leer Ticket")
        print("3. Salir")

        opcion = input("Seleccione una opción (1-3): ").strip()

        if opcion == '1':
            alta_ticket()
        elif opcion == '2':
            leer_ticket()
        elif opcion == '3':
            if confirmar_salida():
                print("¡Gracias por usar el sistema de tickets! 👋")
                break
        else:
            print("⚠️ Opción inválida. Intente nuevamente.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu()