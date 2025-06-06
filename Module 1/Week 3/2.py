contactos = {}

def menu():
    decision_menu = 0
    while decision_menu not in (1, 2, 3, 4):
        print("--------> Gestion de Contactos <--------")
        print("¿Qué deseas hacer?\n"
              "1. Agregar nuevo contacto\n"
              "2. Mostrar todos los contactos\n"
              "3. Buscar contacto por nombre\n"
              "4. Salir")
        decision_menu = int(input())
        if decision_menu not in (1, 2, 3, 4):
            print("Ingresa el valor numérico de tu decisión")
    
    match decision_menu:
        case 1:
            agregar_contacto()
        case 2:
            mostrar_contactos()
        case 3:
            buscar_contacto()
        case 4:
            print("Gracias por usar nuestros servicios")

def agregar_contacto():
    nombre = input("Ingresa el nombre del contacto: ")
    telefono = input("Ingresa el número de teléfono: ")
    contactos[nombre] = telefono
    print(f"Contacto {nombre} agregado con éxito.")

def mostrar_contactos():
    if contactos:
        print("----> Contactos almacenados <----")
        for nombre, telefono in contactos.items():
            print(f"Nombre: {nombre}, Teléfono: {telefono}")
    else:
        print("No hay contactos almacenados.")

def buscar_contacto():
    nombre = input("Ingresa el nombre del contacto que deseas buscar: ")
    if nombre in contactos:
        print(f"Contacto encontrado: Nombre: {nombre}, Teléfono: {contactos[nombre]}")
    else:
        print("Contacto no encontrado.")

menu()
