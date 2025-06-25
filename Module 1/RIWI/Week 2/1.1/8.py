print("Ingresa mes de nacimiento")
while true:
    try:
        M=int(input())
        if 1<=M<=12:
            break
        else:
            print("Ingresa el numero de un mes real")
    except ValueError:
        print("Ingresa el numero del mes")

print("Ingresa dia de nacimiento")

match M:
    case 1, 3, 5, 7, 8, 10, 12:
        while true:
            try:
                D=int(input())
                if 1<=D<=31:
                    break
                else:
                    print("Ingresa un numero de dia valido para tu mes")
            except ValueError:
                print("Ingresa el numero del dia")
    case 4, 6, 9, 11:
        while true:
            try:
                D=int(input())
                if 1<=D<=30:
                    break
                else:
                    print("Ingresa un numero de dia valido para tu mes")
            except ValueError:
                print("Ingresa el numero del dia")
    case 2:
        while true:
            try:
                D=int(input())
                if 1<=D<=29:
                    break
                else:
                    print("Ingresa un numero de dia valido para tu mes")
            except ValueError:
                print("Ingresa el numero del dia")