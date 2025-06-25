Names=[]
Years=[]
Sicks=[]

def menu():
    
    decision_menu=0
    while decision_menu not in (1,2,3,4):
        print("-------->Riwi's Pets<--------")
        print("Que deseas hacer?\n"
              "1. Agregar animal\n"
              "2. Eliminar animal\n"
              "3. Ver animales ingresados\n"
              "4. Salir")
        decision_menu=int(input())
        if decision_menu not in (1,2,3,4):
            print("Ingresa el valor numerico de tu decision")
    
    match decision_menu:
        case 1:
            agregar_animal()
            menu()
        case 2:
            eliminar_animal()
            menu()
        case 3:
            ver_animales_ingresados()
            menu()
        case 4:
            print("Muchas gracias por usar nuestros servicios")

def agregar_animal():
    cuantos_animales=0
    while cuantos_animales<1:
        try:
            cuantos_animales=int(input("Cuantos animales deseas agregar?\n"))
            if cuantos_animales<1:
                print("Ingresa uno o mas animales")
        except ValueError:
            print("Ingresa un valor numerico mayor o igual a 1")
    
    for indice in range(cuantos_animales):
        Name=str(input("Ingresa el nombre del animal a ingresar:\n"))
        
        Year=-1
        while Year<0:
            try:
                Year=int(input("Ingresa la edad del animal:\n"))
                if Year<0:
                    print("Edad invalida")
            except ValueError:
                print("Edad invalida")
        
        Sick=""
        while Sick not in ("si","no"):
            Sick=str(input("El animal esta enfermo?(Si/No)\n")).lower()
            if Sick not in ("si","no"):
                print("Respuesta invalida. Escribe si o no")

        Names.append(Name)
        Years.append(Year)
        Sicks.append(Sick)

def eliminar_animal():
    eliminar=str(input("Escribe el nombre del animal que deseas eliminar:\n"))
    if eliminar in Names:
        posicion=Names.index(eliminar)
        del Names[posicion]
        del Years[posicion]
        del Sicks[posicion]
        print("Animal eliminado exitosamente")
    else:
        print("Animal no encontrado")

def ver_animales_ingresados():
    if len(Names)==0:
        print("No hay animales registrados")
    else:
        print("Animales registrados:")
        for i in range(len(Names)):
            print(f"Nombre: {Names[i]} - Edad: {Years[i]} - Enfermo: {Sicks[i]}")

menu()
