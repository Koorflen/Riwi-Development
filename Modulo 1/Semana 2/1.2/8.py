D=int(input("Que deseas?\n1. Pedir libro a prestamo\n2. Salir\n"))

match D:
    case 1:
        NL=int(input("Cuantos libros prestados tienes?\n"))
        if NL<3:
            S=str(input("Tienes sanciones?(Si/No)\n")).lower()
            if S=="si":
                print("No se le puede hacer el prestamo")
            else:
                print("Prestamo aprovado")
        else:
                print("No se le puede hacer el prestamo")
    case 2:
        print("Tenga un buen dia")