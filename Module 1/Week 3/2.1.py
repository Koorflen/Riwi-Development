estudiantes = {}

def menu():
    decision_menu = 0
    while decision_menu not in (1, 2, 3, 4, 5):
        print("--------> Gestion de Estudiantes <--------")
        print("¿Qué deseas hacer?\n"
              "1. Agregar nuevo estudiante\n"
              "2. Modificar calificación de estudiante\n"
              "3. Mostrar información de estudiantes\n"
              "4. Eliminar estudiante\n"
              "5. Salir")
        try:
            decision_menu = int(input())
            if decision_menu not in (1, 2, 3, 4, 5):
                print("Ingresa un valor numérico válido")
        except ValueError:
            print("Por favor, ingresa un valor numérico")

    match decision_menu:
        case 1:
            agregar_estudiante()
            decision_menu=0
            menu()
        case 2:
            modificar_calificacion()
            decision_menu=0
            menu()
        case 3:
            mostrar_estudiantes()
            decision_menu=0
            menu()
        case 4:
            eliminar_estudiante()
            decision_menu=0
            menu()
        case 5:
            print("Gracias por usar nuestros servicios")

def agregar_estudiante():
    nombre = input("Ingresa el nombre del estudiante: ")
    edad = -1
    while edad < 0:
        try:
            edad = int(input("Ingresa la edad del estudiante: "))
            if edad < 0:
                print("Edad no puede ser negativa.")
        except ValueError:
            print("Por favor, ingresa una edad válida.")

    calificacion = -1
    while calificacion < 0 or calificacion > 10:
        try:
            calificacion = float(input("Ingresa la calificación del estudiante (de 0 a 10): "))
            if calificacion < 0 or calificacion > 10:
                print("La calificación debe estar entre 0 y 10.")
        except ValueError:
            print("Por favor, ingresa una calificación válida.")
    
    estudiantes[nombre] = {'edad': edad, 'calificacion': calificacion}
    print(f"Estudiante {nombre} agregado con éxito.")

def modificar_calificacion():
    nombre = input("Ingresa el nombre del estudiante cuya calificación deseas modificar: ")
    if nombre in estudiantes:
        calificacion = -1
        while calificacion < 0 or calificacion > 10:
            try:
                calificacion = float(input(f"Ingresa la nueva calificación para {nombre} (de 0 a 10): "))
                if calificacion < 0 or calificacion > 10:
                    print("La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Por favor, ingresa una calificación válida.")
        
        estudiantes[nombre]['calificacion'] = calificacion
        print(f"Calificación de {nombre} modificada con éxito.")
    else:
        print("Estudiante no encontrado.")

def mostrar_estudiantes():
    if estudiantes:
        print("----> Estudiantes registrados <----")
        for nombre, datos in estudiantes.items():
            print(f"Nombre: {nombre}, Edad: {datos['edad']}, Calificación: {datos['calificacion']}")
    else:
        print("No hay estudiantes registrados.")

def eliminar_estudiante():
    nombre = input("Ingresa el nombre del estudiante que deseas eliminar: ")
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"Estudiante {nombre} eliminado con éxito.")
    else:
        print("Estudiante no encontrado.")

menu()
