Y=int(input("Ingresa tu edad\n"))
if Y>18:
    V=str(input("Has votado antes?(si/no)\n")).lower()
    if V=="si":
        print("Felicidades sera tu primera vez votando")
    else:
        print("Ya has votado antes entonces")