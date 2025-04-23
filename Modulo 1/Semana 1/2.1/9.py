I=int(input("Digite sus ingresos mensuales\n"))
D=str(input("Tiene deudas activas? (si/no)\n")).lower()
T=["Lo siento no cumples los requisitos para recibir la tarjeta", "Felicidades cumples con los requisitos para recibir la tarjeta"]
print(T[I>2500 or (I>1500 and D=="no")])