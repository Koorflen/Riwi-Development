X=float(input("Ingresa dos numeros\n"))
Y=float(input())
M=[f"{X} es menor que {Y}", f"{X} es mayor o igual que {Y}"]
print(f"De los numeros que ingresaste se concluye que: {M[X>=Y]}")