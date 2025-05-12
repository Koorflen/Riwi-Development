contacts = []

def menu():
    decision_menu = 0
    while decision_menu not in (1, 2, 3, 4, 5, 6):
        print("-------->Agenda de Contactos<--------")
        print("¿Qué deseas hacer?\n"
              "1. Agregar un nuevo contacto\n"
              "2. Buscar un contacto\n"
              "3. Mostrar todos los contactos\n"
              "4. Modificar un contacto\n"
              "5. Eliminar un contacto\n"
              "6. Salir")
        
        decision_menu = input()
        
        # Validar si la entrada es un número y está dentro del rango
        if not decision_menu.isdigit() or not (1 <= int(decision_menu) <= 6):
            print("Ingresa un valor numérico válido entre 1 y 6.")
            decision_menu = 0  # Reset para volver a preguntar
        else:
            decision_menu = int(decision_menu)

    match decision_menu:
        case 1:
            agregar_contacto()
            decision_menu=0
            menu()
        case 2:
            buscar_contacto()
            decision_menu=0
            menu()
        case 3:
            mostrar_contactos()
            decision_menu=0
            menu()
        case 4:
            modificar_contacto()
            decision_menu=0
            menu()
        case 5:
            eliminar_contacto()
            decision_menu=0
            menu()
        case 6:
            print("Gracias por usar la Agenda de Contactos")

def agregar_contacto():
    print("----> Agregar nuevo contacto <----")
    nombre = input("Ingresa el nombre del contacto: ").strip()
    while len(nombre) == 0:
        print("El nombre no puede estar vacío")
        nombre = input("Ingresa el nombre del contacto: ").strip()

    celular = input("Ingresa el número de celular del contacto: ").strip()
    while len(celular) == 0 or not celular.isdigit() or len(celular) != 10:
        print("El número de celular debe ser de 10 dígitos numéricos.")
        celular = input("Ingresa el número de celular del contacto: ").strip()

    estado_civil = input("Ingresa el estado civil del contacto (Soltero, Casado, etc.): ").strip()
    while len(estado_civil) == 0:
        print("El estado civil no puede estar vacío")
        estado_civil = input("Ingresa el estado civil del contacto: ").strip()

    genero = input("Ingresa el género del contacto (Masculino/Femenino): ").strip().lower()
    while genero not in ['masculino', 'femenino']:
        print("El género debe ser 'Masculino' o 'Femenino'.")
        genero = input("Ingresa el género del contacto (Masculino/Femenino): ").strip().lower()

    contacto = {
        "nombre": nombre,
        "celular": celular,
        "estado_civil": estado_civil,
        "genero": genero
    }

    contacts.append(contacto)
    print(f"Contacto {nombre} agregado exitosamente!")

def buscar_contacto():
    print("----> Buscar contacto <----")
    busqueda = input("¿Qué contacto deseas buscar? Ingresa nombre o celular: ").strip()

    encontrado = False
    for contacto in contacts:
        if contacto["nombre"].lower() == busqueda.lower() or contacto["celular"] == busqueda:
            print(f"Nombre: {contacto['nombre']}\n"
                  f"Celular: {contacto['celular']}\n"
                  f"Estado civil: {contacto['estado_civil']}\n"
                  f"Género: {contacto['genero'].capitalize()}")
            encontrado = True
            break

    if not encontrado:
        print("No se encontró el contacto.")

def mostrar_contactos():
    print("----> Mostrar todos los contactos <----")
    if not contacts:
        print("No hay contactos registrados.")
    else:
        for i, contacto in enumerate(contacts, start=1):
            print(f"{i}. Nombre: {contacto['nombre']}\n"
                  f"   Celular: {contacto['celular']}\n"
                  f"   Estado civil: {contacto['estado_civil']}\n"
                  f"   Género: {contacto['genero'].capitalize()}")

def modificar_contacto():
    print("----> Modificar un contacto <----")
    if not contacts:
        print("No hay contactos registrados.")
        return

    mostrar_contactos()
    indice = -1
    while indice < 1 or indice > len(contacts):
        indice = input(f"Selecciona el número del contacto que deseas modificar (1-{len(contacts)}): ").strip()
        if not indice.isdigit() or not (1 <= int(indice) <= len(contacts)):
            print("Por favor, ingresa un número válido dentro del rango de contactos.")
        else:
            indice = int(indice)

    contacto = contacts[indice - 1]
    print(f"Modificando el contacto: {contacto['nombre']}")
    
    nombre = input(f"Nuevo nombre (actual: {contacto['nombre']}): ").strip()
    celular = input(f"Nuevo celular (actual: {contacto['celular']}): ").strip()
    estado_civil = input(f"Nuevo estado civil (actual: {contacto['estado_civil']}): ").strip()
    genero = input(f"Nuevo género (actual: {contacto['genero']}): ").strip().lower()

    while genero not in ['masculino', 'femenino']:
        print("El género debe ser 'Masculino' o 'Femenino'.")
        genero = input(f"Nuevo género (actual: {contacto['genero']}): ").strip().lower()

    contacto["nombre"] = nombre if len(nombre) > 0 else contacto["nombre"]
    contacto["celular"] = celular if len(celular) > 0 else contacto["celular"]
    contacto["estado_civil"] = estado_civil if len(estado_civil) > 0 else contacto["estado_civil"]
    contacto["genero"] = genero if len(genero) > 0 else contacto["genero"]

    print(f"Contacto {contacto['nombre']} modificado exitosamente!")

def eliminar_contacto():
    print("----> Eliminar un contacto <----")
    if not contacts:
        print("No hay contactos registrados.")
        return

    mostrar_contactos()
    indice = -1
    while indice < 1 or indice > len(contacts):
        indice = input(f"Selecciona el número del contacto que deseas eliminar (1-{len(contacts)}): ").strip()
        if not indice.isdigit() or not (1 <= int(indice) <= len(contacts)):
            print("Por favor, ingresa un número válido dentro del rango de contactos.")
        else:
            indice = int(indice)

    contacto = contacts.pop(indice - 1)
    print(f"Contacto {contacto['nombre']} eliminado exitosamente!")

# Iniciar el programa
menu()
