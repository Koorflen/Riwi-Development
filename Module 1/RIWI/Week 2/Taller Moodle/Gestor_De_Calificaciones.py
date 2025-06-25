### MENU PRINCIPAL ###

decision_menu_principal=0
def menu():
    global decision_menu_principal
    while decision_menu_principal not in (1, 2, 3):
        print("----------Riwi Ratings----------")
        print("Bienvenido a Riwi Ratings\n¿Que deseas hacer?")
        print("1. Ingresar una calificacion\n2. Ingresar varias calificaciones\n3. Salir")
        try:
            decision_menu_principal=int(input())
            if decision_menu_principal not in (1, 2, 3):
                print("Ingresa una opcion valida\n")
        except ValueError:
            print("Ingresa el valor numerico de tu decision\n")

menu()
   
###SUB-MENUS###

match decision_menu_principal:
    
    ##APROBO O REPROBO##
    
    case 1:
        calificacion=-1
        while not 0<=calificacion<=100:
            try:
                calificacion=int(input("Ingresa tu calificacion (0-100)\n"))
                if not 0<=calificacion<=100:
                    print("Ingresa una calificacion entre 0 y 100\n")
            except ValueError:
                print("Ingresa un valor numerico entero\n")
                calificacion=-1
        if calificacion >= 60:
            print("¡Aprobaste!")
        else:
            print("No aprobaste. Sigue intentandolo")
        decision_menu_principal=0
        menu()
    ##INGRESO DE VARIAS CALIFICACIONES##
    
    case 2:
        calificaciones=[]
        while True:
            try:
                notas=input("Ingresa tus calificaciones separadas por comas (Ej: 80,90,100)\n")
                notas=notas.split(",")
                for i in notas:
                    nota=int(i.strip())
                    if 0<=nota<=100:
                        calificaciones.append(nota)
                    else:
                        raise ValueError
                break
            except ValueError:
                print("Todas las calificaciones deben ser numeros enteros entre 0 y 100\n")
                
        print("Tus calificaciones ingresadas son:")
        for i, nota in enumerate(calificaciones, start=1):
            print(f"{i}. {nota}")
        
        #MENU LISTAS#
        
        decision_menu_lista=0
        def sub_menu():
            while decision_menu_lista not in (1, 2, 3):
                global decision_menu_lista
                print("Que deseas hacer con tus calificaciones?")
                print("1. Calcular promedio\n2. Contar calificaciones mayores\n3. Verificar y contar calificaciones especificas")
                try:
                    decision_menu_lista=int(input())
                    if decision_menu_lista not in (1, 2, 3):
                        print("Ingresa una opcion valida\n")
                except ValueError:
                    print("Ingresa el valor numerico de tu decision\n")
        sub_menu()
        match decision_menu_lista:
            
            #CALCULAR PROMEDIO
            
            case 1:
                sumatoria=0
                for i in calificaciones:
                    sumatoria+=i
                print(f"Tu promedio es de: {sumatoria/len(calificaciones):.2f}")
                decision_menu_lista=0
                sub_menu()
            #CONTAR CALIFICACIONES MAYORES A UNA CALIFICACION ESPECIFICA
            
            case 2:
                valor=-1
                while not 0<=valor<=100:
                    try:
                        valor=int(input("Ingresa la calificacion a comparar\n"))
                        if not 0<=valor<=100:
                            print("Ingresa una calificacion entre 0 y 100\n")
                    except ValueError:
                        print("Ingresa un valor numerico entero\n")
                        valor=-1
                        
                mayores_que_valor=0
                posicion=0
                while posicion<len(calificaciones):
                    if calificaciones[posicion]>valor:
                        mayores_que_valor+=1
                    posicion+=1
                print(f"Cantidad de calificaciones mayores que {valor} : {mayores_que_valor}")
                decision_menu_lista=0
                sub_menu()
            #CONTAR CUANTAS VECES APARECE UNA MISMA CALIFICACION
            
            case 3:
                calificacion_especifica=-1
                while not 0<=calificacion_especifica<=100:
                    try:
                        calificacion_especifica=int(input("Ingresa la calificacion que deseas buscar\n"))
                        if not 0<=calificacion_especifica<=100:
                            print("Ingresa una calificacion entre 0 y 100\n")
                    except ValueError:
                        print("Ingresa un valor numerico entero\n")
                        calificacion_especifica=-1
                
                contador=0
                for i in calificaciones:
                    if i ==calificacion_especifica:
                        contador+=1
                        continue
                
                if contador > 0:
                    print(f"La calificacion {calificacion_especifica} aparece {contador} veces en la lista.")
                else:
                    print(f"La calificacion {calificacion_especifica} no se encuentra en la lista.")
                decision_menu_lista=0
                sub_menu()
        decision_menu_principal=0
        menu()
        
    ##SALIR##
    
    case 3:
        print("Muchas gracias por usar nuestros servicios")