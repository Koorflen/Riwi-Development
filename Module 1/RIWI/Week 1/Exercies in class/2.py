Y=int(input("Ingrese su edad\n"))
if Y<18:
    print("No puedes ingresar")
else:
    P=str(input("Tienes pase dorado?(si/no)")).lower()
    if P=="si":
        print("Puedes ingresar")
    else:
        if Y>25:
            print("No puedes ingresar")
        else:
            print("Puedes ingresar")