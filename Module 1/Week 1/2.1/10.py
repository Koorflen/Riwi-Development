H=int(input("Ingresa la hora\n"))
P=["Lo siento no estas en horario permitido", "Estas en horario permitido"]
print(P[8<=H<=18 and H!=13])