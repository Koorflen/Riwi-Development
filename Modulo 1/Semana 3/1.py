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
        case 2:
            eliminar_animal()
        case 3:
            ver_animales_ingresados()
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
        Year=int(input("Ingresa la edad del animal:\n"))
        Sick=str(input("El animal esta enfermo?(Si/No)\n")).lower()
        
def eliminar_animal():
    print("Yes")

def ver_animales_ingresados():
    print("Yes")
    
    
menu()