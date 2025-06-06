Y=int(input("Ingresa tu edad\n"))
G=str(input("Ingresa tu sexo (M/H)\n")).upper()
if (G=="M" and Y>=60) or (G=="H" and Y>=65):
    print("Ya te puedes jubilar")
elif G=="M":
    F=60-Y
    print(f"Te faltan {F} años para jubilarte")
elif G=="H":
    F=65-Y
    print(f"Te faltan {F} años para jubilarte")
else:
    print("Sexo no valido")